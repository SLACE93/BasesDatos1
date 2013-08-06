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
        self.setearBotones()
        
        self.connect(self.uiRH.bRegresarHoras, QtCore.SIGNAL("clicked()"), self.regresarHora)

    def setearBotones(self):
        iconReg = QtGui.QIcon()
        iconCons = QtGui.QIcon()
        
        iconReg.addPixmap(QtGui.QPixmap(("imagenes/bregresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiRH.bRegresarHoras.setIcon(iconReg)
        self.uiRH.bRegresarHoras.setIconSize(QtCore.QSize(240, 50))
        
        iconCons.addPixmap(QtGui.QPixmap(("imagenes/bingresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiRH.bConsultarHoras.setIcon(iconCons)
        self.uiRH.bConsultarHoras.setIconSize(QtCore.QSize(240, 50))
        
    def regresarVentanaH(self, ventana):
        self.principal = ventana
    
    def regresarHora(self):
        self.hide()
        self.principal.show()