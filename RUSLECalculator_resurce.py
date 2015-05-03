"""
/***************************************************************************
 RUSLECalculator_resource
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
from os.path import expanduser

PLUGINNAME = 'RUSLECalculator'

FILEPATH = expanduser("~") + '/QGis/' + PLUGINNAME + "/"
OUTPUT_FORMAT = ".asc"
OUTPUT_NAME = "output"
OUTPUT_TECNOLOGY = "GTiff"

CONTROL_CONFIG = "Control_specifications"
OUTPUT_CONFIG = "Output_file"
CONFIG_CONFIG = "Config_configuration"

CONFIG_NAME = 'config.ini'
CONFIG_DIR = FILEPATH + 'config/'
CONFIG_PATH = CONFIG_DIR + CONFIG_NAME