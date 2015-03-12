# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestModule_gui.ui'
#
# Created: Thu Mar 12 10:06:36 2015
#      by: PyQt4 UI code generator 4.10.4
# Import the code for the dialog
import os.path
from PyQt4 import QtGui, uic

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'TestModule_dialog.ui'))


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
