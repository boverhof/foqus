#
# John Eslick, 2013
# Copyright Carnegie Mellon University
#
#from PySide import QtCore, QtGui
#from optMessageWindow_UI import *

from PyQt5 import QtCore, QtGui
import os
from PyQt5 import uic
mypath = os.path.dirname(__file__)
_optMessageWindowUI, _optMessageWindow = \
        uic.loadUiType(os.path.join(mypath, "optMessageWindow_UI.ui"))
#super(, self).__init__(parent=parent)

class optMessageWindow(_optMessageWindow, _optMessageWindowUI):
    def __init__(self, parent=None):
        '''
        Constructor for optimization message window
        '''
        super(optMessageWindow, self).__init__(parent=parent)
        self.setupUi(self) # Create the widgets

        def closeEvent(self, e):
            e.ignore()

        def clearMessages(self):
            self.msgTextBrowser.clear()
