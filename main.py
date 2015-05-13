# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui, uic
import sys

def main ():
    """ Function doc """    
    app = QtGui.QApplication(sys.argv)
    window = uic.loadUi("ui/mainwindow.ui") 
    #QtCore.QObject.connect(window.pushButton,QtCore.SIGNAL("clicked()"),generate)
    
    
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
	main()
