from random import randint

__author__ = 'Fundor333'

from qgis.core import QgsVectorLayer, QgsField, QgsFeature, QgsPoint, QgsGeometry, QgsVectorFileWriter, \
    QgsMapLayerRegistry
from PyQt4.QtCore import QVariant
from osgeo import gdal, ogr
import numpy

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
        cellsize = 25
        nodata_value = -9999
        xllcorner = 0

        source_layer = numpy.zeros((ncols, nrows))
        for i in range(0, ncols):
            for j in range(0, nrows):
                source_layer[i][j] = randint(0, 100)

        # Create the destination data source
        target_ds = gdal.GetDriverByName('GTiff').Create("test.tif", nrows, ncols, 1, gdal.GDT_Byte)
        target_ds.SetGeoTransform((xllcorner, cellsize, 0, nrows * cellsize, 0, -cellsize))
        band = target_ds.GetRasterBand(1)
        band.SetNoDataValue(nodata_value)

        # Rasterize
        gdal.RasterizeLayer(target_ds, [1], source_layer, burn_values=[0])


def las(alt, larg):
    vl = QgsVectorLayer("Point", "temporary_points", "memory")
    pr = vl.dataProvider()

    pr.addAttributes([QgsField("value", QVariant.Int)])

    for i in range(0, larg):
        for j in range(0, alt):
            add_element(pr, vl, i, j)
    vl.updateExtents()

    # show some stats
    print("fields: ", len(pr.fields()))
    print("features: ", pr.featureCount())
    e = vl.extent()
    print(e.__class__.__name__)
    print("extent:", "0", "0", alt, larg)
    # iterate over features
    renderer = vl.rendererV2()
    for f in vl.getFeatures():
        print("F:", f.id(), f.attributes(), f.geometry().asPoint())

    # print(f.__class__.__name__)
    # print("%f - %f: %s %s" % (
    #                f.lowerValue(),
    #                f.upperValue(),
    #                f.label(),
    #                str(f.symbol())
    #            ))

    # TODO Bisogna sistemare la visualizzazione grafica del plugin
    QgsMapLayerRegistry.instance().addMapLayer(vl)


