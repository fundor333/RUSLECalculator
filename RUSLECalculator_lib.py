"""
/***************************************************************************
 RUSLECalculator_lib
                                 A QGIS plugin
 Plugin
                             -------------------
        begin                : 2015-03-12
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Matteo Scarpa
        email                : matteoscarpa92@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import logging
from qgis.utils import iface
from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry
from qgis.core import QgsRasterLayer, QgsMapLayerRegistry
from osgeo.gdalconst import GA_ReadOnly
from osgeo.gdalnumeric import CopyDatasetInfo, BandWriteArray, BandReadAsArray, math, numpy, gdal

from PyQt4.QtCore import QFileInfo
from RUSLECalculator_config import CONFIG_CONFIGURATION, OUTPUT_CONFIG, CONFIG_DIR, CONFIG_OBJECT


def rastermath(k, r, ls, c, p, rasterxsize, rasterysize, datatype,
               path_out=CONFIG_OBJECT.read_config(CONFIG_CONFIGURATION, 'Config_path'), ras_type="GTiff"):
    LOGGER.info("Start calc the raster")
    if p is None:
        dataOut = numpy.sqrt(k * r * ls * c)
        LOGGER.debug("P is None")
    else:
        dataOut = numpy.sqrt(k * r * ls * c * p)
        LOGGER.debug("P is not NONE")

    # Write the out file
    driver = gdal.GetDriverByName(ras_type)
    dsOut = driver.Create(path_out, rasterxsize, rasterysize, 1, datatype)
    LOGGER.info("Writing the result")
    CopyDatasetInfo(k, dsOut)
    bandOut = dsOut.GetRasterBand(1)
    BandWriteArray(bandOut, dataOut)


def calc_ls(flowacc, cell_size, pend):
    LOGGER.info("Calc ls")
    var = numpy.sqrt((flowacc * cell_size / 22.13) ** 0.4) * (-1.5 + 17 / 1 + (math.e ** (2.3 - 6.1 * math.sin(pend))))
    LOGGER.debug("LS is " + str(var))
    LOGGER.info("Ending calc ls")
    return var


def calc_r():
    raise RError("")


def calc_alpha(dem, type_file):
    activeLayer = iface.activeLayer()
    input = QgsRasterCalculatorEntry()
    input.ref = dem[2]
    input.raster = dem[1]
    input.bandNumber = 1
    calc = QgsRasterCalculator(
        "(" + dem[2] + "<8)*100000)+((" + dem[2] + ">=8 AND " + dem[2] + "<16)*200000)+((" + dem[2] + ">=16 AND " + dem[
            2] + "<30)*300000)+((" + dem[2] + ">=30*400000)",
        CONFIG_OBJECT.read_config(OUTPUT_CONFIG, "Output_temp") + "alpha.tif", type_file, activeLayer.extent(),
        activeLayer.width(), activeLayer.height(), input)

    calc.processCalculation()
    if calc == 1:
        return checker(CONFIG_OBJECT.read_config(OUTPUT_CONFIG, "Output_temp") + "alpha.tif")
    raise RError


def calc_c(alpha):
    raise CError
    # options, flags = gscript.parser()
    #
    # inmap = "alpha"
    # outmap = "layerC"
    # some junk example calculation
    # gscript.mapcalc("$outmap = float($inmap / $value)", inmap=inmap, outmap=outmap)


def open_raster(filename):
    LOGGER.info("Opening the layer")
    basename = QFileInfo(filename).baseName()
    r_layer = QgsRasterLayer(filename, basename)
    if not r_layer.isValid():
        LOGGER.error("Layer failed to load!")
    else:
        QgsMapLayerRegistry.instance().addMapLayer(r_layer)
        LOGGER.info("Layer loaded")
    return basename, r_layer


def input_open(element):
    basename, r_layer = open_raster(element)
    ds = gdal.Open(element, GA_ReadOnly)
    band = ds.GetRasterBand(1)
    data = BandReadAsArray(band)
    return data, basename, r_layer


def checker(element):
    open_raster(element)
    ds = gdal.Open(element, GA_ReadOnly)
    band = ds.GetRasterBand(1)
    data = BandReadAsArray(band)
    LOGGER.debug("checker() return " + data)
    return data


class NoDem(Exception):
    def __init__(self, message):
        self.message = message
        LOGGER.error("NoDem " + message)


class NoFieldImage(Exception):
    def __init__(self, message):
        self.message = message
        LOGGER.error("NoFieldImage " + message)


class RasterError(Exception):
    def __init__(self, message):
        self.message = message
        LOGGER.error("RasterError " + message)


class RError(Exception):
    def __init__(self, message):
        self.message = message
        LOGGER.error("RError " + message)


class AlphaError(Exception):
    def __init__(self, message):
        self.message = message
        LOGGER.error("AlphaError " + message)


class LSError(Exception):
    def __init__(self, message):
        self.message = message
        LOGGER.error("LSError " + message)


class CError(Exception):
    def __init__(self, message):
        self.message = message
        LOGGER.error("CError " + message)


class KError(Exception):
    def __init__(self, message):
        self.message = message
        LOGGER.error("KError " + message)


class MyLogger():
    def __init__(self, filename=None):
        if filename is None:
            logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        else:
            logging.basicConfig(filename=filename, level=logging.DEBUG,
                                format='%(asctime)s - %(levelname)s - %(message)s')

    def critical(self, string):
        logging.critical(string)

    def error(self, string):
        logging.error(string)

    def warning(self, string):
        logging.warning(string)

    def info(self, string):
        logging.info(string)

    def debug(self, string):
        logging.debug(string)


LOGGER = MyLogger("/var/tmp/log.txt")
