# import configparser
import os

from qgis.core import QgsMapLayerRegistry, QgsRasterLayer

from PyQt4.QtCore import QFileInfo

'''
from MatrixModule_resurce import CONFIG_CONFIG, CONTROL_CONFIG, OUTPUT_CONFIG, FILEPATH, OUTPUT_NAME, OUTPUT_FORMAT, \
    CONFIG_PATH, CONFIG_NAME

class Configuration():
    def __init__(self):
        try:
            self.config = configparser.ConfigParser()
            self.config.sections()
            print(self.config[CONTROL_CONFIG])
        except Exception:
            self.config = configparser.ConfigParser()
            self.init_config()

    def init_config(self):
        self.config = configparser.ConfigParser()
        self.config.sections()
        self.config[CONTROL_CONFIG] = {'Slope_threhold': '0',
                                       'Maximum_slope_lenght': '0',
                                       'Maximum_slope_unit': 'metric',
                                       'Rounded_to': 'shorter',
                                       'Average_soil_factory_patcher': 'false',
                                       'Aspect_threshold': '0',
                                       'Smallest_patch_size': '0',
                                       'Default_background_value': '0'}
        self.config[OUTPUT_CONFIG] = {'Output_directory': FILEPATH,
                                      'Output_file_name': OUTPUT_NAME,
                                      'Output_file_type': OUTPUT_FORMAT}
        self.config[CONFIG_CONFIG] = {'Config_path': CONFIG_PATH,
                                      'Config_file_name': CONFIG_NAME}

    def save(self):
        if not os.path.exists(self.config[OUTPUT_CONFIG]['Output_directory']):
            os.makedirs(self.config[OUTPUT_CONFIG]['Output_directory'])
        if not os.path.exists(self.config[CONFIG_CONFIG]['Config_path']):
            os.makedirs(self.config[CONFIG_CONFIG]['Config_path'])
        with open(self.config[CONFIG_CONFIG]['Config_path'],
                  'w') as configfile:
            self.config.write(configfile)

    def read_config(self, section, config):
        try:
            print(self.config[section][config])
            return self.config[section][config]
        except KeyError:
            self.init_config()
            return self.config[section][config]

    def edit_config(self, section, config, data):
        try:
            data = configparser.ConfigParser()
            data.sections()
            data.read(self.config['DEFAULT']['Config folder'] + '/' + CONFIG_NAME)
            data.set(section, config, data)
        except KeyError:
            self.init_config()
            self.edit_config(section, config, data)
'''


def open_raster(filename):
    basename = QFileInfo(filename).baseName()
    r_layer = QgsRasterLayer(filename, basename)
    if not r_layer.isValid():
        print("Layer failed to load!")
    else:
        QgsMapLayerRegistry.instance().addMapLayer(r_layer)
        print("Layer loaded")
        print(basename)
    return basename,r_layer

