'''
Created on 27/07/2013

@author: josanvel
'''
from PyQt4 import QtCore, QtGui
from Conductor import Ui_Conductor
import exceptions

class MyformConductor(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uiCond = Ui_Conductor()
        self.uiCond.setupUi(self)
        
        self.connect(self.uiCond.bRegresarConductores, QtCore.SIGNAL("clicked()"),self.regresarConductor)
        self.connect(self.uiCond.bingresarConductores, QtCore.SIGNAL("clicked()"),self.ingresarConductor)
        
    def regresarVentanaCond(self, ventanaAtras):
        self.ventana = ventanaAtras
        
    def regresarConductor(self):
        self.hide()
        self.ventana.show()
    
    def ingresarConductor(self):
        self.cedula = self.uiCond.lineEIDCedula.displayText()
        self.licencia = self.uiCond.lineENLicencia.displayText()
        self.nombre = self.uiCond.lineENombre.displayText()
        if self.cedula!='' and self.licencia!='' and self.nombre!='':    
            if len(self.cedula) != 10:
                QtGui.QMessageBox.information(self, 'Ingreso erroneo','Numero de cedula incorrecto')
            elif self.toInt(self.cedula)==None:  
                QtGui.QMessageBox.information(self, 'Ingreso erroneo','Numero de cedula incorrecto')
            elif len(self.licencia) != 10:
                QtGui.QMessageBox.information(self, 'Ingreso erroneo','Numero de licencia incorrecto')
            elif self.toInt(self.licencia)==None:
                QtGui.QMessageBox.information(self, 'Ingreso erroneo','Numero de licencia incorrecta')
            elif self.toInt(self.nombre):
                QtGui.QMessageBox.information(self, 'Ingreso erroneo','Nombre incorrecto')
            '''else: ingreso a la base '''
        else:
            QtGui.QMessageBox.information(self, 'Campos vacios', 'Todos los campos deben contener informacion')
            
            
    def toInt(self,num):
        try:
            return int(num)
        except exceptions.ValueError:
            return None

        