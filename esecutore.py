__author__ = 'Fundor333'

import os

os.system('pyrcc4 -o resources_rc.py resources.qrc')
os.system('pyuic4 -o TestModule_dialog.py TestModule_dialog.ui')