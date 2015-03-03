import numpy
from random import randint
from QGisLib import sumsixraster

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


def run(dlg):
    array = []
    if array.__sizeof__() != 6:
        print("The program need 6 raster to work correctly")
    else:

        array = []
        sumsixraster(array[0], array[1], array[2], array[3], array[4], array[5], FILEPATH + "temp7" + FILETYPE)

    print("Ended")
