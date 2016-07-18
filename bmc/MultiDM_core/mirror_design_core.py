# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mirror_design.ui'
#
# Created: Wed Jun 17 15:20:43 2015
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!
"""
Function list from MultiDM_core_ui:

self._ui.pushButton_load.clicked.connect(self.loadPattern)
        self._ui.pushButton_rot90.clicked.connect(self.patternRot90)
        self._ui.pushButton_fliplr.clicked.connect(self.patternFlipLR)
        self._ui.pushButton_flipud.clicked.connect(self.patternFlipUD)
        self._ui.pushButton_rotate.clicked.connect(self.patternRotate)
        self._ui.pushButton_getSegs.clicked.connect(self.getSegments)
        self._ui.pushButton_toMirror.clicked.connect(self.toMirror)
        self._ui.pushButton_reconfig.clicked.connect(self.reconfig)
        self._ui.pushButton_mult.clicked.connect(self.setMultiplier)
        self._ui.pushButton_premult.clicked.connect(self.setPreMultiplier)
        self._ui.pushButton_poke.clicked.connect(self.pokeSegment)
        self._ui.pushButton_clear.clicked.connect(self.clearPattern)
        self._ui.pushButton_refresh.clicked.connect(self.refreshPattern)
        self._ui.pushButton_pad.clicked.connect(self.padZeros)
        self._ui.pushButton_applyZern.clicked.connect(self.calcZernike)
        self._ui.pushButton_modulateZernike.clicked.connect(self.modZernike)
        self._ui.pushButton_createGroup.clicked.connect(self.createGroup)
        self._ui.pushButton_setToGroup.clicked.connect(self.setGroupVal) 
"""



