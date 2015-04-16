from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry
from MatrixModule_lib import open_raster


def sumsixraster(rl1, rl2, rl3, rl4, rl5, rl6, path_out, ras_type="GTiff"):
    inp = rl1, rl2, rl3, rl4, rl5, rl6
    elements = []
    list_name = []
    rast_ent = []

    for elem in inp:
        rast_ent.append((elem, open_raster(elem)))

    for i in range(0, 6):
        a = QgsRasterCalculatorEntry()
        a.ref = rast_ent[i][0]
        a.raster = rast_ent[i][1]
        a.bandNumber = 1
        list_name.append(a.raster.name())
        elements.append(a)

    formula = list_name[0] + " + " + list_name[1] + " + " + list_name[2] + " + " + list_name[3] + " + " + list_name[
        4] + " + " + list_name[5]
    print(formula)
    calc = QgsRasterCalculator(formula, path_out, ras_type, elements[0].raster.extent(), elements[0].raster.width(),
                               elements[0].raster.height(), elements)
    print(calc.processCalculation())
    open_raster(path_out)