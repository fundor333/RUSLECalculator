# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestModule_dialog_base.ui'
#
# Created: Tue Mar  3 10:02:39 2015
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_SilvestriClassDialogBase(object):
    def setupUi(self, SilvestriClassDialogBase):
        SilvestriClassDialogBase.setObjectName(_fromUtf8("SilvestriClassDialogBase"))
        SilvestriClassDialogBase.resize(364, 405)
        SilvestriClassDialogBase.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_box = QtGui.QDialogButtonBox(SilvestriClassDialogBase)
        self.button_box.setGeometry(QtCore.QRect(90, 360, 181, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.groupBox = QtGui.QGroupBox(SilvestriClassDialogBase)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 321, 51))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 56, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.selectr1 = QtGui.QComboBox(self.groupBox)
        self.selectr1.setGeometry(QtCore.QRect(70, 20, 241, 26))
        self.selectr1.setObjectName(_fromUtf8("selectr1"))
        self.groupBox_2 = QtGui.QGroupBox(SilvestriClassDialogBase)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 60, 321, 51))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 56, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.selectr2 = QtGui.QComboBox(self.groupBox_2)
        self.selectr2.setGeometry(QtCore.QRect(70, 20, 241, 26))
        self.selectr2.setObjectName(_fromUtf8("selectr2"))
        self.groupBox_3 = QtGui.QGroupBox(SilvestriClassDialogBase)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 110, 321, 51))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 56, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.selectr3 = QtGui.QComboBox(self.groupBox_3)
        self.selectr3.setGeometry(QtCore.QRect(70, 20, 241, 26))
        self.selectr3.setObjectName(_fromUtf8("selectr3"))
        self.groupBox_4 = QtGui.QGroupBox(SilvestriClassDialogBase)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 160, 321, 51))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label_4 = QtGui.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 56, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.selectr4 = QtGui.QComboBox(self.groupBox_4)
        self.selectr4.setGeometry(QtCore.QRect(70, 20, 241, 26))
        self.selectr4.setObjectName(_fromUtf8("selectr4"))
        self.groupBox_5 = QtGui.QGroupBox(SilvestriClassDialogBase)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 210, 321, 51))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.label_5 = QtGui.QLabel(self.groupBox_5)
        self.label_5.setGeometry(QtCore.QRect(20, 30, 56, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.selectr5 = QtGui.QComboBox(self.groupBox_5)
        self.selectr5.setGeometry(QtCore.QRect(70, 20, 241, 26))
        self.selectr5.setObjectName(_fromUtf8("selectr5"))
        self.groupBox_6 = QtGui.QGroupBox(SilvestriClassDialogBase)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 260, 321, 51))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.label_6 = QtGui.QLabel(self.groupBox_6)
        self.label_6.setGeometry(QtCore.QRect(20, 30, 56, 13))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.selectr6 = QtGui.QComboBox(self.groupBox_6)
        self.selectr6.setGeometry(QtCore.QRect(70, 20, 241, 26))
        self.selectr6.setObjectName(_fromUtf8("selectr6"))
        self.checker = QtGui.QPushButton(SilvestriClassDialogBase)
        self.checker.setGeometry(QtCore.QRect(130, 320, 110, 32))
        self.checker.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checker.setObjectName(_fromUtf8("checker"))

        self.retranslateUi(SilvestriClassDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), SilvestriClassDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), SilvestriClassDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(SilvestriClassDialogBase)

    def retranslateUi(self, SilvestriClassDialogBase):
        SilvestriClassDialogBase.setWindowTitle(_translate("SilvestriClassDialogBase", "Silvestri", None))
        self.groupBox.setTitle(_translate("SilvestriClassDialogBase", "Raster 1", None))
        self.label.setText(_translate("SilvestriClassDialogBase", "Raster", None))
        self.groupBox_2.setTitle(_translate("SilvestriClassDialogBase", "Raster 2", None))
        self.label_2.setText(_translate("SilvestriClassDialogBase", "Raster", None))
        self.groupBox_3.setTitle(_translate("SilvestriClassDialogBase", "Raster 3", None))
        self.label_3.setText(_translate("SilvestriClassDialogBase", "Raster", None))
        self.groupBox_4.setTitle(_translate("SilvestriClassDialogBase", "Raster 4", None))
        self.label_4.setText(_translate("SilvestriClassDialogBase", "Raster", None))
        self.groupBox_5.setTitle(_translate("SilvestriClassDialogBase", "Raster 5", None))
        self.label_5.setText(_translate("SilvestriClassDialogBase", "Raster", None))
        self.groupBox_6.setTitle(_translate("SilvestriClassDialogBase", "Raster 6", None))
        self.label_6.setText(_translate("SilvestriClassDialogBase", "Raster", None))
        self.checker.setToolTip(_translate("SilvestriClassDialogBase", "<html><head/><body><p>Check if rasters are corret</p></body></html>", None))
        self.checker.setText(_translate("SilvestriClassDialogBase", "Check", None))

