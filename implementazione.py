import numpy
from random import randint
from QGisLib import generate_raster, sumsixraster

try:
    from osgeo import *
except:
    import gdal
    import ogr
    import osr

FILEPATH = "/var/tmp/"
FILETYPE = ".asc"
FILENAME = FILEPATH + "temp" + FILETYPE
# TODO User decide the file's name?
TYPEOFRASTER = "GTiff"
# TODO Other type of raster implementation
NODATA = -9999
PROJ = 4326
ORG = (0.0, 0.0)
NUM_BAND = 1


def run(dlg):
    ncols = dlg.widthInput.value()
    nrows = dlg.highInput.value()
    pixsize = dlg.pixsizex.value(), dlg.pixsizey.value()
    if ncols == 0 | nrows == 0:
        print("Problem with the matrix's size")
    else:

        array = []
        for i in range(1, 7):
            matrix = numpy.zeros((ncols, nrows))
            for z in range(0, ncols):
                for j in range(0, nrows):
                    matrix[z][j] = randint(0, 100)
            a = generate_raster(FILEPATH + "temp" + str(i) + FILETYPE, ORG[0], ORG[1], pixsize[0], pixsize[1], matrix,
                                PROJ, NODATA, NUM_BAND, TYPEOFRASTER)
            array.append(a)

        sumsixraster(array[0], array[1], array[2], array[3], array[4], array[5], FILEPATH + "temp7" + FILETYPE)

        print("Ended")
