import configparser
import os
from MatrixModule_resurce import *

__author__ = 'Fundor333'


class Configuration():
    def __init__(self,pathdir):
        self.pathdir = pathdir
        try:
            self.config = configparser.ConfigParser()
            self.config.sections()
            self.config.read(MAINCONFIG)
        except Exception:
            self.config = configparser.ConfigParser()
            self.init_config()

    def init_config(self):
        self.config[MAINCONFIG] = {'':''}
        self.save()

    def save(self):
        if not os.path.exists(self.pathdir):
            os.makedirs(self.pathdir)
        if not os.path.exists(self.config[MAINCONFIG]['Download folder'] + '/'):
            os.makedirs(self.config[MAINCONFIG]['Download folder'] + '/')
        with open(self.config[MAINCONFIG]['Config folder'] + '/' + PLUGINNAME, 'w') as configfile:
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
            data.read(self.config[MAINCONFIG]['Config folder'] + '/' + PLUGINNAME)
            data.set(section, config, data)
            self.save()
        except KeyError:
            self.init_config()
            self.edit_config(section, config, data)
            self.save()