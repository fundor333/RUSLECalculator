# -*- coding: utf-8 -*-
"""
/***************************************************************************
 RUSLECalculator
                                 A QGIS plugin
 Plugin
                             -------------------
        begin                : 2015-03-12
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
import resources_rc
import RUSLECalculator_dialog
import os.path

from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import QAction, QIcon
from RUSLECalculator_Gui_Implementation import run, ButtonSignal
from RUSLECalculator_dialog import RUSLECalculatorDialog


class RUSLECalculator():
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(self.plugin_dir, 'i18n', 'RUSLECalculator_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = RUSLECalculatorDialog()

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr('&RUSLE Calculator')

        self.toolbar = self.iface.addToolBar('RUSLECalculator')
        self.toolbar.setObjectName('RUSLECalculator')

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('RUSLECalculator', message)

    def add_action(
            self,
            icon_path,
            text,
            callback,
            enabled_flag=True,
            add_to_menu=True,
            add_to_toolbar=True,
            status_tip=None,
            whats_this=None,
            parent=None):
        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""
        icon_path = ':/plugins/RUSLECalculator/icon.png'
        self.add_action(icon_path, text=self.tr('Elaborate'), callback=self.run, parent=self.iface.mainWindow())


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(self.tr('&RUSLE Calculator'), action)
            self.iface.removeToolBarIcon(action)


    def run(self):
        """Run method that performs all the real work"""
        # show the dialog
        self.dlg.show()

        bott = ButtonSignal(self.dlg)

        self.dlg.buttonDem.clicked.connect(bott.clickdem)
        self.dlg.SoilImage.clicked.connect(bott.clickk)
        self.dlg.FieldImage.clicked.connect(bott.clickfieldimage)
        self.dlg.PrecipitationImage.clicked.connect(bott.clickr)
        self.dlg.ManagementImage.clicked.connect(bott.clickp)
        self.dlg.LandCover.clicked.connect(bott.clickc)
        self.dlg.RasterPathButton.clicked.connect(bott.clickoutput)
        self.dlg.pushButton.clicked.connect(bott.clickloadconfig)
        self.dlg.pushButton_2.clicked.connect(bott.clicksaveconfig)


        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            run(self.dlg)
