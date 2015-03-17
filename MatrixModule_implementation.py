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

FILEPATH = "/var/tmp/"
FILETYPE = ".asc"
FILENAME = FILEPATH + "temp" + FILETYPE
TYPEOFRASTER = "GTiff"


def init(dlg):
    canvas = iface.mapCanvas()
    layerMap = canvas.layers()

    print(layerMap)
    print("")
    array = range(0, 6)
    i = 0
    for a in layerMap:
        array[i] = a.name()
        i = +1
        print(str(a.name()))


def run(dlg):
    layerMap = iface.mapCanvas().layers()
    layerarray = []
    namearray = []
    for element in layerMap:
        namearray.append(element.name())
        layerarray.append(element)
    array = range(0, 6)

    array[0] = layerarray[namearray.index(dlg.inputL1.text().encode("utf-8"))]
    array[1] = layerarray[namearray.index(dlg.inputL2.text().encode("utf-8"))]
    array[2] = layerarray[namearray.index(dlg.inputL3.text().encode("utf-8"))]
    array[3] = layerarray[namearray.index(dlg.inputL4.text().encode("utf-8"))]
    array[4] = layerarray[namearray.index(dlg.inputL5.text().encode("utf-8"))]
    array[5] = layerarray[namearray.index(dlg.inputL6.text().encode("utf-8"))]
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