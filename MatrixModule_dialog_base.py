# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MatrixModule_dialog_base.ui'
#
# Created: Thu Mar 12 16:49:05 2015
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
        MatrixElaboratorDialogBase.resize(401, 302)
        self.button_box = QtGui.QDialogButtonBox(MatrixElaboratorDialogBase)
        self.button_box.setGeometry(QtCore.QRect(30, 260, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.groupBox = QtGui.QGroupBox(MatrixElaboratorDialogBase)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 361, 31))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 10, 56, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.inputL1 = QtGui.QLineEdit(self.groupBox)
        self.inputL1.setGeometry(QtCore.QRect(80, 0, 281, 31))
        self.inputL1.setObjectName(_fromUtf8("inputL1"))
        self.groupBox_2 = QtGui.QGroupBox(MatrixElaboratorDialogBase)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 50, 361, 31))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 56, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.inputL2 = QtGui.QLineEdit(self.groupBox_2)
        self.inputL2.setGeometry(QtCore.QRect(80, 0, 281, 31))
        self.inputL2.setObjectName(_fromUtf8("inputL2"))
        self.groupBox_3 = QtGui.QGroupBox(MatrixElaboratorDialogBase)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 90, 361, 31))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 56, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.inputL3 = QtGui.QLineEdit(self.groupBox_3)
        self.inputL3.setGeometry(QtCore.QRect(80, 0, 281, 31))
        self.inputL3.setObjectName(_fromUtf8("inputL3"))
        self.groupBox_4 = QtGui.QGroupBox(MatrixElaboratorDialogBase)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 130, 361, 31))
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label_4 = QtGui.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 56, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.inputL4 = QtGui.QLineEdit(self.groupBox_4)
        self.inputL4.setGeometry(QtCore.QRect(80, 0, 281, 31))
        self.inputL4.setObjectName(_fromUtf8("inputL4"))
        self.groupBox_5 = QtGui.QGroupBox(MatrixElaboratorDialogBase)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 170, 361, 31))
        self.groupBox_5.setTitle(_fromUtf8(""))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.label_5 = QtGui.QLabel(self.groupBox_5)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 56, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.inputL5 = QtGui.QLineEdit(self.groupBox_5)
        self.inputL5.setGeometry(QtCore.QRect(80, 0, 281, 31))
        self.inputL5.setObjectName(_fromUtf8("inputL5"))
        self.groupBox_6 = QtGui.QGroupBox(MatrixElaboratorDialogBase)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 210, 361, 31))
        self.groupBox_6.setTitle(_fromUtf8(""))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.label_6 = QtGui.QLabel(self.groupBox_6)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 56, 13))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.inputL6 = QtGui.QLineEdit(self.groupBox_6)
        self.inputL6.setGeometry(QtCore.QRect(80, 0, 281, 31))
        self.inputL6.setObjectName(_fromUtf8("inputL6"))

        self.retranslateUi(MatrixElaboratorDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), MatrixElaboratorDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), MatrixElaboratorDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(MatrixElaboratorDialogBase)

    def retranslateUi(self, MatrixElaboratorDialogBase):
        MatrixElaboratorDialogBase.setWindowTitle(_translate("MatrixElaboratorDialogBase", "Earh Matrix Elaborator", None))
        self.label.setText(_translate("MatrixElaboratorDialogBase", "Raste 1", None))
        self.label_2.setText(_translate("MatrixElaboratorDialogBase", "Raster 2", None))
        self.label_3.setText(_translate("MatrixElaboratorDialogBase", "Raster 3", None))
        self.label_4.setText(_translate("MatrixElaboratorDialogBase", "Raster 4", None))
        self.label_5.setText(_translate("MatrixElaboratorDialogBase", "Raster 5", None))
        self.label_6.setText(_translate("MatrixElaboratorDialogBase", "Raster 6", None))

