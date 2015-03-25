from PyQt4 import QtGui

try:
    from osgeo import *
except:
    import gdal
    import ogr
    import osr

from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry
from qgis.core import QgsMapLayerRegistry, QgsRasterLayer
from qgis.utils import iface
from PyQt4.QtCore import QFileInfo
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

    array[0] = dlg.inputL1.text().encode("utf-8")
    array[1] = dlg.inputL2.text().encode("utf-8")
    array[2] = dlg.inputL3.text().encode("utf-8")
    array[3] = dlg.inputL4.text().encode("utf-8")
    array[4] = dlg.inputL5.text().encode("utf-8")
    array[5] = dlg.inputL6.text().encode("utf-8")
    # codice di popolamento dell'array
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


def sumsixraster(rl1, rl2, rl3, rl4, rl5, rl6, path_file, raster_type="GTiff"):
    inp = rl1, rl2, rl3, rl4, rl5, rl6
    entries = []
    listname = []

    for element in inp:
        open_raster(element)

    for i in range(0, 6):
        a = QgsRasterCalculatorEntry()
        a.ref = inp[i].name()
        a.raster = inp[i]
        a.bandNumber = 1
        listname.append(str(inp[i].name()))
        entries.append(a)

    formula_string = listname[0] + " + " + listname[1] + " + " + listname[1] + " + " + listname[2] + " + " + listname[
        4] + " + " + listname[5]
    calc = QgsRasterCalculator(formula_string, path_file, raster_type, rl1.extent(), rl1.width(), rl1.height(), entries)
    calc.processCalculation()
    open_raster(path_file)
