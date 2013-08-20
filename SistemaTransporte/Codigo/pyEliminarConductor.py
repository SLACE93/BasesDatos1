
from PyQt4 import QtCore, QtGui, QtSql
from EliminarConductor import Ui_EliminarConductor

class MyformEliminarConductor(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uiECond = Ui_EliminarConductor()
        self.uiECond.setupUi(self)
        self.center()
        
        self.connect(self.uiECond.bRegresarEConductor, QtCore.SIGNAL("clicked()"), self.regresarConductor)
        #self.connect(self.uiECond.bEliminarConductor, QtCore.SIGNAL("clicked()"), self.modificarConductor)

    def setearBotones(self):
        iconReg = QtGui.QIcon()
        iconElim = QtGui.QIcon()
        
        iconReg.addPixmap(QtGui.QPixmap(("imagenes/bregresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiECond.bRegresarEConductor.setIcon(iconReg)
        self.uiECond.bRegresarEConductor.setIconSize(QtCore.QSize(240, 50))
        
        iconElim.addPixmap(QtGui.QPixmap(("imagenes/bingresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiECond.bEliminarConductor.setIcon(iconElim)
        self.uiECond.bEliminarConductor.setIconSize(QtCore.QSize(240, 50))
        
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