# -*- coding: utf-8 -*-
"""
/***************************************************************************
 RUSLECalculator
                                 A QGIS plugin
 Plugin
                             -------------------
        begin                : 2015-03-12
        copyright            : (C) 2015 by Matteo Scarpa
        email                : matteoscarpa92@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    from .RUSLECalculator import RUSLECalculator

    return RUSLECalculator(iface)
