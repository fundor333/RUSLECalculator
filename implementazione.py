__author__ = 'Fundor333'

from random import randint
import numpy as np

from qgis.core import QgsVectorLayer, QgsField, QgsFeature, QgsPoint, QgsGeometry, QgsVectorFileWriter, \
    QgsMapLayerRegistry, QgsRasterLayer
from PyQt4.QtCore import QVariant, QFileInfo

try:
    from osgeo import *
except:
    import gdal
    import ogr
    import osr

FILEPATH = "/var/tmp/"
FILETYPE = ".tif"
# TODO Far scegliere il nome del file all'utente sotto forma di campo?
#TODO Sistemare il codice in modo che usi sempre la cartella temp, indipendentemente dal OS usato
TYPEOFRASTER = "GTiff"
#TODO Variazione del tipo di raster generato?
NODATA = -9999
PROJ = 4326
ORG = (0.0, 0.0)
PIXSIZE = (10.0, 10.0)
NUM_BAND = 1


def run(dlg):
    ncols = dlg.widthInput.value()
    nrows = dlg.highInput.value()
    if ncols == 0 | nrows == 0:
        print("Problem with the matrix's size")
    else:
        matrix = np.zeros((nrows, ncols))
        for i in range(0, nrows):
            for j in range(0, ncols):
                matrix[i][j] = randint(0, 100)
        create_raster(FILEPATH + "temp" + FILETYPE, ORG[0], ORG[1], PIXSIZE[0], PIXSIZE[1], matrix, PROJ, NODATA,
                      NUM_BAND)
        open_raster(FILEPATH)
        print("Ended")


def create_raster(filepath, orgX, orgY, pixWidth, pixHeight, array, proj, nodata, num_band):
    assert (len(array.shape) == 2)
    rot_x = rot_y = 0
    rows, cols = array.shape
    driver = gdal.GetDriverByName(TYPEOFRASTER)
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
    r_layer = QgsRasterLayer(filename, basename)
    if not r_layer.isValid():
        print("Layer failed to load!")
    else:
        QgsMapLayerRegistry.instance().addMapLayer(r_layer)
        print("Layer loaded")
