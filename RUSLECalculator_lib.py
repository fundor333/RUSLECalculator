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
from qgis.core import QgsRasterLayer, QgsMapLayerRegistry

from osgeo.gdalconst import GA_ReadOnly

from osgeo.gdalnumeric import gdal

from PyQt4.QtCore import QFileInfo
from RUSLECalculator_error import LOG


def aez_calc(aez):
    i = 0
    for row in aez:
        y = 0
        for element in row:
            ele = element.get(4)
            if ele == 1:
                aez[i][y] = 11.6171685
            elif ele == 2:
                aez[i][y] = 11.6171685
            elif ele == 3:
                aez[i][y] = 13.5533632
            y += 1
        i += 1


def get_aez(c):
    aez = c
    i = 0
    for row in aez:
        y = 0
        for element in row:
            ele = element.get(4)
            if ele == 1:
                aez[i][y] = 11.6171685
            elif ele == 2:
                aez[i][y] = 11.6171685
            elif ele == 3:
                aez[i][y] = 13.5533632
            y += 1
        i += 1


def open_raster(filename):
    LOG.i("Opening the layer " + filename)
    basename = QFileInfo(filename).baseName()
    r_layer = QgsRasterLayer(filename, basename)
    if not r_layer.isValid():
        LOG.e("Layer failed to load! " + filename)
        raise IOError
    else:
        QgsMapLayerRegistry.instance().addMapLayer(r_layer)
        LOG.i("Layer loaded " + filename)
    return basename, r_layer


def iterable_function(k, r, ls, c, p):
    open_k = gdal.Open(k)
    open_r = gdal.Open(r)
    open_ls = gdal.Open(ls)
    open_c = gdal.Open(c)
    src_k = open_k.ReadAsArray()
    src_r = open_r.ReadAsArray()
    src_ls = open_ls.ReadAsArray()
    src_c = open_c.ReadAsArray()

    try:
        open_p = gdal.Open(p)
        src_p = open_p.ReadAsArray()
        final_data = src_c * src_k * src_r * src_ls * src_p

    except Exception:
        final_data = src_c * src_k * src_r * src_ls

    return (final_data * 29.0142 / 100)


def get_soil_loss(k, r, ls, c, p, dem, outputfile, driver_name, years=1):
    LOG.i("Start calc the raster")
    open_dem = gdal.Open(dem)
    final_data = None

    for i in range(0, years):
        final_data = iterable_function(k, r, ls, c, p)


    # get parameters
    geotransform = open_dem.GetGeoTransform()
    spatialreference = open_dem.GetProjection()
    data_type = open_dem.GetRasterBand(1).DataType
    ncol = open_dem.RasterXSize
    nrow = open_dem.RasterYSize
    nband = 1

    # create dataset for output
    driver = gdal.GetDriverByName(driver_name)
    dst_dataset = driver.Create(outputfile, ncol, nrow, nband, data_type)
    dst_dataset.SetGeoTransform(geotransform)
    dst_dataset.SetProjection(spatialreference)
    dst_dataset.GetRasterBand(1).WriteArray(final_data)
    dst_dataset = None
    open_raster(outputfile)
