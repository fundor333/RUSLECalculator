__author__ = 'Fundor333'

from random import randint
from QGisLib import create_raster, open_raster
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
FILENAME = FILEPATH + "temp" + FILETYPE
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
        create_raster(FILENAME, ORG[0], ORG[1], PIXSIZE[0], PIXSIZE[1], matrix, PROJ, NODATA,
                      NUM_BAND, TYPEOFRASTER)
        open_raster(FILENAME)
        print("Ended")