from RUSLECalculator_Exception import RasterError  # NoDem, NoFieldImage
from RUSLECalculator_lib import open_raster
from osgeo.gdalnumeric import *
from osgeo.gdalconst import *
import math


def rastermath(dem, fieldimage, k, r, ls, c, p, rasterxsize, rasterysize, datatype, path_out, ras_type="GTiff"):
    dataOut = numpy.sqrt(k * r * ls * c * p)

    # Write the out file
    driver = gdal.GetDriverByName(ras_type)
    dsOut = driver.Create(path_out, rasterxsize, rasterysize, 1, datatype)
    CopyDatasetInfo(k, dsOut)
    bandOut = dsOut.GetRasterBand(1)
    BandWriteArray(bandOut, dataOut)


def calc_p(p_value):
    raise NotImplemented

def calc_ls(flowacc, cell_size, pend):
    return ((flowacc * cell_size / 22.13) ** 0.4) * (-1.5 + 17 / 1 + (math.e ** (2.3 - 6.1 * math.sin(pend))))