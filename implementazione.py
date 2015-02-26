from random import randint
import numpy

__author__ = 'Fundor333'

from qgis.core import QgsVectorLayer, QgsField, QgsFeature, QgsPoint, QgsGeometry, QgsVectorFileWriter, \
    QgsMapLayerRegistry
from PyQt4.QtCore import QVariant

try:
    from osgeo import *
except:
    import gdal
    import ogr
    import osr

def add_element(pr, vl, i, j):
    fet = QgsFeature()
    fet.setGeometry(QgsGeometry.fromPoint(QgsPoint(i, j)))
    fet.setAttributes([randint(0, 100)])
    pr.addFeatures([fet])


def run(dlg):
    ncols = dlg.widthInput.value()
    nrows = dlg.highInput.value()
    if ncols == 0 | nrows == 0:
        print("La matrice non puo' essere costruita correttamente")
    else:
        matrix = numpy.zeros((ncols, nrows))
        for i in range(0, ncols):
            for j in range(0, nrows):
                matrix[i][j] = randint(0, 100)
        create_raster("test.tif", 0.0, 0.0, ncols + 0.0, nrows + 0.0, matrix)


def create_raster(filepath, orgX, orgY, pixWidth, pixHeight, array, proj=4326, gdal_type=gdal.GDT_Float32,
                  nodata=-9999):
    """
    Creates an arbitrary raster
    Args:
    filepath (string): where to save file
    orgX (float): x dimension origin coordinate (bottom left untransformed)
    orgY (float): y dimension origin coordinate (bottom left untransformed)
    pixWidth (float): size of each pixel's width (units depend on
    projection)
    pixHeight (float): size of each pixel's height (units depend on
    projection)
    array (np.array): raster values
    Keyword Args:
    proj (int): EPSG code
    gdal_type (GDAL Datatype): a GDAL datatype
    nodata (same as gdal_type): the NODATA value
    Returns:
    None
    """
    assert (len(array.shape) == 2)
    num_bands = 1
    rotX = 0
    rotY = 0
    rows = array.shape[0]
    cols = array.shape[1]
    driver = gdal.GetDriverByName('GTiff')
    raster = driver.Create(filepath, cols, rows, num_bands, gdal_type)
    print(driver.Create(filepath, cols, rows, num_bands, gdal_type))
    raster.SetGeoTransform((orgX, pixWidth, rotX, orgY, rotY, pixHeight))
    band = raster.GetRasterBand(1)  # Get only raster band
    band.SetNoDataValue(nodata)
    band.WriteArray(array)
    raster_srs = osr.SpatialReference()
    raster_srs.ImportFromEPSG(proj)
    raster.SetProjection(raster_srs.ExportToWkt())
    band.FlushCache()
