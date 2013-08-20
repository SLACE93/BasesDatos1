
from PyQt4 import QtCore, QtGui, QtSql
from EliminarRecorrido import Ui_EliminarRecorrido

class MyformEliminarRecorrido(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uiERec = Ui_EliminarRecorrido()
        self.uiERec.setupUi(self)
        self.center()
        self.setRecorrido()
        
        self.connect(self.uiERec.bRegresarERecorrido, QtCore.SIGNAL("clicked()"), self.regresarRecorrido)
        self.connect(self.uiERec.bEliminarRecorrido, QtCore.SIGNAL("clicked()"), self.eliminarRecorrido)

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
        
    def regresarRecorrido(self):
        self.hide()
        self.principal.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def setRecorrido(self):
        lista_Recorrido = []
        if not QtSql.QSqlDatabase.database().isOpen():
            if not QtSql.QSqlDatabase.database():
                QtGui.QMessageBox.information(None,'ERROR', 'No se pudo abrir la BASES DE DATOS')
                
        query = QtSql.QSqlQuery("select * from Recorrido")
        fieldNo_Id = query.record().indexOf("IdRecorrido")
        fieldFecha = query.record().indexOf("Fecha")
        
        while query.next():
            idR = query.value(fieldNo_Id).toString()
            fecha = query.value(fieldFecha).toString()
            id_fecha = idR + ' Fecha: ' + fecha
            lista_Recorrido.append(id_fecha)
        
        self.uiERec.cboxIDRecorrido.addItems(lista_Recorrido)

    def eliminarRecorrido(self):
        QtGui.QMessageBox.information(None,'Eliminar Recorrido', 'Usted esta seguro de ELIMINAR un Recorrido')
        idConductor = self.uiMCond.cboxIDConductor.currentText()
        lista = idConductor.split("-")
        
        if not QtSql.QSqlDatabase.database().isOpen():
            if not QtSql.QSqlDatabase.database():
                QtGui.QMessageBox.information(None,'ERROR', 'No se pudo abrir la BASES DE DATOS')
        
        model = QtSql.QSqlTableModel(self)
        model.setQuery(QtSql.QSqlQuery("DELETE FROM Recorrido Where IdRecorrido="+lista[0]+";"))
        