from PyQt4.uic.properties import QtGui
from MatrixModule_lib import open_raster
from MatrixModule_resurce import FILEPATH, OUTPUT_FORMAT, CONFIG_CONFIG

try:
    from osgeo import *
except:
    import gdal
    import ogr
    import osr

from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry
from PyQt4.QtCore import QObject
from PyQt4.QtGui import QFileDialog


def selectFile(lineEdit):
    lineEdit.setText(QFileDialog.getOpenFileName())


def selectconfig(parent, config):
    filename = QtGui.QFileDialog.getOpenFileName(
        parent, 'Open File', '', 'Images (*.png *.xpm *.jpg)',
        None, QtGui.QFileDialog.DontUseNativeDialog)
    config.edit_config(CONFIG_CONFIG, 'Config_path', filename)


def init(dlg):
    dlg.DEM.clicked.connect(selectFile(dlg.inputDEM))
    dlg.SoilImage.clicked.connect(selectFile(dlg.inputSoilImage))
    dlg.FieldImage.clicked.connect(selectFile(dlg.inputFieldImage))
    dlg.PrecipitationImage.clicked.connect(selectFile(dlg.inputPrecipitationImage))
    dlg.ManagementImage.clicked.connect(selectFile(dlg.inputManagementImage))
    dlg.LandCover.clicked.connect(selectFile(dlg.inputLandCover))


def run(dlg):
    array = range(0, 6)
    array[0] = dlg.inputDEM.toPlainText()
    array[1] = dlg.inputSoilImage.toPlainText()
    array[2] = dlg.inputFieldImage.toPlainText()
    array[3] = dlg.inputPrecipitationImage.toPlainText()
    array[4] = dlg.inputManagementImage.toPlainText()
    array[5] = dlg.inputLandCover.toPlainText()
    sumsixraster(array[0], array[1], array[2], array[3], array[4], array[5], FILEPATH + "temp7" + OUTPUT_FORMAT)
    print("Ended")


def sumsixraster(rl1, rl2, rl3, rl4, rl5, rl6, path_out, ras_type="GTiff"):
    inp = rl1, rl2, rl3, rl4, rl5, rl6
    elements = []
    list_name = []
    rast_ent = []

    for element in inp:
        rast_ent.append((element, open_raster(element)))

    for i in range(0, 6):
        a = QgsRasterCalculatorEntry()
        a.ref = rast_ent[i][0]
        a.raster = rast_ent[i][1]
        a.bandNumber = 1
        list_name.append(a.raster.name())
        elements.append(a)

    formula = list_name[0] + " + " + list_name[1] + " + " + list_name[2] + " + " + list_name[3] + " + " + list_name[
        4] + " + " + list_name[5]
    print(formula)
    calc = QgsRasterCalculator(formula, path_out, ras_type, elements[0].raster.extent(), elements[0].raster.width(),
                               elements[0].raster.height(), elements)
    print(calc.processCalculation())
    open_raster(path_out)


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