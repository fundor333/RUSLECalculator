# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RUSLECalculator_dialog_base.ui'
#
# Created: Wed Apr 29 08:50:13 2015
# by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MatrixElaboratorDialogBase(object):
    def setupUi(self, MatrixElaboratorDialogBase):
        MatrixElaboratorDialogBase.setObjectName(_fromUtf8("MatrixElaboratorDialogBase"))
        MatrixElaboratorDialogBase.resize(670, 600)
        self.button_box = QtGui.QDialogButtonBox(MatrixElaboratorDialogBase)
        self.button_box.setGeometry(QtCore.QRect(470, 540, 171, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.groupBox_7 = QtGui.QGroupBox(MatrixElaboratorDialogBase)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 10, 641, 271))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.groupBox = QtGui.QGroupBox(self.groupBox_7)
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 631, 31))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.inputDEM = QtGui.QTextEdit(self.groupBox)
        self.inputDEM.setGeometry(QtCore.QRect(130, 0, 451, 31))
        self.inputDEM.setObjectName(_fromUtf8("inputDEM"))
        self.DEM = QtGui.QPushButton(self.groupBox)
        self.DEM.setGeometry(QtCore.QRect(580, -9, 51, 41))
        self.DEM.setObjectName(_fromUtf8("DEM"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_7)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 110, 631, 31))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.SoilImage = QtGui.QPushButton(self.groupBox_3)
        self.SoilImage.setGeometry(QtCore.QRect(580, -9, 51, 41))
        self.SoilImage.setObjectName(_fromUtf8("SoilImage"))
        self.inputK = QtGui.QTextEdit(self.groupBox_3)
        self.inputK.setGeometry(QtCore.QRect(130, 0, 451, 31))
        self.inputK.setObjectName(_fromUtf8("inputK"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox_7)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 70, 631, 31))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.FieldImage = QtGui.QPushButton(self.groupBox_2)
        self.FieldImage.setGeometry(QtCore.QRect(580, -9, 51, 41))
        self.FieldImage.setObjectName(_fromUtf8("FieldImage"))
        self.inputFieldImage = QtGui.QTextEdit(self.groupBox_2)
        self.inputFieldImage.setGeometry(QtCore.QRect(130, 0, 451, 31))
        self.inputFieldImage.setObjectName(_fromUtf8("inputFieldImage"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_7)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 150, 631, 31))
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label_4 = QtGui.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.PrecipitationImage = QtGui.QPushButton(self.groupBox_4)
        self.PrecipitationImage.setGeometry(QtCore.QRect(580, -9, 51, 41))
        self.PrecipitationImage.setObjectName(_fromUtf8("PrecipitationImage"))
        self.inputR = QtGui.QTextEdit(self.groupBox_4)
        self.inputR.setGeometry(QtCore.QRect(130, 0, 451, 31))
        self.inputR.setObjectName(_fromUtf8("inputR"))
        self.groupBox_6 = QtGui.QGroupBox(self.groupBox_7)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 230, 631, 31))
        self.groupBox_6.setTitle(_fromUtf8(""))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.label_6 = QtGui.QLabel(self.groupBox_6)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.ManagementImage = QtGui.QPushButton(self.groupBox_6)
        self.ManagementImage.setGeometry(QtCore.QRect(580, -9, 51, 41))
        self.ManagementImage.setObjectName(_fromUtf8("ManagementImage"))
        self.inputP = QtGui.QTextEdit(self.groupBox_6)
        self.inputP.setGeometry(QtCore.QRect(130, 0, 451, 31))
        self.inputP.setObjectName(_fromUtf8("inputP"))
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_7)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 190, 631, 31))
        self.groupBox_5.setTitle(_fromUtf8(""))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.label_5 = QtGui.QLabel(self.groupBox_5)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.LandCover = QtGui.QPushButton(self.groupBox_5)
        self.LandCover.setGeometry(QtCore.QRect(580, -9, 51, 41))
        self.LandCover.setObjectName(_fromUtf8("LandCover"))
        self.inputC = QtGui.QTextEdit(self.groupBox_5)
        self.inputC.setGeometry(QtCore.QRect(130, 0, 451, 31))
        self.inputC.setObjectName(_fromUtf8("inputC"))
        self.groupBox_8 = QtGui.QGroupBox(MatrixElaboratorDialogBase)
        self.groupBox_8.setGeometry(QtCore.QRect(20, 290, 621, 141))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.label_7 = QtGui.QLabel(self.groupBox_8)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 171, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.SlopeThreshold = QtGui.QDoubleSpinBox(self.groupBox_8)
        self.SlopeThreshold.setGeometry(QtCore.QRect(190, 20, 62, 31))
        self.SlopeThreshold.setObjectName(_fromUtf8("SlopeThreshold"))
        self.Flowacc = QtGui.QLabel(self.groupBox_8)
        self.Flowacc.setGeometry(QtCore.QRect(10, 70, 171, 21))
        self.Flowacc.setObjectName(_fromUtf8("Flowacc"))
        self.InputFlowacc = QtGui.QDoubleSpinBox(self.groupBox_8)
        self.InputFlowacc.setGeometry(QtCore.QRect(190, 60, 62, 31))
        self.InputFlowacc.setObjectName(_fromUtf8("InputFlowacc"))
        self.checkBox = QtGui.QCheckBox(self.groupBox_8)
        self.checkBox.setGeometry(QtCore.QRect(360, 110, 151, 31))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_3 = QtGui.QCheckBox(self.groupBox_8)
        self.checkBox_3.setGeometry(QtCore.QRect(60, 110, 191, 31))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.label_10 = QtGui.QLabel(self.groupBox_8)
        self.label_10.setGeometry(QtCore.QRect(300, 30, 181, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.AspectThreshold = QtGui.QDoubleSpinBox(self.groupBox_8)
        self.AspectThreshold.setGeometry(QtCore.QRect(490, 20, 62, 31))
        self.AspectThreshold.setObjectName(_fromUtf8("AspectThreshold"))
        self.label_11 = QtGui.QLabel(self.groupBox_8)
        self.label_11.setGeometry(QtCore.QRect(300, 70, 181, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.InputCellSize = QtGui.QDoubleSpinBox(self.groupBox_8)
        self.InputCellSize.setGeometry(QtCore.QRect(490, 60, 62, 31))
        self.InputCellSize.setObjectName(_fromUtf8("InputCellSize"))
        self.groupBox_9 = QtGui.QGroupBox(MatrixElaboratorDialogBase)
        self.groupBox_9.setGeometry(QtCore.QRect(20, 440, 631, 71))
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.label_12 = QtGui.QLabel(self.groupBox_9)
        self.label_12.setGeometry(QtCore.QRect(10, 40, 71, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.RasterPath = QtGui.QTextEdit(self.groupBox_9)
        self.RasterPath.setGeometry(QtCore.QRect(130, 30, 451, 31))
        self.RasterPath.setObjectName(_fromUtf8("RasterPath"))
        self.RasterPathButton = QtGui.QPushButton(self.groupBox_9)
        self.RasterPathButton.setGeometry(QtCore.QRect(580, 30, 51, 32))
        self.RasterPathButton.setObjectName(_fromUtf8("RasterPathButton"))
        self.groupBox_10 = QtGui.QGroupBox(MatrixElaboratorDialogBase)
        self.groupBox_10.setGeometry(QtCore.QRect(20, 520, 271, 61))
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.pushButton = QtGui.QPushButton(self.groupBox_10)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 110, 32))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_10)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 20, 110, 32))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(MatrixElaboratorDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")),
                               MatrixElaboratorDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")),
                               MatrixElaboratorDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(MatrixElaboratorDialogBase)

    def retranslateUi(self, MatrixElaboratorDialogBase):
        MatrixElaboratorDialogBase.setWindowTitle(
            _translate("MatrixElaboratorDialogBase", "Earh Matrix Elaborator", None))
        self.groupBox_7.setTitle(_translate("MatrixElaboratorDialogBase", "Input Raster", None))
        self.label.setText(_translate("MatrixElaboratorDialogBase", "DEM Image", None))
        self.DEM.setText(_translate("MatrixElaboratorDialogBase", "...", None))
        self.label_3.setText(_translate("MatrixElaboratorDialogBase", "Soil Image", None))
        self.SoilImage.setText(_translate("MatrixElaboratorDialogBase", "...", None))
        self.label_2.setText(_translate("MatrixElaboratorDialogBase", "Field image", None))
        self.FieldImage.setText(_translate("MatrixElaboratorDialogBase", "...", None))
        self.label_4.setText(_translate("MatrixElaboratorDialogBase", "Precipitation Image", None))
        self.PrecipitationImage.setText(_translate("MatrixElaboratorDialogBase", "...", None))
        self.label_6.setText(_translate("MatrixElaboratorDialogBase", "Management image", None))
        self.ManagementImage.setText(_translate("MatrixElaboratorDialogBase", "...", None))
        self.label_5.setText(_translate("MatrixElaboratorDialogBase", "Land-cover image", None))
        self.LandCover.setText(_translate("MatrixElaboratorDialogBase", "...", None))
        self.groupBox_8.setTitle(_translate("MatrixElaboratorDialogBase", "Control Specification", None))
        self.label_7.setText(_translate("MatrixElaboratorDialogBase", "Slope Threshold", None))
        self.Flowacc.setText(_translate("MatrixElaboratorDialogBase", "Maximum Slope Lenght", None))
        self.checkBox.setText(_translate("MatrixElaboratorDialogBase", "All in Metric System", None))
        self.checkBox_3.setText(_translate("MatrixElaboratorDialogBase", "Average soil factory patcher", None))
        self.label_10.setText(_translate("MatrixElaboratorDialogBase", "Aspect Threshold", None))
        self.label_11.setText(_translate("MatrixElaboratorDialogBase", "Cell Size", None))
        self.groupBox_9.setTitle(_translate("MatrixElaboratorDialogBase", "Output Raster", None))
        self.label_12.setText(_translate("MatrixElaboratorDialogBase", "Raster Path", None))
        self.RasterPathButton.setText(_translate("MatrixElaboratorDialogBase", "...", None))
        self.groupBox_10.setTitle(_translate("MatrixElaboratorDialogBase", "Config", None))
        self.pushButton.setText(_translate("MatrixElaboratorDialogBase", "Load", None))
        self.pushButton_2.setText(_translate("MatrixElaboratorDialogBase", "Save", None))

