"""
/***************************************************************************
 RUSLECalculator_Gui_Implementation
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
import os
from PyQt4.QtCore import QObject
from PyQt4.QtGui import QFileDialog
from PyQt4.uic.properties import QtCore
import GdalTools_utils as Utils
from RUSLECalculator_lib import get_soil_loss
from RUSLECalculator_resurce import RASTER_DRIVER

try:
    from osgeo import *
except Exception:
    import gdal
    import ogr
    import osr


def selectfile(lineEdit):
    lineEdit.setText(QFileDialog.getOpenFileName())


def selectdirectory(lineEdit):
    lineEdit.setText(QFileDialog.getExistingDirectory())


def get_raster_name(dlg):
    lastUsedFilter = Utils.FileFilter.lastUsedRasterFilter()
    fileDialog = Utils.FileDialog
    name_list = RASTER_DRIVER.keys()
    name_list.sort()
    string_to_dialog = ""
    for s in name_list:
        string_to_dialog += s + ";;"

    string_to_dialog = unicode(string_to_dialog[:-2], 'utf-8')
    outputFile = fileDialog.getSaveFileName(dlg, dlg.tr("Select the raster file to save the results to"),
                                            string_to_dialog, lastUsedFilter)
    Utils.FileFilter.setLastUsedRasterFilter(lastUsedFilter)

    if not QtCore.QFileInfo(outputFile).exists():
        file = open(outputFile, 'r+')  # Trying to create a new file or open one
        file.close()
    return outputFile


def outputfunction(dlg):
    filename = get_raster_name(dlg)
    dlg.RasterPath.setText(filename)


def getlistfile(checker_boolean, input_position, years):
    list_out = []
    if checker_boolean:
        for _ in range(0, years):
            list_out.append(input_position)
    else:
        dir_root = os.listdir(input_position)
        dir_root.sort()
        for file_name in dir_root:
            list_out.append(file_name)

        list_out.sort()
    return list_out


def run(dlg):
    dem = dlg.inputDEM.toPlainText()
    datatype = RASTER_DRIVER[str(Utils.FileFilter.lastUsedRasterFilter()[0])]

    k = dlg.checkerK.isChecked(), dlg.inputK.toPlainText()
    r = dlg.checkerR.isChecked(), dlg.inputR.toPlainText()
    ls = dlg.checkerLS.isChecked(), dlg.inputLS.toPlainText()
    c = dlg.checkerC.isChecked(), dlg.inputC.toPlainText()
    p = dlg.checkerP.isChecked(), dlg.inputP.toPlainText()
    outputfile = dlg.RasterPath.toPlainText()
    years = dlg.years_input.value()

    get_soil_loss(k, r, ls, c, p, dem, outputfile, datatype, years)


class ButtonSignal(QObject):
    def __init__(self, dlg):
        QObject.__init__(self)
        self.dlg = dlg

    def clickdem(self):
        if self.dlg.checkerDEM.isChecked():
            selectfile(self.dlg.inputDEM)
        else:
            selectdirectory(self.dlg.inputDEM)

    def clickk(self):
        if self.dlg.checkerK.isChecked():
            selectfile(self.dlg.inputK)
        else:
            selectdirectory(self.dlg.inputK)

    def clickr(self):
        if self.dlg.checkerR.isChecked():
            selectfile(self.dlg.inputR)
        else:
            selectdirectory(self.dlg.inputR)

    def clickp(self):
        if self.dlg.checkerP.isChecked():
            selectfile(self.dlg.inputP)
        else:
            selectdirectory(self.dlg.inputP)

    def clickls(self):
        if self.dlg.checkerLS.isChecked():
            selectfile(self.dlg.inputLS)
        else:
            selectdirectory(self.dlg.inputLS)

    def clickc(self):
        if self.dlg.checkerC.isChecked():
            selectfile(self.dlg.inputC)
        else:
            selectdirectory(self.dlg.inputC)

    def clickoutput(self):
        outputfunction(self.dlg)
