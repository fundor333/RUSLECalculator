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
from PyQt4.uic.uiparser import QtCore

from PyQt4.QtCore import QObject
from PyQt4.QtGui import QFileDialog, QMessageBox

from RUSLECalculator_config import CONFIG_OBJECT, CONFIG_CONFIGURATION
from RUSLECalculator_lib import open_raster, input_open, rastermath, output_open, test_math
from RUSLECalculator_error import RError, LSError, CError, LOG
import GdalTools_utils as Utils

try:
    from osgeo import *
except:
    import gdal
    import ogr
    import osr


def selectfile(lineEdit):
    lineEdit.setText(QFileDialog.getOpenFileName())


def openconfig():
    CONFIG_OBJECT.open(QFileDialog.getOpenFileName())


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
    CONFIG_OBJECT.edit_config(CONFIG_CONFIGURATION, 'Config_path', dlg.RasterPath.toPlainText())
    outputfile = dlg.RasterPath.toPlainText()
    runhelper(dlg)
    open_raster(outputfile)
    LOG.i("Ended")


def runhelper(dlg):
    dem = dlg.inputDEM.toPlainText()
    fieldimage = dlg.inputFieldImage.toPlainText()
    k = dlg.inputK.toPlainText()
    r = dlg.inputR.toPlainText()
    ls = dlg.inputLS.toPlainText()
    c = dlg.inputC.toPlainText()
    p = dlg.inputP.toPlainText()
    outputfile = dlg.RasterPath.toPlainText()
    datatype = Utils.FileFilter.lastUsedRasterFilter()

    test_math(dem, fieldimage, k, r, ls, c, p, outputfile, datatype)

    if datatype[0] == "":
        datatype = gdal.GDT_CFloat64

    ds = {'k': input_open(k), 'dem': dem}

    LOG.i(ds['k'])

    rastersize = ds['k'][0].shape

    try:
        ds['r'] = input_open(r)
        LOG.i("r " + str(ds['r']))
    except Exception:
        raise RError

    try:
        ds['ls'] = input_open(ls)
        LOG.i("ls " + str(ds['ls']))
    except Exception:
        raise LSError

    try:
        ds['c'] = input_open(c)
        LOG.i("c " + str(ds['c']))
    except:
        raise CError

    try:
        ds['p'] = input_open(p)
        LOG.i("p " + str(ds['p']))
    except Exception:
        ds['p'] = None

    try:
        ds['out'] = output_open(outputfile)
        LOG.i("out  " + str(ds['out']))
    except Exception:
        LOG.e("You need to specify an output file", dlg)

    ds['fieldimage'] = fieldimage

    rastermath(ds['k'], ds['r'], ds['ls'], ds['c'], ds['p'], ds['out'], rastersize[0], rastersize[1], datatype)


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


# TODO cambiare le configurazioni
def saveconfig(dlg):
    string_path = get_raster_name(dlg)
    CONFIG_OBJECT.edit_config(CONFIG_CONFIGURATION, 'config_path', string_path)
    CONFIG_OBJECT.edit_config(CONFIG_CONFIGURATION, 'aspect_threshold', dlg.AspectThreshold.value())
    CONFIG_OBJECT.edit_config(CONFIG_CONFIGURATION, 'maximum_slope_lenght', dlg.MaxSlopeLenght.value())
    CONFIG_OBJECT.edit_config(CONFIG_CONFIGURATION, 'maximum_slope_metric', dlg.checkBox.value())
    CONFIG_OBJECT.edit_config(CONFIG_CONFIGURATION, 'average_soil_factory_patcher', dlg.checkBox_3.value())
    CONFIG_OBJECT.edit_config(CONFIG_CONFIGURATION, 'slope_threhold', dlg.SlopeThreshold.value())
    CONFIG_OBJECT.edit_config(CONFIG_CONFIGURATION, 'smallest_patch_size', dlg.SmallestPatchSize.value())
    CONFIG_OBJECT.save()