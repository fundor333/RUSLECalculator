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
from PyQt4.uic.properties import QtCore

from PyQt4.QtCore import QObject
from PyQt4.QtGui import QFileDialog, QMessageBox

from RUSLECalculator_lib import real_math
import GdalTools_utils as Utils

try:
    from osgeo import *
except:
    import gdal
    import ogr
    import osr


def selectfile(lineEdit):
    lineEdit.setText(QFileDialog.getOpenFileName())


def get_raster_name(dlg):
    lastUsedFilter = Utils.FileFilter.lastUsedRasterFilter()
    fileDialog = Utils.FileDialog
    outputFile = fileDialog.getSaveFileName(dlg, dlg.tr("Select the raster file to save the results to"),
                                            Utils.FileFilter.allRastersFilter(), lastUsedFilter)
    Utils.FileFilter.setLastUsedRasterFilter(lastUsedFilter)

    # required either -ts or -tr to create the output file
    if not QtCore.QFileInfo(outputFile).exists():
        QMessageBox.information(dlg, dlg.tr("Output size required"),
                                dlg.tr("The output file doesn't exist. You must set up the output size to create it."))
    return outputFile


def outputfunction(dlg):
    filename = get_raster_name(dlg)
    dlg.RasterPath.setText(filename)


def run(dlg):
    dem = dlg.inputDEM.toPlainText()
    fieldimage = dlg.inputFieldImage.toPlainText()
    datatype = Utils.FileFilter.lastUsedRasterFilter()


    k = dlg.inputK.toPlainText()
    r = dlg.inputR.toPlainText()
    ls = dlg.inputLS.toPlainText()
    c = dlg.inputC.toPlainText()
    p = dlg.inputP.toPlainText()
    outputfile = dlg.RasterPath.toPlainText()

    real_math(k, r, ls, c, p, outputfile)


class ButtonSignal(QObject):
    def __init__(self, dlg):
        QObject.__init__(self)
        self.dlg = dlg

    def clickdem(self):
        selectfile(self.dlg.inputDEM)

    def clickk(self):
        selectfile(self.dlg.inputK)

    def clickfieldimage(self):
        selectfile(self.dlg.imputImageField)

    def clickr(self):
        selectfile(self.dlg.inputR)

    def clickp(self):
        selectfile(self.dlg.inputP)

    def clickls(self):
        selectfile(self.dlg.inputLS)

    def clickc(self):
        selectfile(self.dlg.inputC)

    def clickoutput(self):
        outputfunction(self.dlg)