from PyQt4.uic.properties import QtGui
from MatrixModule_Math import sumsixraster
from MatrixModule_lib import open_raster

from MatrixModule_resurce import FILEPATH, OUTPUT_FORMAT, CONFIG_CONFIG, CONFIG_OBJECT


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


def selectconfig(config):
    filename = QtGui.QFileDialog.getOpenFileName('Open File', '', 'Images (*.png *.xpm *.jpg)',
        None, QtGui.QFileDialog.DontUseNativeDialog)
    CONFIG_OBJECT.edit_config(CONFIG_CONFIG, 'Config_path', filename)


def init(dlg):
    dlg.DEM.clicked.connect(selectFile(dlg.inputDEM))
    dlg.SoilImage.clicked.connect(selectFile(dlg.inputSoilImage))
    dlg.FieldImage.clicked.connect(selectFile(dlg.inputFieldImage))
    dlg.PrecipitationImage.clicked.connect(selectFile(dlg.inputPrecipitationImage))
    dlg.ManagementImage.clicked.connect(selectFile(dlg.inputManagementImage))
    dlg.LandCover.clicked.connect(selectFile(dlg.inputLandCover))
    dlg.RasterPathButton.clicked.connect(selectconfig(dlg))


def run(dlg):
    array = []
    array.append(dlg.inputDEM.toPlainText())
    array.append(dlg.inputSoilImage.toPlainText())
    array.append(dlg.inputFieldImage.toPlainText())
    array.append(dlg.inputPrecipitationImage.toPlainText())
    array.append(dlg.inputManagementImage.toPlainText())
    array.append(dlg.inputLandCover.toPlainText())
    sumsixraster(array[0], array[1], array[2], array[3], array[4], array[5], FILEPATH + "temp7" + OUTPUT_FORMAT)
    open_raster(FILEPATH + "temp7" + OUTPUT_FORMAT)
    print("Ended")


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