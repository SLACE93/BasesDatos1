'''
Created on 27/07/2013

@author: josanvel
'''

from PyQt4 import QtCore, QtGui
from Recorridos import Ui_Recorridos
import exceptions

class MyformRecorridos(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uiR = Ui_Recorridos()
        self.uiR.setupUi(self)
        self.connect(self.uiR.bRegresarRecorridos, QtCore.SIGNAL("clicked()"), self.regresarRecorrido)
        self.connect(self.uiR.bingresarRecorridos, QtCore.SIGNAL("clicked()"), self.ingresarRecorrido)
        
    def regresarVentanaR(self,ventanaAtras):
        self.ventana = ventanaAtras
    
    def regresarRecorrido(self):
        self.hide()
        self.ventana.show()
    
    def ingresarRecorrido(self):
        self.numPasajeros = self.uiR.lineEPasajeros.displayText()
        self.idCond = self.uiR.lineEIDConductor.displayText()
        self.idUni = self.uiR.lineEIDUnidad.displayText()
        if self.uiR.lineEIDConductor.displayText()!='' and self.uiR.lineEIDUnidad.displayText()!='' and self.uiR.lineEPasajeros!='':    
            if self.toInt(self.idCond) == None:
                QtGui.QMessageBox.information(self, 'Ingreso erroneo','Solo se admite enteros en el campo ID Conductor')
            elif self.toInt(self.idUni) == None:
                QtGui.QMessageBox.information(self, 'Ingreso erroneo','Solo se admite enteros en el campo ID Unidad')
            elif self.toInt(self.numPasajeros) == None:
                QtGui.QMessageBox.information(self, 'Ingreso erroneo','Solo se admite enteros en el campo de num Pasajeros')
            '''else: ingreso a la base '''
    
                
                
        else:
            QtGui.QMessageBox.information(self, 'Campos vacios', 'Todos los campos deben contener informacion')
            
            
    def toInt(self,num):
        try:
            return int(num)
        except exceptions.ValueError:
            return None
        
        

        