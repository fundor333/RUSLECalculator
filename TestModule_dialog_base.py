# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestModule_dialog_base.ui'
#
# Created: Thu Feb 26 10:49:05 2015
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
        SilvestriClassDialogBase.resize(337, 174)
        self.button_box = QtGui.QDialogButtonBox(SilvestriClassDialogBase)
        self.button_box.setGeometry(QtCore.QRect(60, 110, 181, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.HighLabel = QtGui.QLabel(SilvestriClassDialogBase)
        self.HighLabel.setGeometry(QtCore.QRect(50, 30, 111, 16))
        self.HighLabel.setObjectName(_fromUtf8("HighLabel"))
        self.WidthLabel = QtGui.QLabel(SilvestriClassDialogBase)
        self.WidthLabel.setGeometry(QtCore.QRect(50, 70, 111, 16))
        self.WidthLabel.setObjectName(_fromUtf8("WidthLabel"))
        self.highInput = QtGui.QSpinBox(SilvestriClassDialogBase)
        self.highInput.setGeometry(QtCore.QRect(220, 20, 53, 25))
        self.highInput.setObjectName(_fromUtf8("highInput"))
        self.widthInput = QtGui.QSpinBox(SilvestriClassDialogBase)
        self.widthInput.setGeometry(QtCore.QRect(220, 60, 53, 25))
        self.widthInput.setObjectName(_fromUtf8("widthInput"))

        self.retranslateUi(SilvestriClassDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), SilvestriClassDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), SilvestriClassDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(SilvestriClassDialogBase)

    def retranslateUi(self, SilvestriClassDialogBase):
        SilvestriClassDialogBase.setWindowTitle(_translate("SilvestriClassDialogBase", "Silvestri", None))
        self.HighLabel.setText(_translate("SilvestriClassDialogBase", "Altezza", None))
        self.WidthLabel.setText(_translate("SilvestriClassDialogBase", "Larghezza", None))

