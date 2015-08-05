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
from osgeo.gdalnumeric import BandWriteArray, BandReadAsArray, numpy, gdal

from PyQt4.QtCore import QFileInfo

from RUSLECalculator_error import LOG, OutError


def rastermath(k, r, ls, c, p, out, rasterxsize, rasterysize, gdalType, ras_type="GTiff"):
    LOG.i("Start calc the raster")
    if p is None:
        LOG.d("P is None")
        dataOut = numpy.sqrt(k[0] * r[0] * ls[0] * c[0])
        dataOut = dataOut * 29.0142 / 100
        LOG.d(dataOut)
    else:
        LOG.d("P is not NONE")
        dataOut = numpy.sqrt(k[0] * r[0] * ls[0] * c[0] * p[0])
        dataOut = dataOut * 29.0142 / 100
        LOG.d(dataOut)

    # Write the out file
    driver = gdal.GetDriverByName(ras_type)
    dsOut = driver.Create(out, rasterxsize, rasterysize, 1, gdalType)

    geotransform = k.GetGeoTransform()
    spatialreference = k.GetProjection()
    dsOut.SetGeoTransform(geotransform)
    dsOut.SetProjection(spatialreference)

    LOG.i("Writing the result")
    bandOut = dsOut.GetRasterBand(1)
    BandWriteArray(bandOut, dataOut)


def output_open(filename):
    if filename is None:
        raise OutError
    return filename


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
    LOG.d("checker() return " + data)
    return data


def test_math(dem, fieldimage, k, r, ls, c, p, outputfile, datatype):
    LOG.i("Start calc the raster")
    open_k = gdal.Open(k)
    open_r = gdal.Open(r)
    open_ls = gdal.Open(ls)
    open_c = gdal.Open(c)
    open_p = gdal.Open(p)
    open_dem = gdal.Open(dem)
    open_fieldimage = gdal.Open(fieldimage)

    src_k = open_k.ReadAsArray()
    src_r = open_r.ReadAsArray()
    src_ls = open_ls.ReadAsArray()
    src_c = open_c.ReadAsArray()
    src_p = open_p.ReadAsArray()
    src_dem = open_dem.ReadAsArray()
    src_fieldimage = open_fieldimage.ReadAsArray()

    # final_data is a 2-D Numpy array of the same dimensions as src_data
    final_data = src_c + src_k + src_r + src_ls + src_p

    # get parameters
    geotransform = src_k.GetGeoTransform()
    spatialreference = src_k.GetProjection()
    ncol = src_k.RasterXSize
    nrow = src_k.RasterYSize
    nband = 1

    # create dataset for output
    fmt = 'GTiff'
    driver = gdal.GetDriverByName(fmt)
    dst_dataset = driver.Create([outputfile], ncol, nrow, nband, gdal.GDT_Byte)
    dst_dataset.SetGeoTransform(geotransform)
    dst_dataset.SetProjection(spatialreference)
    dst_dataset.GetRasterBand(1).WriteArray(final_data)
    dst_dataset = None
