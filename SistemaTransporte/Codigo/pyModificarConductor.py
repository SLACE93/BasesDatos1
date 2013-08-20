'''
Created on 27/07/2013

@author: josanvel
'''

from PyQt4 import QtCore, QtGui, QtSql
from ModificarConductor import Ui_ModificarConductor

class MyformModificarConductor(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uiMCond = Ui_ModificarConductor()
        self.uiMCond.setupUi(self)
        self.center()
        
        self.connect(self.uiMCond.bRegresarConductor, QtCore.SIGNAL("clicked()"), self.regresarConductor)
        #self.connect(self.uiMCond.bModificarConductor, QtCore.SIGNAL("clicked()"), self.modificarConductor)

    def setearBotones(self):
        iconReg = QtGui.QIcon()
        iconMod = QtGui.QIcon()
        
        iconReg.addPixmap(QtGui.QPixmap(("imagenes/bregresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiMCond.bRegresarConductor.setIcon(iconReg)
        self.uiMCond.bRegresarConductor.setIconSize(QtCore.QSize(240, 50))
        
        iconMod.addPixmap(QtGui.QPixmap(("imagenes/bingresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiMCond.bModificarConductor.setIcon(iconMod)
        self.uiMCond.bModificarConductor.setIconSize(QtCore.QSize(240, 50))
        
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
    

        
    
        