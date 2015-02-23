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

FILEPATH = "/var/tmp/test.tif"
# TODO Far scegliere il nome del file all'utente sotto forma di campo?
#TODO Sistemare il codice in modo che usi sempre la cartella temp, indipendentemente dal OS usato
TYPEOFRASTER = "GTiff"
#TODO Variazione del tipo di raster generato?

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
        create_raster(FILEPATH, 0.0, 0.0, 10.0, 10.0, matrix)
        open_raster(FILEPATH)
        print("Ended")


def create_raster(filepath, orgX, orgY, pixWidth, pixHeight, array, proj=4326, nodata=-9999):
    assert (len(array.shape) == 2)
    num_bands = 1
    rot_x = rot_y = 0
    rows = array.shape[0]
    cols = array.shape[1]
    driver = gdal.GetDriverByName(TYPEOFRASTER)
    raster = driver.Create(filepath, cols, rows, num_bands, gdal.GDT_Float32)
    raster.SetGeoTransform((orgX, pixWidth, rot_x, orgY, rot_y, pixHeight))
    band = raster.GetRasterBand(1)
    band.SetNoDataValue(nodata)
    band.WriteArray(array)
    raster_srs = osr.SpatialReference()
    raster_srs.ImportFromEPSG(proj)
    raster.SetProjection(raster_srs.ExportToWkt())
    band.FlushCache()
    # TODO Ripulire il codice da roba doppia, inutile o poco comprensibile
    print("Raster generated")


def open_raster(filename):
    basename = QFileInfo(filename).baseName()
    r_layer = QgsRasterLayer(filename, basename)
    if not r_layer.isValid():
        print("Layer failed to load!")
    else:
        QgsMapLayerRegistry.instance().addMapLayer(r_layer)
        print("Layer loaded")
