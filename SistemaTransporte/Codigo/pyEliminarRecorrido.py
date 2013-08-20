
from PyQt4 import QtCore, QtGui, QtSql
from EliminarRecorrido import Ui_EliminarRecorrido

class MyformEliminarRecorrido(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uiERec = Ui_EliminarRecorrido()
        self.uiERec.setupUi(self)
        self.center()
        
        self.connect(self.uiERec.bRegresarERecorrido, QtCore.SIGNAL("clicked()"), self.regresarConductor)
        #self.connect(self.uiERec.bEliminarConductor, QtCore.SIGNAL("clicked()"), self.modificarConductor)

    def setearBotones(self):
        iconReg = QtGui.QIcon()
        iconElim = QtGui.QIcon()
        
        iconReg.addPixmap(QtGui.QPixmap(("imagenes/bregresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiERec.bRegresarERecorrido.setIcon(iconReg)
        self.uiERec.bRegresarERecorrido.setIconSize(QtCore.QSize(240, 50))
        
        iconElim.addPixmap(QtGui.QPixmap(("imagenes/bingresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiERec.bEliminarRecorrido.setIcon(iconElim)
        self.uiERec.bEliminarRecorrido.setIconSize(QtCore.QSize(240, 50))
        
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