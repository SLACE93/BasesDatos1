'''
Created on 27/07/2013

@author: josanvel
'''

from PyQt4 import QtCore, QtGui
from Consultas import Ui_Consultas
from pyRecorridoConductor import MyformRecorridoConductor
from pyRecorridoHora import MyformRecorridoHoras
from pyRecorridoFecha import MyformRecorridoFecha
from pyRecorridoUnidad import MyformRecorridoUnidad

class MyformConsultas(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uiCons = Ui_Consultas()
        self.uiCons.setupUi(self)
        self.center()
        self.setearBotones()
        
        self.connect(self.uiCons.bRegresar, QtCore.SIGNAL("clicked()"), self.funcionRegresarConsultas)
        self.connect(self.uiCons.bRecorridoConductor, QtCore.SIGNAL("clicked()"), self.entrarRecorridoConductor)
        self.connect(self.uiCons.bRecorridoFecha, QtCore.SIGNAL("clicked()"), self.entrarRecorridoFecha)
        self.connect(self.uiCons.bRecorridoHoras, QtCore.SIGNAL("clicked()"), self.entrarRecorridoHora)
        self.connect(self.uiCons.RecorridoUnidad, QtCore.SIGNAL("clicked()"), self.entrarRecorridoUnidad)


    def setearBotones(self):
        iconReg = QtGui.QIcon()
        iconCond = QtGui.QIcon()
        iconFech = QtGui.QIcon()
        iconHora = QtGui.QIcon()
        iconUnid = QtGui.QIcon()
        
        iconReg.addPixmap(QtGui.QPixmap(("imagenes/bregresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiCons.bRegresar.setIcon(iconReg)
        self.uiCons.bRegresar.setIconSize(QtCore.QSize(240, 50))
        
        iconCond.addPixmap(QtGui.QPixmap(("imagenes/bporconductor.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiCons.bRecorridoConductor.setIcon(iconCond)
        self.uiCons.bRecorridoConductor.setIconSize(QtCore.QSize(450, 50))
        
        iconFech.addPixmap(QtGui.QPixmap(("imagenes/bporfecha.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiCons.bRecorridoFecha.setIcon(iconFech)
        self.uiCons.bRecorridoFecha.setIconSize(QtCore.QSize(450, 50))
        
        iconHora.addPixmap(QtGui.QPixmap(("imagenes/bporhora.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiCons.bRecorridoHoras.setIcon(iconHora)
        self.uiCons.bRecorridoHoras.setIconSize(QtCore.QSize(450, 50))
        
        iconUnid.addPixmap(QtGui.QPixmap(("imagenes/bporunidad.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiCons.RecorridoUnidad.setIcon(iconUnid)
        self.uiCons.RecorridoUnidad.setIconSize(QtCore.QSize(450, 50))
        
        
    def regresarVentanaCons(self, ventanaAtras):
        self.principal = ventanaAtras
    
    def funcionRegresarConsultas(self):
        self.hide()
        self.principal.show()
    
    def entrarRecorridoConductor(self):
        self.hide()
        self.recorridoCond = MyformRecorridoConductor()
        self.recorridoCond.regresarVentana(self)
        self.recorridoCond.show()
        
    def entrarRecorridoFecha(self):
        self.hide()
        self.recorridoF = MyformRecorridoFecha()
        self.recorridoF.regresarVentanaF(self)
        self.recorridoF.show()
        
    def entrarRecorridoHora(self):
        self.hide()
        self.recorridoH = MyformRecorridoHoras()
        self.recorridoH.regresarVentanaH(self)
        self.recorridoH.show()
    
    def entrarRecorridoUnidad(self):
        self.hide()
        self.recorridoU = MyformRecorridoUnidad()
        self.recorridoU.regresarVentanaU(self)
        self.recorridoU.show()
        
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())