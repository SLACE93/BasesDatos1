'''
Created on 27/07/2013

@author: josanvel
'''

from PyQt4 import QtCore, QtGui
from Modificar import Ui_Modificar
from pyModificarConductor import MyformModificarConductor
from pyModificarRecorrido import MyformModificarRecorrido
from pyModificarUnidad import MyformModificarUnidad

class MyformModificar(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uiModificar = Ui_Modificar()
        self.uiModificar.setupUi(self)
        self.center()
        #self.setearBotones()
        
        self.connect(self.uiModificar.bRegresar, QtCore.SIGNAL("clicked()"), self.funcionRegresarModificar)
        self.connect(self.uiModificar.bModificarConductor, QtCore.SIGNAL("clicked()"), self.entrarModificarConductor)
        self.connect(self.uiModificar.bModificarUnidad, QtCore.SIGNAL("clicked()"), self.entrarModificarUnidad)
        self.connect(self.uiModificar.bModificarRecorrido, QtCore.SIGNAL("clicked()"), self.entrarModificarRecorrido)


    def setearBotones(self):
        iconReg = QtGui.QIcon()
        iconCond = QtGui.QIcon()
        iconUnid = QtGui.QIcon()
        iconRec = QtGui.QIcon()
        
        iconReg.addPixmap(QtGui.QPixmap(("imagenes/bregresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiModificar.bRegresar.setIcon(iconReg)
        self.uiModificar.bRegresar.setIconSize(QtCore.QSize(240, 50))
        
        iconCond.addPixmap(QtGui.QPixmap(("imagenes/bporconductor.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiModificar.bModificarConductor.setIcon(iconCond)
        self.uiModificar.bModificarConductor.setIconSize(QtCore.QSize(450, 50))
        
        iconUnid.addPixmap(QtGui.QPixmap(("imagenes/bporfecha.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiModificar.bModificarUnidad.setIcon(iconUnid)
        self.uiModificar.bModificarUnidad.setIconSize(QtCore.QSize(450, 50))
        
        iconRec.addPixmap(QtGui.QPixmap(("imagenes/bporhora.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiModificar.bModificarRecorrido.setIcon(iconRec)
        self.uiModificar.bModificarRecorrido.setIconSize(QtCore.QSize(450, 50))
        
        
    def regresarVentanaModificar(self, ventanaAtras):
        self.principal = ventanaAtras
    
    def funcionRegresarModificar(self):
        self.hide()
        self.principal.show()
    
    def entrarModificarConductor(self):
        self.hide()
        self.modificarConductor = MyformModificarConductor()
        self.modificarConductor.regresarVentana(self)
        self.modificarConductor.show()
        
    def entrarModificarUnidad(self):
        self.hide()
        self.modificarUnidad = MyformModificarUnidad()
        self.modificarUnidad.regresarVentana(self)
        self.modificarUnidad.show()
        
    def entrarModificarRecorrido(self):
        self.hide()
        self.modificarRecorrido = MyformModificarRecorrido()
        self.modificarRecorrido.regresarVentana(self)
        self.modificarRecorrido.show()
        
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())