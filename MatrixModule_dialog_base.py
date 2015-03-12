# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MatrixModule_dialog_base.ui'
#
# Created: Thu Mar 12 13:46:16 2015
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

class Ui_MatrixElaboratorDialogBase(object):
    def setupUi(self, MatrixElaboratorDialogBase):
        MatrixElaboratorDialogBase.setObjectName(_fromUtf8("MatrixElaboratorDialogBase"))
        MatrixElaboratorDialogBase.resize(400, 300)
        self.button_box = QtGui.QDialogButtonBox(MatrixElaboratorDialogBase)
        self.button_box.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))

        self.retranslateUi(MatrixElaboratorDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), MatrixElaboratorDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), MatrixElaboratorDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(MatrixElaboratorDialogBase)

    def retranslateUi(self, MatrixElaboratorDialogBase):
        MatrixElaboratorDialogBase.setWindowTitle(_translate("MatrixElaboratorDialogBase", "Earh Matrix Elaborator", None))

