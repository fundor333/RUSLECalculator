"""
/***************************************************************************
 RUSLECalculator_config
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

import os
import configparser

PLUGIN_NAME = 'RUSLECalculator'
FILEPATH = os.path.expanduser("~") + '/QGis/' + PLUGIN_NAME + "/"
OUTPUT_FORMAT = ".asc"
OUTPUT_NAME = "output"
OUTPUT_TECNOLOGY = "GTiff"
OUTPUT_TEMP = 'temp/'
CONTROL_CONFIG = "Control_specifications"
OUTPUT_CONFIG = "Output_file"
CONFIG_NAME = 'config.ini'
CONFIG_DIR = FILEPATH + 'config/'
CONFIG_CONFIGURATION = "Config_configuration"

class ConfigurationManager:
    def __init__(self):
        try:
            self.config = configparser.ConfigParser()
            self.config.sections()
        except Exception:
            self.config = configparser.ConfigParser()
            self.init_config()

    def open(self, path):
        self.config.read(path)

    # TODO bisogna sistemare in base alla nuova gui e alle nuove necessita
    def init_config(self):
        self.config = configparser.ConfigParser()
        self.config.sections()
        self.config[CONTROL_CONFIG] = {'Slope_threhold': '0',
                                       'Maximum_slope_lenght': '0',
                                       'Maximum_slope_metric': 'true',
                                       'Average_soil_factory_patcher': 'false',
                                       'Aspect_threshold': '0',
                                       'Smallest_patch_size': '0'}
        self.config[OUTPUT_CONFIG] = {'Output_directory': FILEPATH,
                                      'Output_file_name': OUTPUT_NAME,
                                      'Output_file_type': OUTPUT_FORMAT,
                                      'Output_temp': CONFIG_DIR + OUTPUT_TEMP}
        self.config[CONFIG_CONFIGURATION] = {'Config_path': CONFIG_DIR + CONFIG_NAME,
                                      'Config_file_name': CONFIG_NAME,
                                      'Config_dir': CONFIG_DIR}

    def save(self):
        if not os.path.exists(self.read_config(OUTPUT_CONFIG, 'Output_directory')):
            os.makedirs(self.read_config(OUTPUT_CONFIG, 'Output_directory'))
        if not os.path.exists(self.read_config(CONFIG_CONFIGURATION, 'Config_dir')):
            os.makedirs(self.read_config(CONFIG_CONFIGURATION, 'Config_dir'))
        with open(self.read_config(CONFIG_CONFIGURATION, 'Config_path'), 'w') as configfile:
            self.config.write(configfile)

    def read_config(self, section, config):
        try:
            return self.config[section][config]
        except KeyError:
            self.init_config()
            return self.config[section][config]

    def edit_config(self, section, config, data):
        try:
            self.config.sections()
            self.config.read(self.config[CONFIG_CONFIGURATION]['Config_path'])
            self.config.set(section, config, str(data))
            return data
        except KeyError:
            self.init_config()
            self.edit_config(section, config, data)


CONFIG_OBJECT = ConfigurationManager()

if __name__ == '__main__':
    CONFIG_OBJECT.save()
