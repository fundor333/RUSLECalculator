try:
    from osgeo import *
except:
    import gdal
    import ogr
    import osr

from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry
from qgis.core import QgsMapLayerRegistry
from PyQt4.QtCore import QVariant, QFileInfo

FILEPATH = "/var/tmp/"
FILETYPE = ".asc"
FILENAME = FILEPATH + "temp" + FILETYPE
TYPEOFRASTER = "GTiff"


def run(dlg):
    array = []
    layerMap = QgsMapLayerRegistry.instance().mapLayers()

    array[0] = layerMap(dlg.inputL1.getValue())
    array[1] = layerMap(dlg.inputL2.getValue())
    array[2] = layerMap(dlg.inputL3.getValue())
    array[3] = layerMap(dlg.inputL4.getValue())
    array[4] = layerMap(dlg.inputL5.getValue())
    array[5] = layerMap(dlg.inputL6.getValue())
    # codice di popolamento dell'array
    if array.__sizeof__() != 6:
        print("The program need 6 raster to work correctly")
    else:
        array = []
        sumsixraster(array[0], array[1], array[2], array[3], array[4], array[5], FILEPATH + "temp7" + FILETYPE)
    print("Ended")


def open_raster(filename):
    basename = QFileInfo(filename).baseName()
    print(filename)
    r_layer = QgsRasterLayer(filename, basename)
    if not r_layer.isValid():
        print("Layer failed to load!")
    else:
        QgsMapLayerRegistry.instance().addMapLayer(r_layer)
        print("Layer loaded")
    return r_layer


def sumsixraster(rl1, rl2, rl3, rl4, rl5, rl6, path_file, raster_type="GTiff"):
    inp = rl1, rl2, rl3, rl4, rl5, rl6
    entries = []

    for i in range(0, 6):
        a = QgsRasterCalculatorEntry()
        a.ref = inp[i].name() + '@1'
        a.raster = inp[i]
        a.bandNumber = 1
        entries.append(a)

    formula_string = "temp1@1 + temp2@1 + temp3@1 + temp4@1 + temp5@1 + temp6@1"
    calc = QgsRasterCalculator(formula_string, path_file, raster_type, rl1.extent(), rl1.width(), rl1.height(), entries)
    calc.processCalculation()
    open_raster(path_file)


class TestClassDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(TestClassDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
