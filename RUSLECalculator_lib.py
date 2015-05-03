from osgeo.gdalconst import GA_ReadOnly
from osgeo.gdalnumeric import *
import math
from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry
from RUSLECalculator_config import CONFIG_OBJECT
from RUSLECalculator_resurce import CONFIG_CONFIG


def rastermath(k, r, ls, c, p, rasterxsize, rasterysize, datatype,
               path_out=CONFIG_OBJECT.read_config(CONFIG_CONFIG, 'Config_path'), ras_type="GTiff"):
    if p == None:
        dataOut = numpy.sqrt(k * r * ls * c * p)
    else:
        dataOut = numpy.sqrt(k * r * ls * c * p)

    # Write the out file
    driver = gdal.GetDriverByName(ras_type)
    dsOut = driver.Create(path_out, rasterxsize, rasterysize, 1, datatype)
    CopyDatasetInfo(k, dsOut)
    bandOut = dsOut.GetRasterBand(1)
    BandWriteArray(bandOut, dataOut)


def calc_ls(flowacc, cell_size, pend):
    return numpy.sqrt((flowacc * cell_size / 22.13) ** 0.4) * (-1.5 + 17 / 1 + (math.e ** (2.3 - 6.1 * math.sin(pend))))


def calc_r(dem):
    activeLayer = iface.activeLayer()
    input = QgsRasterCalculatorEntry()
    input.ref = dem[2]
    input.raster = dem[1]
    input.bandNumber = 1
    calc = QgsRasterCalculator("(" + dem[2] + '<600)*2768.8196+((' + dem[2] + ">=600)*5509.1530", 'D:\outputfile.tif',
                               'GTiff', activeLayer.extent(), activeLayer.width(), activeLayer.height(), input)

    calc.processCalculation()
    return calc


def calc_c(pendenze):
    return numpy.sqrt()


def open_raster(filename):
    basename = QFileInfo(filename).baseName()
    r_layer = QgsRasterLayer(filename, basename)
    if not r_layer.isValid():
        print("Layer failed to load!")
    else:
        QgsMapLayerRegistry.instance().addMapLayer(r_layer)
        print("Layer loaded")
    return basename, r_layer


def input_open(element):
    basename, r_layer = open_raster(element)
    ds = gdal.Open(element, GA_ReadOnly)
    band = ds.GetRasterBand(1)
    data = BandReadAsArray(band)
    return data, basename, r_layer