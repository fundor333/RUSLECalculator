"""
/***************************************************************************
 RUSLECalculator_error
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

import logging
from PyQt4.QtGui import QMessageBox
from RUSLECalculator_config import PLUGIN_NAME


class NoDem(Exception):
    def __init__(self, message=""):
        self.message = message
        LOGGER.error("NoDem " + message)


class NoFieldImage(Exception):
    def __init__(self, message=""):
        self.message = message
        LOGGER.error("NoFieldImage " + message)


class PError(Exception):
    def __init__(self, message=""):
        self.message = message
        LOGGER.error("PError " + message)


class RasterError(Exception):
    def __init__(self, message=""):
        self.message = message
        LOGGER.error("RasterError " + message)


class RError(Exception):
    def __init__(self, message=""):
        self.message = message
        LOGGER.error("RError " + message)


class AlphaError(Exception):
    def __init__(self, message=""):
        self.message = message
        LOGGER.error("AlphaError " + message)


class LSError(Exception):
    def __init__(self, message=""):
        self.message = message
        LOGGER.error("LSError " + message)


class CError(Exception):
    def __init__(self, message=""):
        self.message = message
        LOGGER.error("CError " + message)


class KError(Exception):
    def __init__(self, message=""):
        self.message = message
        LOGGER.error("KError " + message)


class OutError(Exception):
    def __init__(self, message=""):
        self.message = message
        LOGGER.error("OutError " + message)


class MyLogger():
    def __init__(self, filename=None):
        if filename is None:
            logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        else:
            logging.basicConfig(filename=filename, level=logging.DEBUG,
                                format='%(asctime)s - %(levelname)s - %(message)s')

    def critical(self, string, dlg=None):
        if dlg is not None:
            error_window(dlg, "Critical", string)
        logging.critical(string)
        print(string)

    def error(self, string, dlg=None):
        if dlg is not None:
            error_window(dlg, "Error", string)
        logging.error(string)
        print(string)

    def warning(self, string):
        logging.warning(string)
        print(string)

    def info(self, string):
        logging.info(string)
        print(string)

    def debug(self, string):
        logging.debug(string)
        print(string)


LOGGER = MyLogger("/var/tmp/" + PLUGIN_NAME + ".log")


def error_window(dlg, title, body):
    QMessageBox.information(dlg, dlg.tr(title), dlg.tr(body), "")
