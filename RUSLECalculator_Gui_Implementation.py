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
from PyQt4.QtCore import QObject
from PyQt4.QtGui import QFileDialog, QMessageBox
from RUSLECalculator_config import CONFIG_OBJECT
from RUSLECalculator_lib import open_raster, input_open, calc_r, rastermath
from RUSLECalculator_resurce import CONFIG_CONFIG

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
    outputFile = Utils.FileDialog.getSaveFileName(dlg, dlg.tr("Select the raster file to save the results to"),
                                                  Utils.FileFilter.allRastersFilter(), lastUsedFilter)
    if outputFile == "":
        raise ValueError("Void string")
    return outputFile


def outputfunction(dlg):
    filename = get_raster_name(dlg)
    dlg.RasterPath.setText(filename)


def run(dlg):
    CONFIG_OBJECT.edit_config(CONFIG_CONFIG, 'Config_path', dlg.RasterPath.toPlainText())
    outputfile = dlg.RasterPath.toPlainText()
    runhelper(dlg)
    open_raster(outputfile)
    print("Ended")


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

    ds = {}

    ds['k'] = input_open(k)

    print(ds['k'])

    rastersize = ds['k'][0].shape

    try:
        ds['r'] = input_open(r)
    except Exception:
        ds['r'] = calc_r()

    try:
        ds['ls'] = input_open(ls)
    except Exception:
        # ds['ls'] = calc_ls(flowacc, cell_size, pend)
        raise NotImplemented

    try:
        ds['c'] = input_open(c)
    except:
        raise NotImplemented

    try:
        ds['p'] = input_open(p)
    except Exception:
        ds['p'] = None

    try:
        ds['out'] = input_open(outputfile)
    except:
        error_window(dlg, "Error", "You need to specify an output file")

    ds['fieldimage'] = fieldimage

    rastermath(ds['k'][0], ds['r'][0], ds['ls'][0], ds['c'][0], ds['p'][0], rastersize[0], rastersize[1], datatype)


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

    def clickloadconfig(self):
        openconfig()

    def clicksaveconfig(self):
        saveconfig(self.dlg)


# TODO cambiare le configurazioni
def saveconfig(dlg):
    string_path = get_raster_name(dlg)
    CONFIG_OBJECT.edit_config(CONFIG_CONFIG, 'config_path', string_path)
    CONFIG_OBJECT.edit_config(CONFIG_CONFIG, 'aspect_threshold', dlg.AspectThreshold.value())
    CONFIG_OBJECT.edit_config(CONFIG_CONFIG, 'maximum_slope_lenght', dlg.MaxSlopeLenght.value())
    CONFIG_OBJECT.edit_config(CONFIG_CONFIG, 'maximum_slope_metric', dlg.checkBox.value())
    CONFIG_OBJECT.edit_config(CONFIG_CONFIG, 'average_soil_factory_patcher', dlg.checkBox_3.value())
    CONFIG_OBJECT.edit_config(CONFIG_CONFIG, 'slope_threhold', dlg.SlopeThreshold.value())
    CONFIG_OBJECT.edit_config(CONFIG_CONFIG, 'smallest_patch_size', dlg.SmallestPatchSize.value())
    CONFIG_OBJECT.save()


def error_window(dlg, title, body):
    QMessageBox.information(dlg, dlg.tr(title), dlg.tr(body), "")
