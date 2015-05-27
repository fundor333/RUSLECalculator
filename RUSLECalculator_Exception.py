"""
/***************************************************************************
 RUSLECalculator_Exception
                                 A QGIS plugin
 Plugin
                             -------------------
        begin                : 2015-03-12
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Matteo Scarpa
        email                : matteoscarpa92@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""


class NoDem(Exception):
    def __init__(self, message):
        self.message = message


class NoFieldImage(Exception):
    def __init__(self, message):
        self.message = message


class RasterError(Exception):
    def __init__(self, message):
        self.message = message


class RError(Exception):
    def __init__(self, message):
        self.message = message


class AlphaError(Exception):
    def __init__(self, message):
        self.message = message


class LSError(Exception):
    def __init__(self, message):
        self.message = message


class CError(Exception):
    def __init__(self, message):
        self.message = message


class KError(Exception):
    def __init__(self, message):
        self.message = message


