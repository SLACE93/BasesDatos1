'''
Created on 27/07/2013

@author: josanvel
'''
from PyQt4 import QtCore, QtGui
from Unidades import Ui_Unidades
import exceptions
class MyformUnidades(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uiU = Ui_Unidades()
        self.uiU.setupUi(self)
        
        self.connect(self.uiU.bRegresarUnidades, QtCore.SIGNAL("clicked()"), self.regresarUnidades)
        self.connect(self.uiU.bingresarUnidades, QtCore.SIGNAL("clicked()"), self.ingresarUnidades)
        
    def regresarVentanaU(self, ventanaAtras):
        self.principal = ventanaAtras
        
    def regresarUnidades(self):
        self.hide()
        self.principal.show()
    
    def ingresarUnidades(self):
        self.matricula = self.uiU.lineEMatricula.displayText()
        self.capacidad = self.uiU.lineECapacidad.displayText()
        self.anoF  = self.uiU.lineEAnoFab.displayText()
        if self.matricula!='' and self.capacidad!='' and self.anoF!='':    
            if self.valMatricula(self.matricula) == False:
                QtGui.QMessageBox.information(self, 'Ingreso erroneo','Numero de matricula incorrecto')
            elif self.toInt(self.capacidad)==None:  
                QtGui.QMessageBox.information(self, 'Ingreso erroneo','El campo capacidad solo admite enteros')
            elif self.toInt(self.anoF)==None:
                QtGui.QMessageBox.information(self, 'Ingreso erroneo','El campo anio fabricacion solo admite enteros')
            '''else: ingreso a la base '''
        else:
            QtGui.QMessageBox.information(self, 'Campos vacios', 'Todos los campos deben contener informacion')
            
            
    def toInt(self,num):
        try:
            return int(num)
        except exceptions.ValueError:
            return None
    
    def valMatricula(self,mat):
        if len(mat)==7 or len(mat)==8:
            if mat[3]=='-':
                a = mat.split('-')
                letras = a[0]
                digitos = a[1]
                if self.toInt(digitos) and self.toInt(letras)==None:
                    return True
            else:
                return False
        else:
            return False
            
        