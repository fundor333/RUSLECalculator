__author__ = 'Fundor333'

import os

os.system('pyrcc4 -o resources_rc.py resources.qrc')
os.system('pyuic4 -o MatrixModule_dialog_base.py MatrixModule_dialog_base.ui')