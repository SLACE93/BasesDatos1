'''
Created on 27/07/2013

@author: josanvel
'''
from PyQt4 import QtCore, QtGui, QtSql
from RecorridoUnidad import Ui_RecorridoUnidad
import exceptions

class MyformRecorridoUnidad(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uiRU = Ui_RecorridoUnidad()
        self.uiRU.setupUi(self)
        self.center()
        self.setearBotones()
        self.setUnidades()

        self.connect(self.uiRU.bRegresarRUnidad, QtCore.SIGNAL("clicked()"), self.regresarUnidad)
        self.connect(self.uiRU.bConsultarRUnidad, QtCore.SIGNAL("clicked()"), self.consultarRecorridoUnidad)

    def setearBotones(self):
        iconReg = QtGui.QIcon()
        iconCons = QtGui.QIcon()
        
        iconReg.addPixmap(QtGui.QPixmap(("imagenes/bregresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiRU.bRegresarRUnidad.setIcon(iconReg)
        self.uiRU.bRegresarRUnidad.setIconSize(QtCore.QSize(240, 50))
        
        iconCons.addPixmap(QtGui.QPixmap(("imagenes/bingresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiRU.bConsultarRUnidad.setIcon(iconCons)
        self.uiRU.bConsultarRUnidad.setIconSize(QtCore.QSize(240, 50))
        
    def regresarVentanaU(self, ventana):
        self.principal = ventana
    
    def regresarUnidad(self):
        self.hide()
        self.principal.show()
    
    def consultarRecorridoUnidad(self):
        
        self.idUnidad = self.uiRU.comboBIDUnidadRU.currentText()
        if(self.idUnidad !=''):
            if self.toInt(self.idUnidad) == None:
                QtGui.QMessageBox.information(None, 'Ingreso erroneo','Solo se admite enteros en el campo de ID Unidad')
            else: 
                self.consultarUnidad()
        else:
            QtGui.QMessageBox.information(None, 'Campos vacios', 'Todos los campos deben contener informacion')


    def consultarUnidad(self):
        if not QtSql.QSqlDatabase.database().isOpen():
            if not QtSql.QSqlDatabase.database():
                QtGui.QMessageBox.information(None,'ERROR', 'No se pudo abrir la BASES DE DATOS')
        
        model = QtSql.QSqlTableModel(self)
        
        unidad = self.uiRU.comboBIDUnidadRU.currentText()
        model.setQuery(QtSql.QSqlQuery("CALL PRQueryRecorridoUnidad('"+unidad+"')"))

        self.uiRU.tableViewRU.setModel(model)
        self.uiRU.tableViewRU.resizeColumnsToContents()
        self.uiRU.tableViewRU.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
    
    
    def toInt(self,num):
        try:
            return int(num)
        except exceptions.ValueError:
            return None
        
    def setUnidades(self):
        lista_Unidades = [] 
        if not QtSql.QSqlDatabase.database().isOpen():
            if not QtSql.QSqlDatabase.database():
                QtGui.QMessageBox.information(None,'ERROR', 'No se pudo abrir la BASES DE DATOS')
                

        query = QtSql.QSqlQuery("call PRGetUnidad")
        fieldNo_Uni = query.record().indexOf("IdUnidad")
        while query.next():
            idUni = query.value(fieldNo_Uni).toString()
            lista_Unidades.append(idUni)
            
        self.uiRU.comboBIDUnidadRU.addItems(lista_Unidades)

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
            