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
from RUSLECalculator_Gui_Implementation import get_raster_name
from RUSLECalculator_resurce import CONTROL_CONFIG, OUTPUT_CONFIG, FILEPATH, OUTPUT_NAME, OUTPUT_FORMAT, CONFIG_CONFIG, \
    CONFIG_PATH, CONFIG_NAME, CONFIG_DIR

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
                                      'Output_file_type': OUTPUT_FORMAT}
        self.config[CONFIG_CONFIG] = {'Config_path': CONFIG_PATH,
                                      'Config_file_name': CONFIG_NAME,
                                      'Config_dir': CONFIG_DIR}

    def save(self):
        if not os.path.exists(self.read_config(OUTPUT_CONFIG, 'Output_directory')):
            os.makedirs(self.read_config(OUTPUT_CONFIG, 'Output_directory'))
        if not os.path.exists(self.read_config(CONFIG_CONFIG, 'Config_dir')):
            os.makedirs(self.read_config(CONFIG_CONFIG, 'Config_dir'))
        with open(self.read_config(CONFIG_CONFIG, 'Config_path'), 'w') as configfile:
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
            self.config.read(self.config[CONFIG_CONFIG]['Config_path'])
            self.config.set(section, config, str(data))
            return data
        except KeyError:
            self.init_config()
            self.edit_config(section, config, data)


CONFIG_OBJECT = ConfigurationManager()


def saveconfig(dlg):
    string_path = get_raster_name(dlg)
    CONFIG_OBJECT.edit_config(CONFIG_CONFIG, 'config_path', string_path)
    CONFIG_OBJECT.edit_config(CONFIG_CONFIG, 'aspect_threshold', dlg.AspectThreshold.value())
    CONFIG_OBJECT.edit_config(CONFIG_CONFIG, 'maximum_slope_lenght', dlg.MaxSlopeLenght.value())
    CONFIG_OBJECT.edit_config(CONFIG_CONFIG, 'maximum_slope_metric', dlg.checkBox.value())
    CONFIG_OBJECT.edit_config(CONFIG_CONFIG, 'average_soil_factory_patcher', dlg.checkBox_3.value())
    CONFIG_OBJECT.edit_config(CONFIG_CONFIG, 'slope_threhold', dlg.SlopeThreshold.value())
    CONFIG_OBJECT.edit_config(CONFIG_CONFIG, 'smallest_patch_size', dlg.SmallestPatchSize.value())
    CONFIG_OBJECT.save()