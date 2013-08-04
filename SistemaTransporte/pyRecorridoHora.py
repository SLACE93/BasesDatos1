'''
Created on 27/07/2013

@author: josanvel
'''
from PyQt4 import QtCore, QtGui
from RecorridoHora import Ui_RecorridoHoras

class MyformRecorridoHoras(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uiRH = Ui_RecorridoHoras()
        self.uiRH.setupUi(self)
        
        self.connect(self.uiRH.bRegresarHoras, QtCore.SIGNAL("clicked()"), self.regresarHora)
        
    def regresarVentanaH(self, ventana):
        self.principal = ventana
    
    def regresarHora(self):
        self.hide()
        self.principal.show()