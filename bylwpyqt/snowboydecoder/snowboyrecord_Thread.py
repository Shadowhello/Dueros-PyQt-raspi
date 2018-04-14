from PyQt5 import QtCore,QtGui
import time

class snowboyThread(QtCore.QThread):

    def __init__(self,parent=None):
        super(snowboyThread,self).__init__(parent)

    sinout = QtCore.pyqtSignal(str)
    def run(self):
        import snowboydecoder.my_decoder as mydecoder
        mydecoder.detected_callback()

        pass
