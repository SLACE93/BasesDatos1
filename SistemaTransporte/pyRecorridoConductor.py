'''
Created on 27/07/2013

@author: josanvel
'''

from PyQt4 import QtCore, QtGui
from RecorridoConductor import Ui_RecorridoConductor
import exceptions

class MyformRecorridoConductor(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uiRCond = Ui_RecorridoConductor()
        self.uiRCond.setupUi(self)
        
        self.connect(self.uiRCond.bRegresarConductor, QtCore.SIGNAL("clicked()"), self.regresarConductor)
        self.connect(self.uiRCond.bConsultarConductor, QtCore.SIGNAL("clicked()"), self.consultarRecorridoCond)
        
    def regresarVentana(self, ventana):
        self.principal = ventana
        
    def regresarConductor(self):
        self.hide()
        self.principal.show()
    
    def consultarRecorridoCond(self):
        self.idRCond = self.uiRCond.lineIDConductorRC.displayText()
        if(self.idRCond !=''):
            if self.toInt(self.idRCond) == None:
                QtGui.QMessageBox.information(self, 'Ingreso erroneo','Solo se admite enteros en el campo de ID Conductor')
            '''else: ingreso a la base '''
        else:
            QtGui.QMessageBox.information(self, 'Campos vacios', 'Todos los campos deben contener informacion')
    
        
    def toInt(self,num):
        try:
            return int(num)
        except exceptions.ValueError:
            return None
        
            
        
    
        