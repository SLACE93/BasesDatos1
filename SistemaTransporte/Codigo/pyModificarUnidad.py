
from PyQt4 import QtCore, QtGui, QtSql
from ModificarUnidad import Ui_ModificarUnidad

class MyformModificarUnidad(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uiMUnidad = Ui_ModificarUnidad()
        self.uiMUnidad.setupUi(self)
        self.center()
        
        self.connect(self.uiMUnidad.bRegresarUnidad, QtCore.SIGNAL("clicked()"), self.regresarUnidad)
        #self.connect(self.uiMUnidad.bModificarUnidad, QtCore.SIGNAL("clicked()"), self.modificarConductor)

    def setearBotones(self):
        iconReg = QtGui.QIcon()
        iconMod = QtGui.QIcon()
        
        iconReg.addPixmap(QtGui.QPixmap(("imagenes/bregresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiMUnidad.bRegresarUnidad.setIcon(iconReg)
        self.uiMUnidad.bRegresarUnidad.setIconSize(QtCore.QSize(240, 50))
        
        iconMod.addPixmap(QtGui.QPixmap(("imagenes/bingresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiMUnidad.bModificarUnidad.setIcon(iconMod)
        self.uiMUnidad.bModificarUnidad.setIconSize(QtCore.QSize(240, 50))
        
    def regresarVentana(self, ventana):
        self.principal = ventana
        
    def regresarUnidad(self):
        self.hide()
        self.principal.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())