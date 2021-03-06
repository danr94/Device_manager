#!/usr/bin/python


import inLib
import numpy as np
from Utilities import zernike
#from Utilities import pupil_forInControl as pupil
import pupil_forInControl as pupil
from scipy.ndimage import interpolation
from scipy.ndimage import gaussian_filter as gf
from scipy import optimize
import os
import time
import matplotlib.pyplot as plt
import libtim
import libtim.zern
import signalForAO
from skimage.restoration import unwrap_phase


def gaussian(z, a, z0, w, b):
    return a * np.exp(-(z-z0)**2/w) + b


class Control(inLib.Module):
    
    def __init__(self, control, settings):
        print 'Initializing Adaptive Optics.'
        inLib.Module.__init__(self, control, settings)
        dim = self._control.camera.getDimensions()
        # A list to store the indices of the 'Other' modulations, given by the SLM API:
        self._modulations = []
        print 'Adaptive Optics initialized.'

        self.hasSLM = settings['hasSLM']
        self.hasMirror = settings['hasMirror']

        self._PSF = None
        self._PF = None
        self._PFradius = None
        self._sharpness = None
        

        self.sharpnessList = []
        self.zernModesToFit = 22 #Number of zernike modes to fit unwrapped pupil functions

        self._zernFitUnwrapped = None
        self._zernFitUnwrappedModes = None

        self.varyAOactive = True

    def updateImSize(self):
        '''
        Gets the image size from the camera.
        _ui uses this for sharpness calculations...
        '''
        return self._control.camera.getDimensions()
        

    def _getGeo(self):
        '''
        Gets geometry from either SLM (if exist) or elsewhere
        '''
        if self.hasSLM:
            geometry = self._control.slm.getGeometry()
        elif self.hasMirror:
            geometry = self._control.mirror.getGeometry()
        else:
            geometry = None
        return geometry

    def _addMOD(self, MOD):
        # edited by Dan on 07/14
        if self.hasSLM:
            index = self._control.slm.addOther(MOD)
            return index
        if self.hasMirror:
            index = self._control.mirror.addOther(MOD)
            return index
        else:
            return None

    def _setZernModeFirstActive(self, coeff):
        if self.hasSLM:
            self._control.slm.setZernikeModeFirstActive(coeff)

    def _setOtherActive(self,other_index,state):
        if self.hasSLM:
            self._control.slm.setOtherActive(other_index, state)
        if self.hasMirror:
            self._control.mirror.setOtherActive(other_index, state)



    def acquirePSF(self, range_, nSlices, nFrames, center_xy=True, filename=None,
                   mask_size = 40, mask_center = (-1,-1)):
        '''
        Acquires a PSF stack. The PSF is returned but also stored internally.

        :Parameters:
            *range_*: float
                The range of the scan around the current axial position in micrometers.
            *nSlices*: int
                The number of PSF slices to acquire.
            *nFrames*: int
                The number of frames to be averaged for each PSF slice.
            *filename*: str
                The file name into which the PSF will be saved.

        :Returns:
            *PSF*: numpy.array
                An array of shape (k,l,m), where k are the number of PSF slices and
                (l,m) the lateral slice dimensions.
        '''

        # Logging
        self._settings['range'] = range_
        self._settings['nSlices'] = nSlices
        self._settings['nFrames'] = nFrames
        self._settings['filename'] = filename

        # Some parameters
        start = range_/2.0
        end = -range_/2.0
        self._dz = abs(range_/(nSlices-1.0))

        # Scan the PSF:
        scan = self._control.piezoscan.scan(start, end, nSlices, nFrames, filename)

        nz, nx, ny = scan.shape
        # An empty PSF
        PSF = np.zeros_like(scan)
        # Geometry info
        g = pupil.Geometry((nx,ny), nx/2.-0.5, ny/2.-0.5, 16)
        # Filled cylinder:
        cyl = np.array(nz*[g.r_pxl<16])
        new_cyl = np.array(nz*[g.r_pxl<mask_size])
        # Fill the empty PSF with every voxel in scan where cyl=True
        if not center_xy:
            PSF[cyl] = scan[cyl]
        # Hollow cylinder
        hcyl = np.array(nz*[np.logical_and(g.r_pxl>=50, g.r_pxl<61)])
        if mask_center[0] > -1:
            g2 = pupil.Geometry((nx,ny), mask_center[0], mask_center[1], 16)
            mask = g2.r_pxl<mask_size
        else:
            mask = g.r_pxl<mask_size
        if filename:
            np.save(filename+"pre-cut", scan)
        if center_xy:
            # The coordinates of the brightest pixel
            cz, cx, cy = np.unravel_index(np.argmax(gf(scan*mask,2)), scan.shape)
            print "Center found at: ", (cz,cx,cy)
            # We laterally center the scan at the brightest pixel
            cut = scan[:,cx-mask_size:cx+mask_size,cy-mask_size:cy+mask_size]
            PSF = np.zeros((nz,nx,ny))
            PSF[:,nx/2-mask_size:nx/2+mask_size,ny/2-mask_size:ny/2+mask_size] = cut
            # Background estimation
            self._background = np.mean(scan[hcyl])
            print "Background guess: ", self._background
        else:
            self._background = np.mean(scan[hcyl])
        PSF[np.logical_not(new_cyl)] = self._background

        self._PSF = PSF
        if filename:
            np.save(filename, PSF)
        return PSF

    def getSharpness(self, pixelSize=163, diffLimit=800):
        '''
        Finds the sharpnes of self._PSF
        '''
        if self._PSF is None:
            time.sleep(2)
        sharpness = signalForAO.secondMomentOnStack(self._PSF,pixelSize,diffLimit)
        self._sharpness = sharpness
        print "Maximum sharpness = ", sharpness.max()
        return sharpness


    def retrievePF(self, dx, l, n, NA, f, guess, nIt, neglect_defocus=True,
                   invert=False, wavelengths=1, resetAmp=True,
                   symmeterize=False):
        # 08/01: 
        # To be changed: fit the gaussian profile prior to the phase retrieval; 
        # Average the fitting between 5 adjacent columns. 
        
        
        
        '''
        Retrieves the phase of the most recent PSF. The retrieved pupil function is both
        returned and stored internally.

        :Parameters:
            *dx*: float
                The lateral pixel size in micrometers.
            *l*: float
                Emission wavelength in micrometers.
            *n*: float
                Immersion medium refractive index.
            *NA*: float
                Objective numerical aperture.
            *f*: float
                Objective focal length in micrometers.
            *guess*: [('plane',) | ('mirror', z0) | ('file', path)]
                If *('plane',)*, the initial guess is a plane wave.
                If *('mirror',z0)*, the initial guess is the pupil function of an emitter
                with distance *z0* (in micrometers) to a mirror.
                If *('file', path)*, the initial guess is loaded from a file given by *path*.
                The file at *path* has to be a numpy array stored in the .npy format and contain
                the guess in radiants.
            *nIt*: int
                Number of iterations of the phase retrieval algorithms to be performed.
            *gaussian*: float
                If not *None*, a Gaussian filter is applied to the phase after each iteration.
                The standard deviation of the Gaussian kernel is given with this parameter.

        :Returns:
            *PF*: numpy.array
                The complex pupil function. The shape is the same as the shape of the acquired 
                PSF slices.
        '''
        
        # Logging
        self._settings['nIterations'] = nIt

        z_offset = 0
        if neglect_defocus:
            # We try to estimate the axial position of the emitter
            # The coordinates of the brightest pixel
            cz, cx, cy = np.unravel_index(self._PSF.argmax(), self._PSF.shape)
            # Intensity trace along z
            im_z = self._PSF[:,cx,cy]
            # Get z positions
            nz = self._PSF.shape[0]
            upper = 0.5*(nz-1)*self._dz
            z = np.linspace(-upper, upper, nz)
            # Initial fit parameters
            b = np.mean((im_z[0],im_z[-1]))
            a = im_z.max() - b
            w = l/3.2
            p0 = (a,0,w,b)
            
            # Fit gaussian to axial intensity trace
            popt, pcov = optimize.curve_fit(gaussian, z, im_z, p0)
            # Where we think the emitter is axially located:
            z_offset = popt[1] # The original version is wrong
            plt.plot(z, im_z)
            plt.plot(z, gaussian(z,*popt))
            plt.savefig('z_fit.png')

        nx,ny = self._PSF.shape[1:3]
        self._pupil = pupil.Simulation(nx,dx,l,n,NA,f,wavelengths=wavelengths)
        if guess[0] == 'plane':
            A = self._pupil.plane
        elif guess[0] == 'mirror':
            z0 = guess[1]
            A = np.angle(self._pupil.get_sli_pupil_function(z0,0.0))
            A = np.nan_to_num(A)
        elif guess[0] == 'file':
            A = np.load(guess[1])      
        else:
            A = self._pupil.plane

        print "Finding PF..."
        print "   Using parameters:"
        print "   dz = ", self._dz
        print "   background = ", self._background
        print "   z_offset = ", z_offset
        complex_PF = self._pupil.psf2pf(self._PSF, self._dz, self._background, A, nIt, z_offset,
                                        resetAmp=resetAmp,symmeterize=symmeterize)

        if invert:
            complex_PF = abs(complex_PF) * np.exp(-1*1j*np.angle(complex_PF))

        self._PF = _PupilFunction(complex_PF, self._pupil)

        nz = self._PSF.shape[0]
        upper = 0.5*(nz-1)*self._dz
        z = np.linspace(-upper, upper, nz)
        psft = self._pupil.pf2psf(complex_PF, z)
        np.save('retrieved_psf', psft)

        return self._PF.phase


    def fit(self):
        '''
        Fits the most recent pupil function to Zernike modes up to the fourth order.

        :Returns:
            *p*: numpy.array
                A 1-dimensional array of Zernike coefficients. Array indices correspond to
                the Noll coefficient *j* of Zernike modes.
            *PF*: numpy.array
                The phase pupil function as produced by the phase retrieval algorithm with Zernike
                coefficients.
        '''
        ''' Old fitting procedure
        p, success, error = zernike.fit_to_basic_set(self._PF.phase, np.zeros(15),
                self._pupil.r, self._pupil.theta)
        self._PF.zernike_coefficients = p
        '''
        nx,ny = self._PF.phase.shape
        self._PFradius = np.sum(self._pupil.r[nx/2,:]<1)/2
        print "Radius of fitted zernike: ", self._PFradius
        #fitResults = libtim.zern.fit_zernike(self._PF.phase, rad=radius, nmodes=15)
        unwrapped=self.unwrap()
        print "Unwrapped!"
        
        fitResults_wrong = libtim.zern.fit_zernike(self._PF.phase, rad=radius, nmodes=21)
        fitResults = libtim.zern.fit_zernike(unwrapped, rad=radius, nmodes=21)
        self._PF.zernike_coefficients = fitResults[0]
        #print("unwrapped:", fitResults[0])
        #print("original:", fitResults_wrong[0])
        
        return self._PF

    def unwrap(self):
        unwrapped = unwrap_phase(self._PF.phase)
        return unwrapped

    def setZernModesToFit(self, nmodes):
        self.zernModesToFit = nmodes

    def zernFitUnwrapped(self, skip4orders=False):
        unwrapped = self.unwrap()

        #geometry = self._control.slm.getGeometry()
        geometry = self._getGeo()

        nx,ny = unwrapped.shape
        rad = np.sum(self._pupil.r[nx/2,:]<1)/2

        if skip4orders:
            zernModes, resultFit, errFit = libtim.zern.fit_zernike(unwrapped, nmodes=self.zernModesToFit, rad=rad,
                                                                   startmode=5)
        else:
            zernModes, resultFit, errFit = libtim.zern.fit_zernike(unwrapped, nmodes=self.zernModesToFit, rad=rad)

        MOD0 = resultFit
        newMOD = np.zeros((geometry.nx,geometry.ny))
        nx,ny = MOD0.shape
        newMOD[geometry.cx-np.floor(nx/2.):geometry.cx+np.ceil(nx/2.),geometry.cy-np.floor(ny/2.0):geometry.cy+np.ceil(ny/2.)] = MOD0.copy()
        self._zernFitUnwrapped = newMOD
        self._zernFitUnwrappedModes = zernModes

        return resultFit

    def modZernFitUnwrapped(self, useMask=False, radius=0):
        #geometry = self._control.slm.getGeometry()
        geometry = self._getGeo()
        d = geometry.d
        if radius==0:
            r = d/2
        else:
            r = radius
        cx = geometry.cx
        cy = geometry.cy
        if self._zernFitUnwrappedModes is not None:
            print "ZernFitUnwrapped Modes: ", self._zernFitUnwrappedModes
            print "Radius for zernCalc: ", r
