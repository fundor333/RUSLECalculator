import configparser
import os
from MatrixModule_resurce import *

__author__ = 'Fundor333'


class Configuration():
    def __init__(self):
        try:
            self.config = configparser.ConfigParser()
            self.config.sections()
            self.config.read(CONTROL_CONFIG)
        except Exception:
            self.config = configparser.ConfigParser()
            self.init_config()

    def init_config(self):
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
        self.config[CONFIG_CONFIG] = {'Config_path': CONFIG_PATH}

    def save(self):
        if not os.path.exists(self.config[CONFIG_CONFIG]['Config_path']):
            os.makedirs(self.config[CONFIG_CONFIG]['Config_path'])
        if not os.path.exists(self.config[OUTPUT_CONFIG]['Output_directory']):
            os.makedirs(self.config[CONTROL_CONFIG]['Output_directory'])
        with open(self.config[CONTROL_CONFIG]['Config_path'] + PLUGINNAME, 'w') as configfile:
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
            data.read(self.config[CONTROL_CONFIG]['Config folder'] + PLUGINNAME)
            data.set(section, config, data)
        except KeyError:
            self.init_config()
            self.edit_config(section, config, data)

# TODO: Non genera le cartelle richieste
if __name__ == '__main__':
    print(CONFIG_PATH)
    m = Configuration().init_config()