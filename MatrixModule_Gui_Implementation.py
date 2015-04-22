from os.path import expanduser
from MatrixModule_Math import sumsixraster
from MatrixModule_lib import open_raster, CONFIG_OBJECT
from MatrixModule_resurce import CONFIG_CONFIG

try:
    from osgeo import *
except:
    import gdal
    import ogr
    import osr

from PyQt4.QtCore import QObject
from PyQt4.QtGui import QFileDialog


def selectFile(lineEdit):
    lineEdit.setText(QFileDialog.getOpenFileName())


def openconfig():
    CONFIG_OBJECT.open(QFileDialog.getOpenFileName())


def settingoutput(dlg):
    filename = QFileDialog.getOpenFileName(dlg, 'Save File', expanduser("~"), 'All (*.*)')
    if filename:
        dlg.RasterPath.setText(filename)


def run(dlg):
    try:
        outputfile = CONFIG_OBJECT.edit_config(CONFIG_CONFIG, 'Config_path', dlg.RasterPath.toPlainText())
        array = []
        array.append(dlg.inputDEM.toPlainText())
        array.append(dlg.inputSoilImage.toPlainText())
        array.append(dlg.inputFieldImage.toPlainText())
        array.append(dlg.inputPrecipitationImage.toPlainText())
        array.append(dlg.inputManagementImage.toPlainText())
        array.append(dlg.inputLandCover.toPlainText())
        sumsixraster(array[0], array[1], array[2], array[3], array[4], array[5], outputfile)
        open_raster(outputfile)
        print("Ended")
    except:
        raise NotImplemented


class ButtonSignal(QObject):
    def __init__(self, dlg):
        QObject.__init__(self)
        self.dlg = dlg

    def clickedme1(self):
        selectFile(self.dlg.inputDEM)

    def clickedme2(self):
        selectFile(self.dlg.inputSoilImage)

    def clickedme3(self):
        selectFile(self.dlg.inputFieldImage)

    def clickedme4(self):
        selectFile(self.dlg.inputPrecipitationImage)

    def clickedme5(self):
        selectFile(self.dlg.inputManagementImage)

    def clickedme6(self):
        selectFile(self.dlg.inputLandCover)

    def clickedoutput(self):
        settingoutput(self.dlg)

    def clickedloadconfig(self):
        raise NotImplemented

    def clickedsaveconfig(self):
        raise NotImplemented