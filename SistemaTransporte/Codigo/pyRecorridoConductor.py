'''
Created on 27/07/2013

@author: josanvel
'''

from PyQt4 import QtCore, QtGui, QtSql
from RecorridoConductor import Ui_RecorridoConductor
import exceptions

class MyformRecorridoConductor(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uiRCond = Ui_RecorridoConductor()
        self.uiRCond.setupUi(self)
        self.center()
        self.setearBotones()
        self.setConductores()
        self.connect(self.uiRCond.bRegresarConductor, QtCore.SIGNAL("clicked()"), self.regresarConductor)
        self.connect(self.uiRCond.bConsultarConductor, QtCore.SIGNAL("clicked()"), self.consultarRecorridoCond)

    def setearBotones(self):
        iconReg = QtGui.QIcon()
        iconIng = QtGui.QIcon()
        
        iconReg.addPixmap(QtGui.QPixmap(("imagenes/bregresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiRCond.bRegresarConductor.setIcon(iconReg)
        self.uiRCond.bRegresarConductor.setIconSize(QtCore.QSize(240, 50))
        
        iconIng.addPixmap(QtGui.QPixmap(("imagenes/bingresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiRCond.bConsultarConductor.setIcon(iconIng)
        self.uiRCond.bConsultarConductor.setIconSize(QtCore.QSize(240, 50))
        
    def regresarVentana(self, ventana):
        self.principal = ventana
        
    def regresarConductor(self):
        self.hide()
        self.principal.show()
    
    def consultarRecorridoCond(self):
        conductor = self.uiRCond.comboBIDConductorRC.currentText()
        c = conductor.split('-')
        self.idRCond = c[0]
        
        if(self.idRCond !=''):
            if self.toInt(self.idRCond) == None:
                QtGui.QMessageBox.information(self, 'Ingreso erroneo','Solo se admite enteros en el campo de ID Conductor')
            else:
                self.consultarConductor()
                
        else:
            QtGui.QMessageBox.information(self, 'Campos vacios', 'Todos los campos deben contener informacion')

    def consultarConductor(self):
        if not QtSql.QSqlDatabase.database().isOpen():
            if not QtSql.QSqlDatabase.database():
                print 'No se pudo abrir la BASES DE DATOS'
        else: 
                print 'Bases de Datos Abierta'
        
        model = QtSql.QSqlTableModel(self)
        
        #dia1 = self.uiRCond.fechaInicialRC.date().day()
        #mes1 = self.uiRCond.fechaInicialRC.date().month()
        #ano1 = self.uiRCond.fechaInicialRC.date().year()
        #fechaInicial = str(ano1)+"/"+str(mes1)+"/"+str(dia1)
        
        #dia2 = self.uiRCond.fechaFinalRC.date().day()
        #mes2 = self.uiRCond.fechaFinalRC.date().month()
        #ano2 = self.uiRCond.fechaFinalRC.date().year()
        #fechaFinal = str(ano2)+"/"+str(mes2)+"/"+str(dia2)
        
        conductor = self.uiRCond.comboBIDConductorRC.currentText()
        c = conductor.split('-')
        
        idCond_CI = c[0]
        
        model.setQuery(QtSql.QSqlQuery("CALL PRQueryRecorridoConductor('"+idCond_CI+"')"))
        model.select();
    
        self.uiRCond.tableViewRC.setModel(model)
        self.uiRCond.tableViewRC.resizeColumnsToContents()
        self.uiRCond.tableViewRC.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        
    def toInt(self,num):
        try:
            return int(num)
        except exceptions.ValueError:
            return None

    def setConductores(self):
        lista_Conductores = []
        if not QtSql.QSqlDatabase.database().isOpen():
            if not QtSql.QSqlDatabase.database():
                print 'No se pudo abrir la BASES DE DATOS'
                
        query = QtSql.QSqlQuery("call PRGetConductor")
        #fieldNo_Id = query.record().indexOf("IdConductor")
        fieldNo_Ced = query.record().indexOf("Cedula")
        fieldNo_Nom =query.record().indexOf("cNombre")
        
        while query.next():
            #idC = query.value(fieldNo_Id).toString()
            cedula = query.value(fieldNo_Ced).toString()
            nombre = query.value(fieldNo_Nom).toString()
            ced_nombre = cedula + '-' + nombre
            lista_Conductores.append(ced_nombre)
        print lista_Conductores
        self.uiRCond.comboBIDConductorRC.addItems(lista_Conductores)
    
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    
        