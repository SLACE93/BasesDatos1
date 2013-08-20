
from PyQt4 import QtCore, QtGui, QtSql
from EliminarConductor import Ui_EliminarConductor

class MyformEliminarConductor(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uiECond = Ui_EliminarConductor()
        self.uiECond.setupUi(self)
        self.center()
        self.setConductores()
        
        self.connect(self.uiECond.bRegresarEConductor, QtCore.SIGNAL("clicked()"), self.regresarConductor)
        self.connect(self.uiECond.bEliminarConductor, QtCore.SIGNAL("clicked()"), self.eliminarConductor)

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

    def setConductores(self):
        lista_Conductores = []
        if not QtSql.QSqlDatabase.database().isOpen():
            if not QtSql.QSqlDatabase.database():
                QtGui.QMessageBox.information(None,'ERROR', 'No se pudo abrir la BASES DE DATOS')
                
        query = QtSql.QSqlQuery("call PRGetConductor")
        fieldNo_Id = query.record().indexOf("IdConductor")
        fieldNo_Ced = query.record().indexOf("Cedula")
        fieldNo_Nom =query.record().indexOf("cNombre")
        
        while query.next():
            idC = query.value(fieldNo_Id).toString()
            cedula = query.value(fieldNo_Ced).toString()
            nombre = query.value(fieldNo_Nom).toString()
            ced_nombre = idC + '-' + cedula + '-' + nombre
            lista_Conductores.append(ced_nombre)
        
        self.uiECond.cboxIDConductor.addItems(lista_Conductores)
    
    def eliminarConductor(self):
        QtGui.QMessageBox.information(None,'Eliminar Conductor', 'Usted esta seguro de ELIMINAR un Conductor')
        idConductor = self.uiECond.cboxIDConductor.currentText()
        lista = idConductor.split("-")
        
        if not QtSql.QSqlDatabase.database().isOpen():
            if not QtSql.QSqlDatabase.database():
                QtGui.QMessageBox.information(None,'ERROR', 'No se pudo abrir la BASES DE DATOS')
        
        model = QtSql.QSqlTableModel(self)
        model.setQuery(QtSql.QSqlQuery("DELETE FROM Conductor Where IdConductor="+lista[0]+";"))
        