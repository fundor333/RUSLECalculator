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


class NoDem(Exception):
    def __init__(self, message=""):
        self.message = message
        LOG.e("NoDem " + message)


class NoFieldImage(Exception):
    def __init__(self, message=""):
        self.message = message
        LOG.e("NoFieldImage " + message)


class PError(Exception):
    def __init__(self, message=""):
        self.message = message
        LOG.e("PError " + message)


class RasterError(Exception):
    def __init__(self, message=""):
        self.message = message
        LOG.e("RasterError " + message)


class RError(Exception):
    def __init__(self, message=""):
        self.message = message
        LOG.e("RError " + message)


class AlphaError(Exception):
    def __init__(self, message=""):
        self.message = message
        LOG.e("AlphaError " + message)


class LSError(Exception):
    def __init__(self, message=""):
        self.message = message
        LOG.e("LSError " + message)


class CError(Exception):
    def __init__(self, message=""):
        self.message = message
        LOG.e("CError " + message)


class KError(Exception):
    def __init__(self, message=""):
        self.message = message
        LOG.e("KError " + message)


class OutError(Exception):
    def __init__(self, message=""):
        self.message = message
        LOG.e("OutError " + message)


class Log():
    def __init__(self, filename=None):
        if filename is None:
            logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        else:
            logging.basicConfig(filename=filename, level=logging.DEBUG,
                                format='%(asctime)s - %(levelname)s - %(message)s')

    def c(self, string, dlg=None):
        if dlg is not None:
            error_window(dlg, "Critical", string)
        logging.critical(string)
        print(string)

    def e(self, string, dlg=None):
        if dlg is not None:
            error_window(dlg, "Error", string)
        logging.error(string)
        print(string)

    def w(self, string):
        logging.warning(string)
        print(string)

    def i(self, string):
        logging.info(string)
        print(string)

    def d(self, string):
        logging.debug(string)
        print(string)


LOG = Log("/var/tmp/RUSLECalculator.log")


def error_window(dlg, title, body):
    QMessageBox.information(dlg, dlg.tr(title), dlg.tr(body), "")
