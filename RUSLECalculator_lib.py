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
from RUSLECalculator_Gui_Implementation import getListFile
from RUSLECalculator_error import LOG, DriverError
from RUSLECalculator_resurce import AEZ100, AEZ200, AEZ300


def aez_calc(aez):
    i = 0
    for row in aez:
        y = 0
        for element in row:
            ele = element.get(3)
            if ele == 1:
                aez[i][y] = AEZ100
            elif ele == 2:
                aez[i][y] = AEZ200
            elif ele == 3:
                aez[i][y] = AEZ300
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


def iterable_function(k, r, ls, c, p, pixel_value):
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

    return final_data * pixel_value / 100


def get_pixel_size(dem):
    dataset = gdal.Open(dem, GA_ReadOnly)
    geotransform = dataset.GetGeoTransform()
    return geotransform[1]


def elaborate_document(document_file, num):
    output = []
    if document_file[0] == num:
        output = document_file[1]
    else:
        if document_file[0] == 0:
            for i in range(0, num):
                output[i] = document_file[0]
        else:
            for i in range(0, num):
                output[i] = document_file[0][i % document_file[0].size]
    return output


def writer_dataset(open_dem, driver_name, final_data, outputfile):
    # get parameters
    geotransform = open_dem.GetGeoTransform()
    spatialreference = open_dem.GetProjection()
    data_type = open_dem.GetRasterBand(1).DataType
    ncol = open_dem.RasterXSize
    nrow = open_dem.RasterYSize
    nband = 1

    # create dataset for output
    driver = gdal.GetDriverByName(driver_name)
    LOG.d(driver)
    if driver != None:
        dst_dataset = driver.Create(outputfile, ncol, nrow, nband, data_type)
        dst_dataset.SetGeoTransform(geotransform)
        dst_dataset.SetProjection(spatialreference)
        dst_dataset.GetRasterBand(1).WriteArray(final_data)
        dst_dataset = None
        open_raster(outputfile)
    else:
        raise DriverError()


def get_soil_loss(k, r, ls, c, p, dem, outputfile, driver_name, years=1):
    LOG.i("Start calc the raster")
    LOG.i("The driver use is " + driver_name)
    open_dem = gdal.Open(dem)
    pixel_size = get_pixel_size(dem)
    final_data = None

    k_file = getListFile(k[0], k[1], years)
    r_file = getListFile(r[0], r[1], years)
    ls_file = getListFile(ls[0], ls[1], years)
    c_file = getListFile(c[0], c[1], years)
    p_file = getListFile(p[0], p[1], years)
    dem_file = getListFile(dem[0], dem[1], years)

    for i in range(0, years):
        if (final_data == None):
            final_data = iterable_function(k_file, r_file, ls_file, c_file, p_file, pixel_size)
        else:
            final_data += iterable_function(k_file, r_file, ls_file, c_file, p_file, pixel_size)

    writer_dataset(open_dem, driver_name, final_data, outputfile)
