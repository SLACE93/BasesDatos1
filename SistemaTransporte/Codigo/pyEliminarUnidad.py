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
        self.setUnidad()
        
        self.connect(self.uiEUnidad.bRegresarEUnidad, QtCore.SIGNAL("clicked()"), self.regresarUnidad)
        self.connect(self.uiEUnidad.bEliminarUnidad, QtCore.SIGNAL("clicked()"), self.eliminarUnidad)

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
        
    def regresarUnidad(self):
        self.hide()
        self.principal.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setUnidad(self):
        lista_Unidades = []
        if not QtSql.QSqlDatabase.database().isOpen():
            if not QtSql.QSqlDatabase.database():
                QtGui.QMessageBox.information(None,'ERROR', 'No se pudo abrir la BASES DE DATOS')
                
        query = QtSql.QSqlQuery("call PRGetUnidad")
        fieldNo_Uni = query.record().indexOf("IdUnidad")
        fieldNo_Cap = query.record().indexOf("Capacidad")
        
        while query.next():
            idU = query.value(fieldNo_Uni).toString()
            capacidad = query.value(fieldNo_Cap).toString()
            id_capacidad = idU + '-Capacidad:' + capacidad
            lista_Unidades.append(id_capacidad)
        
        self.uiEUnidad.cboxIDUnidad.addItems(lista_Unidades)
        
    def eliminarUnidad(self):
        QtGui.QMessageBox.information(None,'Eliminar Unidad', 'Usted esta seguro de ELIMINAR una Unidades')
        idRecorrido = self.uiEUnidad.cboxIDUnidad.currentText()
        lista = idRecorrido.split("-")
        
        if not QtSql.QSqlDatabase.database().isOpen():
            if not QtSql.QSqlDatabase.database():
                QtGui.QMessageBox.information(None,'ERROR', 'No se pudo abrir la BASES DE DATOS')
        
        model = QtSql.QSqlTableModel(self)
        model.setQuery(QtSql.QSqlQuery("DELETE FROM Unidad Where IdUnidad="+lista[0]+";"))

        