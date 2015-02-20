__author__ = 'Fundor333'

import os

os.system('pyrcc4 -o resources.py resources.qrc')
os.system('pyuic4 -o form.py form.ui')