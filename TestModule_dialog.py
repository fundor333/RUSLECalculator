# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestModule_dialog.ui'
#
# Created: Wed Mar 11 08:20:03 2015
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

# Import the code for the dialog
import os.path
from PyQt4 import QtGui, uic

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'TestModule_dialog.ui'))


class Ui_TestModule(object):
    def setupUi(self, TestModule):
        TestModule.setObjectName(_fromUtf8("TestModule"))
        TestModule.resize(361, 360)
        TestModule.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_box = QtGui.QDialogButtonBox(TestModule)
        self.button_box.setGeometry(QtCore.QRect(90, 320, 181, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.groupBox = QtGui.QGroupBox(TestModule)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 321, 51))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 56, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.inputL1 = QtGui.QLineEdit(self.groupBox)
        self.inputL1.setGeometry(QtCore.QRect(80, 20, 231, 21))
        self.inputL1.setObjectName(_fromUtf8("inputL1"))
        self.groupBox_2 = QtGui.QGroupBox(TestModule)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 60, 321, 51))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 56, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.inputL2 = QtGui.QLineEdit(self.groupBox_2)
        self.inputL2.setGeometry(QtCore.QRect(82, 20, 231, 21))
        self.inputL2.setObjectName(_fromUtf8("inputL2"))
        self.groupBox_3 = QtGui.QGroupBox(TestModule)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 110, 321, 51))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 56, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.inputL3 = QtGui.QLineEdit(self.groupBox_3)
        self.inputL3.setGeometry(QtCore.QRect(80, 20, 231, 21))
        self.inputL3.setObjectName(_fromUtf8("inputL3"))
        self.groupBox_4 = QtGui.QGroupBox(TestModule)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 160, 321, 51))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label_4 = QtGui.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 56, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.inputL4 = QtGui.QLineEdit(self.groupBox_4)
        self.inputL4.setGeometry(QtCore.QRect(82, 20, 231, 21))
        self.inputL4.setObjectName(_fromUtf8("inputL4"))
        self.groupBox_5 = QtGui.QGroupBox(TestModule)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 210, 321, 51))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.label_5 = QtGui.QLabel(self.groupBox_5)
        self.label_5.setGeometry(QtCore.QRect(20, 30, 56, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.inputL5 = QtGui.QLineEdit(self.groupBox_5)
        self.inputL5.setGeometry(QtCore.QRect(80, 20, 231, 21))
        self.inputL5.setObjectName(_fromUtf8("inputL5"))
        self.groupBox_6 = QtGui.QGroupBox(TestModule)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 260, 321, 51))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.label_6 = QtGui.QLabel(self.groupBox_6)
        self.label_6.setGeometry(QtCore.QRect(20, 30, 56, 13))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.inputL6 = QtGui.QLineEdit(self.groupBox_6)
        self.inputL6.setGeometry(QtCore.QRect(80, 20, 231, 21))
        self.inputL6.setObjectName(_fromUtf8("inputL6"))

        self.retranslateUi(TestModule)
        QtCore.QMetaObject.connectSlotsByName(TestModule)

    def retranslateUi(self, TestModule):
        TestModule.setWindowTitle(_translate("TestModule", "TestModule", None))
        self.groupBox.setTitle(_translate("TestModule", "Raster 1", None))
        self.label.setText(_translate("TestModule", "Raster", None))
        self.groupBox_2.setTitle(_translate("TestModule", "Raster 2", None))
        self.label_2.setText(_translate("TestModule", "Raster", None))
        self.groupBox_3.setTitle(_translate("TestModule", "Raster 3", None))
        self.label_3.setText(_translate("TestModule", "Raster", None))
        self.groupBox_4.setTitle(_translate("TestModule", "Raster 4", None))
        self.label_4.setText(_translate("TestModule", "Raster", None))
        self.groupBox_5.setTitle(_translate("TestModule", "Raster 5", None))
        self.label_5.setText(_translate("TestModule", "Raster", None))
        self.groupBox_6.setTitle(_translate("TestModule", "Raster 6", None))
        self.label_6.setText(_translate("TestModule", "Raster", None))


class TestClassDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(TestClassDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)