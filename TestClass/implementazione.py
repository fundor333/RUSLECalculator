from random import randint

__author__ = 'Fundor333'

from qgis.core import QgsVectorLayer, QgsField, QgsFeature, QgsPoint, QgsGeometry, QgsVectorFileWriter, \
    QgsMapLayerRegistry
from PyQt4.QtCore import QVariant


def add_element(pr, vl, i, j):
    fet = QgsFeature()
    fet.setGeometry(QgsGeometry.fromPoint(QgsPoint(i, j)))
    fet.setAttributes([randint(0, 100)])
    pr.addFeatures([fet])


def run(dlg):
    alt = dlg.widthInput.value()
    larg = dlg.highInput.value()
    if larg == 0 | alt == 0:
        pass
    else:

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
        print("extent:", "0", "0" , alt, larg)
        # iterate over features
        renderer = vl.rendererV2()
        for f in vl.getFeatures():
            print("F:", f.id(), f.attributes(), f.geometry().asPoint())

#            print(f.__class__.__name__)
#            print("%f - %f: %s %s" % (
#                f.lowerValue(),
#                f.upperValue(),
#                f.label(),
#                str(f.symbol())
#            ))

        # TODO Bisogna sistemare la visualizzazione grafica del plugin
        QgsMapLayerRegistry.instance().addMapLayer(vl)