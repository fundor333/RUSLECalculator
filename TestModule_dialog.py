# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TestClassDialog
                                 A QGIS plugin
 Descrizione generica
                             -------------------
        begin                : 2015-02-17
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Matteo Scarpa
        email                : matteoscarpa92@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import QtGui, uic
from PyQt4.QtCore import QObject, SIGNAL
from PyQt4.uic.properties import QtCore
from TestModule_dialog_base import _fromUtf8

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'TestModule_dialog_base.ui'))


class TestClassDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(TestClassDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), SilvestriClassDialogBase.accept)
        self.setupUi(self)

    # TODO Inserire esecuzione bottone
    def chooseLayer(self):
        layerlist = []     # crea una lista vuota
        self.ui.layerComboBox.clear()     # svuota la lista del combo box
        layerlist = self.getLayerNames()     # a layerlist assegna il risultato della procedura getLayerNames()
        self.ui.layerComboBox.addItems(layerlist)     # aggiunge layerlist al combo box
        return