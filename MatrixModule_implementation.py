from PyQt4 import QtGui
try:
    from osgeo import *
except:
    import gdal
    import ogr
    import osr

from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry
from qgis.core import QgsMapLayerRegistry, QgsRasterLayer
from PyQt4.QtCore import QFileInfo

FILEPATH = "/var/tmp/"
FILETYPE = ".asc"
FILENAME = FILEPATH + "temp" + FILETYPE
TYPEOFRASTER = "GTiff"


def init(dlg):
    layerMap = QgsMapLayerRegistry.instance().mapLayers()

    for a in layerMap:
        print(str(a))
    print("")

def run(dlg):
    layerMap = QgsMapLayerRegistry.instance().mapLayers()
    array = range(0, 6)

    array[0] = layerMap[dlg.inputL1.text().encode("utf-8")]
    array[1] = layerMap[dlg.inputL2.text().encode("utf-8")]
    array[2] = layerMap[dlg.inputL3.text().encode("utf-8")]
    array[3] = layerMap[dlg.inputL4.text().encode("utf-8")]
    array[4] = layerMap[dlg.inputL5.text().encode("utf-8")]
    array[5] = layerMap[dlg.inputL6.text().encode("utf-8")]
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

    for i in range(0, 6):
        a = QgsRasterCalculatorEntry()
        a.ref = inp[i].name() + '@1'
        a.raster = inp[i]
        a.bandNumber = 1
        entries.append(a)

    formula_string = "temp1@1 + temp2@1 + temp3@1 + temp4@1 + temp5@1 + temp6@1"
    calc = QgsRasterCalculator(formula_string, path_file, raster_type, rl1.extent(), rl1.width(), rl1.height(), entries)
    calc.processCalculation()
    open_raster(path_file)