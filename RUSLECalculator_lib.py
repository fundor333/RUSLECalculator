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
import math

from osgeo.gdalconst import GA_ReadOnly
from osgeo.gdalnumeric import *
from qgis.utils import iface
from PyQt4.QtCore import QFileInfo
from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry
from qgis.core import QgsRasterLayer, QgsMapLayerRegistry
from RUSLECalculator_Exception import RError
from RUSLECalculator_config import CONFIG_OBJECT
from RUSLECalculator_resurce import CONFIG_CONFIG, OUTPUT_CONFIG

def rastermath(k, r, ls, c, p, rasterxsize, rasterysize, datatype,
               path_out=CONFIG_OBJECT.read_config(CONFIG_CONFIG, 'Config_path'), ras_type="GTiff"):
    if p == None:
        dataOut = numpy.sqrt(k * r * ls * c)
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


def calc_r(dem, fileout, type_file):
    activeLayer = iface.activeLayer()
    input = QgsRasterCalculatorEntry()
    input.ref = dem[2]
    input.raster = dem[1]
    input.bandNumber = 1
    calc = QgsRasterCalculator("(" + dem[2] + '<600)*2768.8196+((' + dem[2] + ">=600)*5509.1530",
                               fileout, type_file, activeLayer.extent(), activeLayer.width(), activeLayer.height(),
                               input)
    calc.processCalculation()
    if calc == 1:
        return checker(fileout)
    raise RError


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
    raise NotImplemented
    options, flags = grass.parser()

    inmap = "alpha"
    outmap = "layerC"
    # some junk example calculation
    grass.mapcalc("$outmap = float($inmap / $value)", inmap=inmap, outmap=outmap)


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


def checker(element):
    open_raster(element)
    ds = gdal.Open(element, GA_ReadOnly)
    band = ds.GetRasterBand(1)
    data = BandReadAsArray(band)
    return data