from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(781, 617)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Deformable Mirror", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Pattern", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.pushButton_rot90 = QtGui.QPushButton(self.groupBox)
        self.pushButton_rot90.setText(QtGui.QApplication.translate("Form", "Rotate 90", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_rot90.setObjectName(_fromUtf8("pushButton_rot90"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.pushButton_rot90)
        self.pushButton_fliplr = QtGui.QPushButton(self.groupBox)
        self.pushButton_fliplr.setText(QtGui.QApplication.translate("Form", "Flip L-R", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_fliplr.setObjectName(_fromUtf8("pushButton_fliplr"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.pushButton_fliplr)
        self.pushButton_rotate = QtGui.QPushButton(self.groupBox)
        self.pushButton_rotate.setText(QtGui.QApplication.translate("Form", "Rotate", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_rotate.setObjectName(_fromUtf8("pushButton_rotate"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.LabelRole, self.pushButton_rotate)
        self.lineEdit_rotate = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_rotate.setObjectName(_fromUtf8("lineEdit_rotate"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.FieldRole, self.lineEdit_rotate)
        self.pushButton_pad = QtGui.QPushButton(self.groupBox)
        self.pushButton_pad.setText(QtGui.QApplication.translate("Form", "Pad Zeros", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_pad.setObjectName(_fromUtf8("pushButton_pad"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.LabelRole, self.pushButton_pad)
        self.lineEdit_pad = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_pad.setObjectName(_fromUtf8("lineEdit_pad"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.FieldRole, self.lineEdit_pad)
        self.pushButton_getSegs = QtGui.QPushButton(self.groupBox)
        self.pushButton_getSegs.setText(QtGui.QApplication.translate("Form", "Calculate Segments", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_getSegs.setObjectName(_fromUtf8("pushButton_getSegs"))
        self.formLayout.setWidget(14, QtGui.QFormLayout.SpanningRole, self.pushButton_getSegs)
        self.pushButton_load = QtGui.QPushButton(self.groupBox)
        self.pushButton_load.setText(QtGui.QApplication.translate("Form", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_load.setObjectName(_fromUtf8("pushButton_load"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.pushButton_load)
        self.lineEdit_loadMult = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_loadMult.setObjectName(_fromUtf8("lineEdit_loadMult"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_loadMult)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(QtGui.QApplication.translate("Form", "Center x:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setText(QtGui.QApplication.translate("Form", "Center y:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_cx = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_cx.setObjectName(_fromUtf8("lineEdit_cx"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_cx)
        self.lineEdit_cy = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_cy.setObjectName(_fromUtf8("lineEdit_cy"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit_cy)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setText(QtGui.QApplication.translate("Form", "Number of pxls:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_npixels = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_npixels.setObjectName(_fromUtf8("lineEdit_npixels"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEdit_npixels)
        self.pushButton_reconfig = QtGui.QPushButton(self.groupBox)
        self.pushButton_reconfig.setText(QtGui.QApplication.translate("Form", "Reconfig Geometry", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_reconfig.setObjectName(_fromUtf8("pushButton_reconfig"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.SpanningRole, self.pushButton_reconfig)
        self.pushButton_mult = QtGui.QPushButton(self.groupBox)
        self.pushButton_mult.setText(QtGui.QApplication.translate("Form", "Multiplier", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_mult.setObjectName(_fromUtf8("pushButton_mult"))
        self.formLayout.setWidget(16, QtGui.QFormLayout.LabelRole, self.pushButton_mult)
        self.lineEdit_mult = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_mult.setObjectName(_fromUtf8("lineEdit_mult"))
        self.formLayout.setWidget(16, QtGui.QFormLayout.FieldRole, self.lineEdit_mult)
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 50))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "Poke One Segment", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setText(QtGui.QApplication.translate("Form", "Segment", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setText(QtGui.QApplication.translate("Form", "Addition", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 1, 1, 1, 1)
        self.spinBox_segment = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_segment.setMinimum(1)
        self.spinBox_segment.setMaximum(144)
        self.spinBox_segment.setObjectName(_fromUtf8("spinBox_segment"))
        self.gridLayout_2.addWidget(self.spinBox_segment, 2, 0, 1, 1)
        self.lineEdit_pokeval = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_pokeval.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_pokeval.setObjectName(_fromUtf8("lineEdit_pokeval"))
        self.gridLayout_2.addWidget(self.lineEdit_pokeval, 2, 1, 1, 1)
        self.pushButton_poke = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_poke.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_poke.setText(QtGui.QApplication.translate("Form", "Set", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_poke.setObjectName(_fromUtf8("pushButton_poke"))
        self.gridLayout_2.addWidget(self.pushButton_poke, 2, 2, 1, 1)
        self.checkBox_pokeAll = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_pokeAll.setText(QtGui.QApplication.translate("Form", "All ", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_pokeAll.setObjectName(_fromUtf8("checkBox_pokeAll"))
        self.gridLayout_2.addWidget(self.checkBox_pokeAll, 0, 0, 1, 1)
        self.formLayout.setWidget(17, QtGui.QFormLayout.SpanningRole, self.groupBox_2)
        self.pushButton_toMirror = QtGui.QPushButton(self.groupBox)
        self.pushButton_toMirror.setText(QtGui.QApplication.translate("Form", "Apply to Mirror", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_toMirror.setObjectName(_fromUtf8("pushButton_toMirror"))
        self.formLayout.setWidget(18, QtGui.QFormLayout.SpanningRole, self.pushButton_toMirror)
        self.pushButton_clear = QtGui.QPushButton(self.groupBox)
        self.pushButton_clear.setText(QtGui.QApplication.translate("Form", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_clear.setObjectName(_fromUtf8("pushButton_clear"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.pushButton_clear)
        
        # refresh button        
        self.pushButton_refresh = QtGui.QPushButton(self.groupBox)
        self.pushButton_refresh.setText(QtGui.QApplication.translate("Form", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_refresh.setObjectName(_fromUtf8("pushButton_refresh"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.pushButton_refresh)
        self.pushButton_premult = QtGui.QPushButton(self.groupBox)
        self.pushButton_premult.setText(QtGui.QApplication.translate("Form", "Pre Multiplier", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_premult.setObjectName(_fromUtf8("pushButton_premult"))
        self.formLayout.setWidget(15, QtGui.QFormLayout.LabelRole, self.pushButton_premult)
        self.lineEdit_premult = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_premult.setObjectName(_fromUtf8("lineEdit_premult"))
        self.formLayout.setWidget(15, QtGui.QFormLayout.FieldRole, self.lineEdit_premult)
        self.pushButton_flipud = QtGui.QPushButton(self.groupBox)
        self.pushButton_flipud.setText(QtGui.QApplication.translate("Form", "Flip U-D", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_flipud.setObjectName(_fromUtf8("pushButton_flipud"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.pushButton_flipud)
        self.pushButton_loadSegs = QtGui.QPushButton(self.groupBox)
        self.pushButton_loadSegs.setText(QtGui.QApplication.translate("Form", "Load Segs", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_loadSegs.setObjectName(_fromUtf8("pushButton_loadSegs"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.pushButton_loadSegs)
        self.checkBox_alwayspad = QtGui.QCheckBox(self.groupBox)
        self.checkBox_alwayspad.setText(QtGui.QApplication.translate("Form", "Always pad?", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_alwayspad.setObjectName(_fromUtf8("checkBox_alwayspad"))
        self.formLayout.setWidget(12, QtGui.QFormLayout.FieldRole, self.checkBox_alwayspad)
        self.horizontalLayout.addWidget(self.groupBox)
        self.tabWidgetPF = QtGui.QTabWidget(Form)
        self.tabWidgetPF.setEnabled(True)
        self.tabWidgetPF.setIconSize(QtCore.QSize(15, 16))
        self.tabWidgetPF.setObjectName(_fromUtf8("tabWidgetPF"))
        self.tabWidgetPFPage1 = QtGui.QWidget()
        self.tabWidgetPFPage1.setObjectName(_fromUtf8("tabWidgetPFPage1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tabWidgetPFPage1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mplwidgetPhase = MatplotlibWidget(self.tabWidgetPFPage1)
        self.mplwidgetPhase.setObjectName(_fromUtf8("mplwidgetPhase"))
        self.verticalLayout.addWidget(self.mplwidgetPhase)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_Save = QtGui.QPushButton(self.tabWidgetPFPage1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Save.sizePolicy().hasHeightForWidth())
        self.pushButton_Save.setSizePolicy(sizePolicy)
        self.pushButton_Save.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_Save.setText(QtGui.QApplication.translate("Form", "Save to file", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Save.setObjectName(_fromUtf8("pushButton_Save"))
        self.gridLayout.addWidget(self.pushButton_Save, 1, 1, 1, 1)
        self.pushButton_Modulate = QtGui.QPushButton(self.tabWidgetPFPage1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Modulate.sizePolicy().hasHeightForWidth())
        
        # 07/14 is this pushButton Modulate under Zernike tab?
        self.pushButton_Modulate.setSizePolicy(sizePolicy)
        self.pushButton_Modulate.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_Modulate.setText(QtGui.QApplication.translate("Form", "Modulate", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Modulate.setObjectName(_fromUtf8("pushButton_Modulate"))
        self.gridLayout.addWidget(self.pushButton_Modulate, 1, 3, 1, 1)
        self.pushButton_Load = QtGui.QPushButton(self.tabWidgetPFPage1)
        self.pushButton_Load.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_Load.setText(QtGui.QApplication.translate("Form", "Fit to Zernike", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Load.setObjectName(_fromUtf8("pushButton_Load"))
        self.gridLayout.addWidget(self.pushButton_Load, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.tabWidgetPF.addTab(self.tabWidgetPFPage1, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.mplwidgetSegs = MatplotlibWidget(self.tab_4)
        self.mplwidgetSegs.setGeometry(QtCore.QRect(0, 0, 371, 371))
        self.mplwidgetSegs.setObjectName(_fromUtf8("mplwidgetSegs"))
        self.label_meanSeg = QtGui.QLabel(self.tab_4)
        self.label_meanSeg.setGeometry(QtCore.QRect(30, 410, 121, 16))
        self.label_meanSeg.setText(QtGui.QApplication.translate("Form", "Mean: --", None, QtGui.QApplication.UnicodeUTF8))
        self.label_meanSeg.setObjectName(_fromUtf8("label_meanSeg"))
        self.label_maxSeg = QtGui.QLabel(self.tab_4)
        self.label_maxSeg.setGeometry(QtCore.QRect(30, 440, 121, 16))
        self.label_maxSeg.setText(QtGui.QApplication.translate("Form", "Maximum: --", None, QtGui.QApplication.UnicodeUTF8))
        self.label_maxSeg.setObjectName(_fromUtf8("label_maxSeg"))
        self.label_minSeg = QtGui.QLabel(self.tab_4)
        self.label_minSeg.setGeometry(QtCore.QRect(30, 470, 141, 16))
        self.label_minSeg.setText(QtGui.QApplication.translate("Form", "Minimum: --", None, QtGui.QApplication.UnicodeUTF8))
        self.label_minSeg.setObjectName(_fromUtf8("label_minSeg"))
        self.tabWidgetPF.addTab(self.tab_4, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.mplwidgetSharpness2 = MatplotlibWidget(self.tab)
        self.mplwidgetSharpness2.setObjectName(_fromUtf8("mplwidgetSharpness2"))
        self.verticalLayout_2.addWidget(self.mplwidgetSharpness2)
        self.tabWidgetPF.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.mplwidgetZern = MatplotlibWidget(self.tab_2)
        self.mplwidgetZern.setGeometry(QtCore.QRect(10, 0, 380, 349))
        self.mplwidgetZern.setObjectName(_fromUtf8("mplwidgetZern"))
        
        # This is modulate zernike 
        self.pushButton_modulateZernike = QtGui.QPushButton(self.tab_2)
        self.pushButton_modulateZernike.setGeometry(QtCore.QRect(20, 350, 75, 23))
        self.pushButton_modulateZernike.setText(QtGui.QApplication.translate("Form", "Add Zernike", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_modulateZernike.setObjectName(_fromUtf8("pushButton_modulateZernike"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 370, 391, 151))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Form", "Add Zernike", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 48, 30, 16))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Mode:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(121, 48, 51, 16))
        self.label_7.setText(QtGui.QApplication.translate("Form", "Amplitude:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.spinBox_zernMode = QtGui.QSpinBox(self.groupBox_3)
        self.spinBox_zernMode.setGeometry(QtCore.QRect(52, 48, 63, 19))
        self.spinBox_zernMode.setMinimum(1)
        self.spinBox_zernMode.setObjectName(_fromUtf8("spinBox_zernMode"))
        self.lineEdit_zernAmp = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_zernAmp.setGeometry(QtCore.QRect(178, 48, 50, 19))
        self.lineEdit_zernAmp.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_zernAmp.setObjectName(_fromUtf8("lineEdit_zernAmp"))
        self.checkBox_zernMask = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox_zernMask.setGeometry(QtCore.QRect(234, 49, 47, 17))
        self.checkBox_zernMask.setText(QtGui.QApplication.translate("Form", "Mask", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_zernMask.setObjectName(_fromUtf8("checkBox_zernMask"))
        self.pushButton_applyZern = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_applyZern.setGeometry(QtCore.QRect(289, 48, 86, 19))
        self.pushButton_applyZern.setText(QtGui.QApplication.translate("Form", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_applyZern.setObjectName(_fromUtf8("pushButton_applyZern"))
        self.spinBox_numZerns = QtGui.QSpinBox(self.groupBox_3)
        self.spinBox_numZerns.setGeometry(QtCore.QRect(52, 73, 63, 19))
        self.spinBox_numZerns.setMinimum(1)
        self.spinBox_numZerns.setMaximum(999)
        self.spinBox_numZerns.setObjectName(_fromUtf8("spinBox_numZerns"))
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(10, 73, 25, 16))
        self.label_8.setText(QtGui.QApplication.translate("Form", "Num:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(121, 73, 44, 16))
        self.label_9.setText(QtGui.QApplication.translate("Form", "Min Amp:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(121, 98, 48, 16))
        self.label_10.setText(QtGui.QApplication.translate("Form", "Max Amp:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.lineEdit_minZAmp = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_minZAmp.setGeometry(QtCore.QRect(178, 73, 50, 19))
        self.lineEdit_minZAmp.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_minZAmp.setText(QtGui.QApplication.translate("Form", "-1", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_minZAmp.setObjectName(_fromUtf8("lineEdit_minZAmp"))
        self.lineEdit_maxZAmp = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_maxZAmp.setGeometry(QtCore.QRect(178, 98, 50, 19))
        self.lineEdit_maxZAmp.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_maxZAmp.setText(QtGui.QApplication.translate("Form", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_maxZAmp.setObjectName(_fromUtf8("lineEdit_maxZAmp"))
        self.label_11 = QtGui.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(10, 98, 26, 16))
        self.label_11.setText(QtGui.QApplication.translate("Form", "Wait:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.lineEdit_wTime = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_wTime.setGeometry(QtCore.QRect(52, 98, 63, 19))
        self.lineEdit_wTime.setText(QtGui.QApplication.translate("Form", "-1", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_wTime.setObjectName(_fromUtf8("lineEdit_wTime"))
        self.checkBox_zernWithSharpness = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox_zernWithSharpness.setGeometry(QtCore.QRect(234, 74, 141, 17))
        self.checkBox_zernWithSharpness.setText(QtGui.QApplication.translate("Form", "With running sharpness?", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_zernWithSharpness.setObjectName(_fromUtf8("checkBox_zernWithSharpness"))
        self.label_14 = QtGui.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(10, 23, 36, 16))
        self.label_14.setText(QtGui.QApplication.translate("Form", "Radius:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.lineEdit_zernRad = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_zernRad.setGeometry(QtCore.QRect(52, 23, 63, 19))
        self.lineEdit_zernRad.setText(QtGui.QApplication.translate("Form", "256", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_zernRad.setObjectName(_fromUtf8("lineEdit_zernRad"))
        self.checkBox_clearFirst = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox_clearFirst.setGeometry(QtCore.QRect(234, 99, 75, 17))
        self.checkBox_clearFirst.setText(QtGui.QApplication.translate("Form", "Clear first?", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_clearFirst.setChecked(True)
        self.checkBox_clearFirst.setObjectName(_fromUtf8("checkBox_clearFirst"))
       
        self.tabWidgetPF.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.mplwidgetGrouped = MatplotlibWidget(self.tab_3)
        self.mplwidgetGrouped.setGeometry(QtCore.QRect(-10, 0, 380, 349))
        self.mplwidgetGrouped.setObjectName(_fromUtf8("mplwidgetGrouped"))
        self.label_12 = QtGui.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(10, 360, 291, 16))
        self.label_12.setText(QtGui.QApplication.translate("Form", "Enter segments to group together (comma separated):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.lineEdit_group = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_group.setGeometry(QtCore.QRect(10, 380, 351, 20))
        self.lineEdit_group.setObjectName(_fromUtf8("lineEdit_group"))
        self.pushButton_createGroup = QtGui.QPushButton(self.tab_3)
        self.pushButton_createGroup.setGeometry(QtCore.QRect(14, 410, 121, 23))
        self.pushButton_createGroup.setText(QtGui.QApplication.translate("Form", "Create Group", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_createGroup.setObjectName(_fromUtf8("pushButton_createGroup"))
        self.lineEdit_groupVal = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_groupVal.setGeometry(QtCore.QRect(10, 450, 81, 20))
        self.lineEdit_groupVal.setObjectName(_fromUtf8("lineEdit_groupVal"))
        self.pushButton_setToGroup = QtGui.QPushButton(self.tab_3)
        self.pushButton_setToGroup.setGeometry(QtCore.QRect(100, 450, 121, 23))
        self.pushButton_setToGroup.setText(QtGui.QApplication.translate("Form", "Add value to group", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_setToGroup.setObjectName(_fromUtf8("pushButton_setToGroup"))
        self.pushButton_toMirrorGroupVary = QtGui.QPushButton(self.tab_3)
        self.pushButton_toMirrorGroupVary.setGeometry(QtCore.QRect(100, 480, 121, 23))
        self.pushButton_toMirrorGroupVary.setText(QtGui.QApplication.translate("Form", "Vary Group", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_toMirrorGroupVary.setObjectName(_fromUtf8("pushButton_toMirrorGroupVary"))
        self.label_13 = QtGui.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(230, 480, 141, 16))
        self.label_13.setText(QtGui.QApplication.translate("Form", "Use params in previous tab", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.tabWidgetPF.addTab(self.tab_3, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.mplwidget2x2 = MatplotlibWidget(self.tab_5)
        self.mplwidget2x2.setGeometry(QtCore.QRect(0, 0, 380, 349))
        self.mplwidget2x2.setObjectName(_fromUtf8("mplwidget2x2"))
        self.tabWidgetPF.addTab(self.tab_5, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidgetPF)
        self.groupBoxModulations = QtGui.QGroupBox(Form)
        self.groupBoxModulations.setTitle(QtGui.QApplication.translate("Form", "Modulations", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxModulations.setCheckable(True)
        self.groupBoxModulations.setObjectName(_fromUtf8("groupBoxModulations"))
        self.verticalLayoutModulations = QtGui.QVBoxLayout(self.groupBoxModulations)
        self.verticalLayoutModulations.setObjectName(_fromUtf8("verticalLayoutModulations"))
        spacerItem = QtGui.QSpacerItem(20, 317, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayoutModulations.addItem(spacerItem)
        
        
        # 07/17: connect pushButton_setMods
        self.pushButton_setMods = QtGui.QPushButton(self.groupBoxModulations)
        self.pushButton_setMods.setText(QtGui.QApplication.translate("Form", "Set modulations", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_setMods.setObjectName(_fromUtf8("pushButton_setMods"))
        self.verticalLayoutModulations.addWidget(self.pushButton_setMods)
        self.horizontalLayout.addWidget(self.groupBoxModulations)        
        
        
        
        self.label_filenameloaded = QtGui.QLabel(self.groupBoxModulations)
        self.label_filenameloaded.setText(QtGui.QApplication.translate("Form", "--", None, QtGui.QApplication.UnicodeUTF8))
        self.label_filenameloaded.setObjectName(_fromUtf8("label_filenameloaded"))
        self.verticalLayoutModulations.addWidget(self.label_filenameloaded)
        self.horizontalLayout.addWidget(self.groupBoxModulations)



        self.retranslateUi(Form)
        self.tabWidgetPF.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        self.tabWidgetPF.setTabText(self.tabWidgetPF.indexOf(self.tabWidgetPFPage1), QtGui.QApplication.translate("Form", "Pattern", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetPF.setTabText(self.tabWidgetPF.indexOf(self.tab_4), QtGui.QApplication.translate("Form", "Segment", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetPF.setTabText(self.tabWidgetPF.indexOf(self.tab), QtGui.QApplication.translate("Form", "Running Sharpness", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetPF.setTabText(self.tabWidgetPF.indexOf(self.tab_2), QtGui.QApplication.translate("Form", "Zernikes", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetPF.setTabText(self.tabWidgetPF.indexOf(self.tab_3), QtGui.QApplication.translate("Form", "GroupSegs", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetPF.setTabText(self.tabWidgetPF.indexOf(self.tab_5), QtGui.QApplication.translate("Form", "2x2", None, QtGui.QApplication.UnicodeUTF8))

from matplotlibwidget import MatplotlibWidget
