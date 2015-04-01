try:
    from osgeo import *
except:
    import gdal
    import ogr
    import osr

from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry
from qgis.core import QgsMapLayerRegistry, QgsRasterLayer
from PyQt4.QtCore import QFileInfo, QObject
from PyQt4.QtGui import QFileDialog

FILEPATH = "/var/tmp/"
FILETYPE = ".asc"
FILENAME = FILEPATH + "temp" + FILETYPE
TYPEOFRASTER = "GTiff"


def selectFile(lineEdit):
    lineEdit.setText(QFileDialog.getOpenFileName())


def init(dlg):
    dlg.b1.clicked.connect(selectFile(dlg.inputL1))
    dlg.b2.clicked.connect(selectFile(dlg.inputL2))
    dlg.b3.clicked.connect(selectFile(dlg.inputL3))
    dlg.b4.clicked.connect(selectFile(dlg.inputL4))
    dlg.b5.clicked.connect(selectFile(dlg.inputL5))
    dlg.b6.clicked.connect(selectFile(dlg.inputL6))


def run(dlg):
    array = range(0, 6)
    array[0] = dlg.inputL1.toPlainText()
    array[1] = dlg.inputL2.toPlainText()
    array[2] = dlg.inputL3.toPlainText()
    array[3] = dlg.inputL4.toPlainText()
    array[4] = dlg.inputL5.toPlainText()
    array[5] = dlg.inputL6.toPlainText()
    sumsixraster(array[0], array[1], array[2], array[3], array[4], array[5], FILEPATH + "temp7" + FILETYPE)
    print("Ended")


def open_raster(filename):
    basename = QFileInfo(filename).baseName()
    print(filename)
    r_layer = QgsRasterLayer(filename, basename)
    if not r_layer.isValid():
        print("Layer failed to load!")
    else:
        QgsMapLayerRegistry.instance().addMapLayer(r_layer)
        print("Layer loaded")
    return r_layer


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
    calc.processCalculation()
    open_raster(path_out)


class ButtonSignal(QObject):
    def __init__(self, dlg):
        QObject.__init__(self)
        self.dlg = dlg

    def clickedme1(self):
        selectFile(self.dlg.inputL1)

    def clickedme2(self):
        selectFile(self.dlg.inputL2)

    def clickedme3(self):
        selectFile(self.dlg.inputL3)

    def clickedme4(self):
        selectFile(self.dlg.inputL4)

    def clickedme5(self):
        selectFile(self.dlg.inputL5)

    def clickedme6(self):
        selectFile(self.dlg.inputL6)