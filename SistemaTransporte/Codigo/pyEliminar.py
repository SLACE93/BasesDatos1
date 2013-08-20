'''
Created on 27/07/2013

@author: josanvel
'''

from PyQt4 import QtCore, QtGui
from Eliminar import Ui_Eliminar
from pyEliminarConductor import MyformEliminarConductor
from pyEliminarRecorrido import MyformEliminarRecorrido
from pyEliminarUnidad import MyformEliminarUnidad

class MyformEliminar(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uiEliminar = Ui_Eliminar()
        self.uiEliminar.setupUi(self)
        self.center()
        #self.setearBotones()
        
        self.connect(self.uiEliminar.bRegresarEliminar, QtCore.SIGNAL("clicked()"), self.funcionRegresarEliminar)
        self.connect(self.uiEliminar.bEliminarConductor, QtCore.SIGNAL("clicked()"), self.entrarEliminarConductor)
        self.connect(self.uiEliminar.bEliminarUnidad, QtCore.SIGNAL("clicked()"), self.entrarEliminarUnidad)
        self.connect(self.uiEliminar.bEliminarRecorrido, QtCore.SIGNAL("clicked()"), self.entrarEliminarRecorrido)


    def setearBotones(self):
        iconReg = QtGui.QIcon()
        iconCond = QtGui.QIcon()
        iconUnid = QtGui.QIcon()
        iconRec = QtGui.QIcon()
        
        iconReg.addPixmap(QtGui.QPixmap(("imagenes/bregresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiEliminar.bRegresarEliminar.setIcon(iconReg)
        self.uiEliminar.bRegresarEliminar.setIconSize(QtCore.QSize(240, 50))
        
        iconCond.addPixmap(QtGui.QPixmap(("imagenes/bporconductor.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiEliminar.bEliminarConductor.setIcon(iconCond)
        self.uiEliminar.bEliminarConductor.setIconSize(QtCore.QSize(450, 50))
        
        iconUnid.addPixmap(QtGui.QPixmap(("imagenes/bporfecha.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiEliminar.bEliminarUnidad.setIcon(iconUnid)
        self.uiEliminar.bEliminarUnidad.setIconSize(QtCore.QSize(450, 50))
        
        iconRec.addPixmap(QtGui.QPixmap(("imagenes/bporhora.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiEliminar.bEliminarRecorrido.setIcon(iconRec)
        self.uiEliminar.bEliminarRecorrido.setIconSize(QtCore.QSize(450, 50))
        
        
    def regresarVentanaEliminar(self, ventanaAtras):
        self.principal = ventanaAtras
    
    def funcionRegresarEliminar(self):
        self.hide()
        self.principal.show()
    
    def entrarEliminarConductor(self):
        self.hide()
        self.eliminarConductor = MyformEliminarConductor()
        self.eliminarConductor.regresarVentana(self)
        self.eliminarConductor.show()
        
    def entrarEliminarUnidad(self):
        self.hide()
        self.eliminarUnidad = MyformEliminarUnidad()
        self.eliminarUnidad.regresarVentana(self)
        self.eliminarUnidad.show()
        
    def entrarEliminarRecorrido(self):
        self.hide()
        self.eliminarRecorrido = MyformEliminarRecorrido()
        self.eliminarRecorrido.regresarVentana(self)
        self.eliminarRecorrido.show()
        
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())