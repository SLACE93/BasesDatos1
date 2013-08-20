
from PyQt4 import QtCore, QtGui, QtSql
from ModificarRecorrido import Ui_ModificarRecorrido

class MyformModificarRecorrido(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uiMRec = Ui_ModificarRecorrido()
        self.uiMRec.setupUi(self)
        self.center()
        
        self.connect(self.uiMRec.bRegresarRecorrido, QtCore.SIGNAL("clicked()"), self.regresarRecorrido)
        #self.connect(self.uiMRec.bModificarRecorrido, QtCore.SIGNAL("clicked()"), self.modificarConductor)

    def setearBotones(self):
        iconReg = QtGui.QIcon()
        iconMod = QtGui.QIcon()
        
        iconReg.addPixmap(QtGui.QPixmap(("imagenes/bregresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiMRec.bRegresarRecorrido.setIcon(iconReg)
        self.uiMRec.bRegresarRecorrido.setIconSize(QtCore.QSize(240, 50))
        
        iconMod.addPixmap(QtGui.QPixmap(("imagenes/bingresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiMRec.bModificarRecorrido.setIcon(iconMod)
        self.uiMRec.bModificarRecorrido.setIconSize(QtCore.QSize(240, 50))
        
    def regresarVentana(self, ventana):
        self.principal = ventana
        
    def regresarRecorrido(self):
        self.hide()
        self.principal.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())