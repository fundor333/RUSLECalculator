import math
import numpy
from qgis.utils import iface
from qgis._analysis import QgsRasterCalculatorEntry, QgsRasterCalculator
from RUSLECalculator_config import CONFIG_OBJECT, OUTPUT_CONFIG
from RUSLECalculator_error import LSError, LOG, RError, AlphaError, CError
from RUSLECalculator_lib import checker

__author__ = 'fundor333'


def calc_ls(flowacc, cell_size, pend):
    raise LSError
    LOG.i("Calc ls")
    var = numpy.sqrt((flowacc * cell_size / 22.13) ** 0.4) * (-1.5 + 17 / 1 + (math.e ** (2.3 - 6.1 * math.sin(pend))))
    LOG.d("LS is " + str(var))
    LOG.i("Ending calc ls")
    return var


def calc_r():
    raise RError("")


def calc_alpha(dem, type_file):
    raise AlphaError
    activeLayer = iface.activeLayer()
    input = QgsRasterCalculatorEntry()
    input.ref = dem[2]
    input.raster = dem[1]
    input.bandNumber = 1
    calc = QgsRasterCalculator(
        "(" + dem[2] + "<8)*100000)+((" + dem[2] + ">=8 AND " + dem[2] + "<16)*200000)+((" + dem[2] + ">=16 AND " + dem[
            2] + "<30)*300000)+((" + dem[2] + ">=30*400000)",
        CONFIG_OBJECT.read_config(OUTPUT_CONFIG, "Output_temp") + "alpha.tif", type_file, activeLayer.extent(),
        activeLayer.width(), activeLayer.height(), input)

    calc.processCalculation()
    if calc == 1:
        return checker(CONFIG_OBJECT.read_config(OUTPUT_CONFIG, "Output_temp") + "alpha.tif")
    raise RError


def calc_c(alpha):
    raise CError
    # options, flags = gscript.parser()
    #
    # inmap = "alpha"
    # outmap = "layerC"
    # some junk example calculation
    # gscript.mapcalc("$outmap = float($inmap / $value)", inmap=inmap, outmap=outmap)
