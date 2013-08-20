'''
Created on 27/07/2013

@author: josanvel
'''


from PyQt4 import QtCore, QtGui, QtSql
from EliminarUnidad import Ui_EliminarUnidad

class MyformEliminarUnidad(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uiEUnidad = Ui_EliminarUnidad()
        self.uiEUnidad.setupUi(self)
        self.center()
        
        self.connect(self.uiEUnidad.bRegresarEUnidad, QtCore.SIGNAL("clicked()"), self.regresarConductor)
        #self.connect(self.uiEUnidad.bEliminarUnidad, QtCore.SIGNAL("clicked()"), self.modificarConductor)

    def setearBotones(self):
        iconReg = QtGui.QIcon()
        iconElim = QtGui.QIcon()
        
        iconReg.addPixmap(QtGui.QPixmap(("imagenes/bregresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiEUnidad.bRegresarEUnidad.setIcon(iconReg)
        self.uiEUnidad.bRegresarEUnidad.setIconSize(QtCore.QSize(240, 50))
        
        iconElim.addPixmap(QtGui.QPixmap(("imagenes/bingresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiEUnidad.bEliminarUnidad.setIcon(iconElim)
        self.uiEUnidad.bEliminarUnidad.setIconSize(QtCore.QSize(240, 50))
        
    def regresarVentana(self, ventana):
        self.principal = ventana
        
    def regresarConductor(self):
        self.hide()
        self.principal.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())