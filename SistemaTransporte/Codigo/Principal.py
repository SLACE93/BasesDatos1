'''
Created on 09/07/2013

@author: josanvel
'''
import sys
from PyQt4 import QtGui
from pyVentanaPrincipal import pyVentanaP

def main():
    aplicacion = QtGui.QApplication(sys.argv)
    ventana = pyVentanaP()
    ventana.show()
    sys.exit(aplicacion.exec_())

if __name__ == '__main__':
    main()