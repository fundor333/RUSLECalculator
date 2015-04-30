import gdal
from osgeo.gdal_array import BandReadAsArray
from osgeo.gdalconst import GA_ReadOnly
from PyQt4.QtCore import QFileInfo
import configparser
import os

from qgis.core import QgsMapLayerRegistry, QgsRasterLayer
from RUSLECalculator_resurce import CONFIG_CONFIG, CONTROL_CONFIG, OUTPUT_CONFIG, FILEPATH, OUTPUT_NAME, OUTPUT_FORMAT, \
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


def open_raster(filename):
    basename = QFileInfo(filename).baseName()
    r_layer = QgsRasterLayer(filename, basename)
    if not r_layer.isValid():
        print("Layer failed to load!")
    else:
        QgsMapLayerRegistry.instance().addMapLayer(r_layer)
        print("Layer loaded")
    return basename, r_layer


def name_opener(element):
    open_raster(element)
    ds = gdal.Open(element, GA_ReadOnly)
    band = ds.GetRasterBand(1)
    data = BandReadAsArray(band)
    return data


CONFIG_OBJECT = ConfigurationManager()