#             zernCalc = libtim.zern.calc_zernike(self._zernFitUnwrappedModes, r, mask=useMask)
            zernCalc = libtim.zern.calc_zernike(self._zernFitUnwrappedModes, r, mask = True)
            MOD = -1*zernCalc
            MOD = np.flipud(MOD)
            MOD = np.rot90(MOD)
            MOD = np.rot90(-1.0*MOD)
            #MOD = interpolation.shift(MOD,(cy-255.5,cx-255.5),order=0,
            #                                       mode='nearest')
            newMOD = np.zeros((geometry.nx,geometry.ny))
            nx,ny = MOD.shape
            newMOD[cy-np.floor(nx/2.):cy+np.ceil(nx/2.),cx-np.floor(ny/2.):cx+np.ceil(ny/2.)] = MOD.copy()
            if self.hasSLM:
                index = self._control.slm.addOther(newMOD)
            else:
                # tried on 07/21
#                 index = self._control.mirror.addOther(newMOD)
                index = self._control.mirror.addOther(newMOD)
            self._modulations.append(index)
            return index


    def removePTTD(self):
        # remove the first four Zernike modes
        p = self._PF.zernike_coefficients
        p[0:4] = 0
        self._PF.zernike_coefficients = p
        #self._PF.zernike_coefficients[0:4] = 0
        return self._PF

    
    def modulatePF(self, use_zernike=True):
        '''
        Sends phase of the current internally stored pupil function to the SLM.

        :Returns:
            *index*: int
                Each modulation that is sent to the SLM by the AdaptiveOptics module has an
                individual index, which can be used later to access this modulation.
        '''
        print 'Modulating pupil function.'

        #geometry = self._control.slm.getGeometry()
        geometry = self._getGeo()
        if use_zernike:
            # The SLM vs camera image is flipped upside down. That's why we define a
            # flipped theta:
            #x_pxl = -geometry.x_pxl
            #theta = np.arctan2(geometry.y_pxl, x_pxl)
            #MOD = -zernike.basic_set(self._PF.zernike_coefficients, geometry.r, theta)
            if self._zernFitUnwrappedModes is not None:
                print "ZernFitUnwrapped Modes: ", self._zernFitUnwrappedModes
                zernCalc = libtim.zern.calc_zernike(self._zernFitUnwrappedModes,geometry.d/2.0, mask = True,
                                               zern_data ={})
                MOD0=-1*zernCalc

            else:
                print "not pre-fitted!"
                MOD0 = -1*libtim.zern.calc_zernike(self._PF.zernike_coefficients, geometry.d/2.0, mask= False,
                                               zern_data ={})
            print "Using zernike to modulate. Radius of calculated mod: ", (geometry.d/2.0)
            np.save("testing_mod0.npy", MOD0)
            MOD0 = np.flipud(MOD0)
            MOD0 = np.rot90(MOD0)
            MOD0 = np.rot90(-1.0*MOD0)
            MODx,MODy = MOD0.shape
            newMOD = np.zeros((geometry.nx,geometry.ny))
            newMOD[geometry.cx-np.floor(MODx/2.):geometry.cx+np.ceil(MODx/2.),geometry.cy-np.floor(MODy/2.0):geometry.cy+np.ceil(MODy/2.)] = MOD0.copy()
            MOD = newMOD
            
        
        else:
            MOD = -1*self._PF.phase
            MOD = np.flipud(MOD)
            MOD = np.rot90(MOD)
            cx,cy,d = geometry.cx, geometry.cy, geometry.d
            # Diameter of phase retrieval output [pxl]:
            dPhRt = (self._pupil.k_max/self._pupil.kx.max())*self._pupil.nx
            # Zoom needed to fit onto SLM map:
            zoom = d/dPhRt
            MOD = interpolation.zoom(MOD,zoom,order=0,mode='nearest')
            # Flip up down:
            #MOD = np.flipud(MOD)
            # Flip left right:
            #MOD = np.fliplr(MOD)
            #MOD = np.rot90(MOD)
            MOD = np.rot90(-1.0*MOD) #Invert and rot90
            # Shift center:
            MOD = interpolation.shift(MOD,(cy-255.5,cx-255.5),order=0,
                                                   mode='nearest')
            # Cut out center 512x512:
            c = MOD.shape[0]/2
            MOD = MOD[c-256:c+256,c-256:c+256]

        
        # Add an 'Other' modulation using the SLM API. Store the index in _modulations:
        #index = self._control.slm.addOther(MOD)
        index = self._addMOD(MOD)
        self._modulations.append(index)
        return index



    def savePF(self, filename):
        '''
        Saves the most recent pupil function in InControl's working directory.

        :Parameters:
            *filename*: str
        '''
        working_dir = self._control.getWorkingDir()
        np.save(os.path.join(working_dir, filename + '_complex.npy'), self._PF.complex)
        np.save(os.path.join(working_dir, filename + '_amplitude.npy'), self._PF.amplitude)
        np.save(os.path.join(working_dir, filename + '_phase.npy'), self._PF.phase)


    def setModulationActive(self, index, state):
        '''
        Enables or disables a modulation.

        :Parameters:
            *index*: int
                The modulation index given by :func:`modulatePF`.
            *state*: bool
                If True, the modulation at *index* is enabled.
        '''
        # Retrieve the index of the respective 'Other' Modulation, generated previously by the
        # SLM API:
        other_index = self._modulations[index]
        #self._control.slm.setOtherActive(other_index, state)
        self._setOtherActive(other_index,state)


    def getNumberOfZernToVary(self):
        if self.hasMirror:
            num = self._control.mirror.getNumberOfZernToVary()
        elif self.hasSLM:
            num = 100
        else:
            num = 0
        return num


    def findSharpnessEachFrame(self, pixelSize, diffLimit, mask=None):
        frame_length = 1.0/self._control.camera.getFrameRate()
        #np_image = self._control._control.camera.getImageForPreview()
        im = self._control.camera.getMostRecentImageNumpy()
        if mask is not None:
            background_est = np.median(im * np.logical_not(mask))
            im = (im * mask) + (background_est * np.logical_not(mask))
        if im is not None:
            sharpness = signalForAO.secondMoment(im,pixelSize,diffLimit)
            if len(self.sharpnessList)<200:
                self.sharpnessList.append(sharpness)
            else:
                self.sharpnessList = self.sharpnessList[1:] + [sharpness]
        else:
            sharpness = None
        time.sleep(frame_length)
        return sharpness, self.sharpnessList



class _PupilFunction(object):
    '''
    A pupil function that keeps track when when either complex or amplitude/phase
    representation is changed.
    '''
    def __init__(self, cmplx, geometry):
        self._complex = cmplx
        self._geometry = geometry

    @property
    def complex(self):
        return self._complex

    @complex.setter
    def complex(self, new):
        self._complex = new
        self._amplitude = abs(new)
        self._phase = unwrap_phase(np.angle(new))

    @property
    def amplitude(self):
        return self._amplitude

    @amplitude.setter
    def amplitude(self, new):
        self._amplitude = new
        self._complex = new * np.exp(1j*self._phase)

    @property
    def phase(self):
        return self._phase

    @phase.setter
    def phase(self, new):
        self._phase = new
        self._complex = self._amplitude * np.exp(1j*new)

    @property
    def zernike_coefficients(self):
        return self._zernike_coefficients

    @zernike_coefficients.setter
    def zernike_coefficients(self, new):
        self._zernike_coefficients = new
        #self._zernike = zernike.basic_set(new, self._geometry.r, self._geometry.theta)
        self._zernike = libtim.zern.calc_zernike(new, self._geometry.nx/2.0, mask = True)

    @property
    def zernike(self):
        return self._zernike
