__author__ = 'Fundor333'

from random import randint
import numpy as np

from qgis.core import QgsVectorLayer, QgsField, QgsFeature, QgsPoint, QgsGeometry, QgsVectorFileWriter, \
    QgsMapLayerRegistry, QgsRasterLayer
from PyQt4.QtCore import QVariant, QFileInfo

import gdal
import ogr
import osr


def create_raster(filepath, orgX, orgY, pixWidth, pixHeight, array, proj, nodata, num_band, typeofraster):
    assert (len(array.shape) == 2)
    rot_x = rot_y = 0
    rows, cols = array.shape
    driver = gdal.GetDriverByName(typeofraster)
    raster = driver.Create(filepath, cols, rows, num_band, gdal.GDT_Float32)
    raster.SetGeoTransform((orgX, pixWidth, rot_x, orgY, rot_y, pixHeight))
    band = raster.GetRasterBand(1)
    band.SetNoDataValue(nodata)
    band.WriteArray(array)
    raster_srs = osr.SpatialReference()
    raster_srs.ImportFromEPSG(proj)
    raster.SetProjection(raster_srs.ExportToWkt())
    band.FlushCache()
    print("Raster generated")


def open_raster(filename):
    basename = QFileInfo(filename).baseName()
    print(filename)
    r_layer = QgsRasterLayer(filename, basename)
    if not r_layer.isValid():
        print("Layer failed to load!")
    else:
        QgsMapLayerRegistry.instance().addMapLayer(r_layer)
        print("Layer loaded")
