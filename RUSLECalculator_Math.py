from RUSLECalculator_lib import open_raster
from osgeo.gdalnumeric import *
from osgeo.gdalconst import *


def rastermath(rl1, rl2, rl3, rl4, rl5, rl6, path_out, ras_type="GTiff"):
    rl = rl1, rl2, rl3, rl4, rl5, rl6
    ds = range(0, 6)
    band = range(0, 6)
    data = range(0, 6)

    for i in range(0, 6):
        open_raster(rl[i])
        ds[i] = gdal.Open(rl[1], GA_ReadOnly)
        band[i] = ds[i].GetRasterBand(1)
        data[i] = BandReadAsArray(band[i])

    dataOut = numpy.sqrt(data[0] + data[1] + data[2] + data[3] + data[4] + data[5])

    # Write the out file
    driver = gdal.GetDriverByName(ras_type)
    dsOut = driver.Create(path_out, ds[0].RasterXSize, ds[0].RasterYSize, 1, band[0].DataType)
    CopyDatasetInfo(ds[0], dsOut)
    bandOut = dsOut.GetRasterBand(1)
    BandWriteArray(bandOut, dataOut)
