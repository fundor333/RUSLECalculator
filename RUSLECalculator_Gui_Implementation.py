from RUSLECalculator_config import saveconfig, CONFIG_OBJECT
from RUSLECalculator_lib import open_raster, input_open, calc_r, rastermath
from RUSLECalculator_resurce import CONFIG_CONFIG

import GdalTools_utils as Utils

try:
    from osgeo import *
except:
    import gdal
    import ogr
    import osr

from PyQt4.QtCore import QObject
from PyQt4.QtGui import QFileDialog


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


    ds = range(0, 6)
    rastersize = k.RasterXSize, k.RasterYSize
    datatype = k.GetRasterBand(1).DataType

    ds['k'] = input_open(k)

    try:
        ds['r'] = input_open(r)
    except Exception:
        ds['r'] = calc_r(input_open(dem))

    try:
        ds['ls'] = input_open(ls)
    except Exception:
        # ds['ls'] = calc_ls(flowacc, cell_size, pend)
        raise NotImplemented

    ds['c'] = input_open(c)

    try:
        ds['p'] = input_open(p)
    except Exception:
        ds['p'] = None

    ds['fieldimage'] = fieldimage

    rastermath(ds['k'][0], ds['r'][0], ds['ls'][0], ds['c'][0], ds['p'][0], rastersize[0], rastersize[1], datatype)

class ButtonSignal(QObject):
    def __init__(self, dlg):
        QObject.__init__(self)
        self.dlg = dlg

    def clickedme1(self):
        selectfile(self.dlg.inputDEM)

    def clickedme2(self):
        selectfile(self.dlg.inputK)

    def clickedme3(self):
        selectfile(self.dlg.inputFieldImage)

    def clickedme4(self):
        selectfile(self.dlg.inputR)

    def clickedme5(self):
        selectfile(self.dlg.inputP)

    def clickedme6(self):
        selectfile(self.dlg.inputC)

    def clickedoutput(self):
        outputfunction(self.dlg)

    def clickedloadconfig(self):
        openconfig()

    def clickedsaveconfig(self):
        saveconfig(self.dlg)
