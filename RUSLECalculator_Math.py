from RUSLECalculator_lib import open_raster
from osgeo.gdalnumeric import *
from osgeo.gdalconst import *
import math


def rastermath(dem, fieldimage, k, r, p, c, path_out, flowacc, cell_size, pend, ras_type="GTiff"):
    rl = dem, fieldimage, k, r, p, c
    ds = range(0, 6)
    band = range(0, 6)
    data = range(0, 6)

    for i in range(0, 6):
        open_raster(rl[i])
        ds[i] = gdal.Open(rl[1], GA_ReadOnly)
        band[i] = ds[i].GetRasterBand(1)
        data[i] = BandReadAsArray(band[i])

    ls = calc_ls(flowacc, cell_size, pend)

    dataOut = numpy.sqrt(data[2] * data[3] * data[4] * data[5] * ls)

    # Write the out file
    driver = gdal.GetDriverByName(ras_type)
    dsOut = driver.Create(path_out, k.RasterXSize, k.RasterYSize, 1, k.GetRasterBand(1).DataType)
    CopyDatasetInfo(k, dsOut)
    bandOut = dsOut.GetRasterBand(1)
    BandWriteArray(bandOut, dataOut)


def calc_ls(flowacc, cell_size, pend):
    return ((flowacc * cell_size / 22.13) ** 0.4) * (-1.5 + 17 / 1 + (math.e ** (2.3 - 6.1 * math.sin(pend))))