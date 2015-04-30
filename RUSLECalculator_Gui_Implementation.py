from RUSLECalculator_Math import rastermath
from RUSLECalculator_lib import open_raster, CONFIG_OBJECT, name_opener
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


def openconfig(dlg):
    CONFIG_OBJECT.open(QFileDialog.getOpenFileName())


def get_raster_name(dlg):
    lastUsedFilter = Utils.FileFilter.lastUsedRasterFilter()
    outputFile = Utils.FileDialog.getSaveFileName(dlg, dlg.tr("Select the raster file to save the results to"),
                                                  Utils.FileFilter.allRastersFilter(), lastUsedFilter)
    if outputFile == "":
        raise ValueError("Void string")
    return outputFile


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
    p = makep(dlg.inputP.data())

    ds = range(0, 6)
    band = range(0, 6)
    data = {}

    ds[k] = name_opener(k)
    ds[r] = name_opener(r)
    ds[ls] = name_opener(ls)
    ds[c] = name_opener(c)

    k.RasterXSize, k.RasterYSize, 1, k.GetRasterBand(1).DataType
    rastermath()

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
        openconfig(self.dlg)

    def clickedsaveconfig(self):
        saveconfig(self.dlg)
