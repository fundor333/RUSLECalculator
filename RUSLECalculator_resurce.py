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