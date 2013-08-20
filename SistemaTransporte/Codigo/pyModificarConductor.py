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
        self.setConductores()
        
        self.connect(self.uiMCond.bRegresarConductor, QtCore.SIGNAL("clicked()"), self.regresarConductor)
        self.connect(self.uiMCond.bModificarConductor, QtCore.SIGNAL("clicked()"), self.modificarConductor)

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
        
        self.uiMCond.cboxIDConductor.addItems(lista_Conductores)

    def modificarConductor(self):
        QtGui.QMessageBox.information(None,'Modificar Conductor', 'Usted podra modificar cualquier dato del Conductor')
        idConductor = self.uiMCond.cboxIDConductor.currentText()
        lista = idConductor.split("-")
        
        if not QtSql.QSqlDatabase.database().isOpen():
            if not QtSql.QSqlDatabase.database():
                QtGui.QMessageBox.information(None,'ERROR', 'No se pudo abrir la BASES DE DATOS')
        
        model = QtSql.QSqlTableModel(self)
        model.setQuery(QtSql.QSqlQuery("select Cedula, cNombre, NoLicencia, Fecha_Ingreso, Fecha_Nacimiento from Conductor Where IdConductor="+lista[0]+";"))

        self.uiMCond.tableViewMC.setModel(model)
        self.uiMCond.tableViewMC.resizeColumnsToContents()
        
        