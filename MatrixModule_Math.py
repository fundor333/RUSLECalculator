from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry
from MatrixModule_lib import open_raster
import numpy
from osgeo import gdal
from osgeo.gdalnumeric import *
from osgeo.gdalconst import *


def sumsixraster(rl1, rl2, rl3, rl4, rl5, rl6, path_out, ras_type="GTiff"):
    # Open the dataset and read the data into numpy arrays
    ds1 = gdal.Open(rl1, GA_ReadOnly)
    ds2 = gdal.Open(rl2, GA_ReadOnly)
    ds3 = gdal.Open(rl3, GA_ReadOnly)
    ds4 = gdal.Open(rl4, GA_ReadOnly)
    ds5 = gdal.Open(rl5, GA_ReadOnly)
    ds6 = gdal.Open(rl6, GA_ReadOnly)

    band1 = ds1.GetRasterBand(1)
    band2 = ds2.GetRasterBand(1)
    band3 = ds3.GetRasterBand(1)
    band4 = ds4.GetRasterBand(1)
    band5 = ds5.GetRasterBand(1)
    band6 = ds6.GetRasterBand(1)

    data1 = BandReadAsArray(band1)
    data2 = BandReadAsArray(band2)
    data3 = BandReadAsArray(band3)
    data4 = BandReadAsArray(band4)
    data5 = BandReadAsArray(band5)
    data6 = BandReadAsArray(band6)

    dataOut = numpy.sqrt(data1 + data2 + data3 + data4 + data5 + data6)

    #Write the out file
    driver = gdal.GetDriverByName(ras_type)
    dsOut = driver.Create(path_out, ds1.RasterXSize, ds1.RasterYSize, 1, band1.DataType)
    CopyDatasetInfo(ds1, dsOut)
    bandOut = dsOut.GetRasterBand(1)
    BandWriteArray(bandOut, dataOut)


def oldsumsixraster(rl1, rl2, rl3, rl4, rl5, rl6, path_out, ras_type="GTiff"):
    inp = rl1, rl2, rl3, rl4, rl5, rl6
    elements = []
    list_name = []
    rast_ent = []

    for elem in inp:
        rast_ent.append(open_raster(elem))

    for i in range(0, 6):
        a = QgsRasterCalculatorEntry()
        a.ref = rast_ent[i][0]
        print(a.ref)
        a.raster = rast_ent[i][1]
        print(a.raster)
        a.bandNumber = 1
        print(a.bandNumber)
        list_name.append(rast_ent[i][0])
        elements.append(a)

    formula = list_name[0] + " + " + list_name[1] + " + " + list_name[2] + " + " + list_name[3] + " + " + list_name[
        4] + " + " + list_name[5]
    print(formula)
    calc = QgsRasterCalculator(formula, path_out, ras_type, elements[0].raster.extent(), elements[0].raster.width(),
                               elements[0].raster.height(), elements)
    print(calc.processCalculation())
    open_raster(path_out)