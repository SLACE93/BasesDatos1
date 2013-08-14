'''
Created on 27/07/2013

@author: josanvel
'''
from PyQt4 import QtCore, QtGui, QtSql
from Recorridos import Ui_Recorridos
import exceptions

class MyformRecorridos(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uiR = Ui_Recorridos()
        self.uiR.setupUi(self)
        self.center()
        self.setearBotones()
        self.setConductores_Unidad()
        
        self.connect(self.uiR.bRegresarRecorridos, QtCore.SIGNAL("clicked()"), self.regresarRecorrido)
        self.connect(self.uiR.bingresarRecorridos, QtCore.SIGNAL("clicked()"), self.ingresarRecorrido)

    def setearBotones(self):
        iconReg = QtGui.QIcon()
        iconIng = QtGui.QIcon()
        
        iconReg.addPixmap(QtGui.QPixmap(("imagenes/bregresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiR.bRegresarRecorridos.setIcon(iconReg)
        self.uiR.bRegresarRecorridos.setIconSize(QtCore.QSize(240, 50))
        
        iconIng.addPixmap(QtGui.QPixmap(("imagenes/bingresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiR.bingresarRecorridos.setIcon(iconIng)
        self.uiR.bingresarRecorridos.setIconSize(QtCore.QSize(240, 50))
        
    def regresarVentanaR(self,ventanaAtras):
        self.ventana = ventanaAtras
    
    def regresarRecorrido(self):
        self.hide()
        self.ventana.show()
    
    def ingresarRecorrido(self):
        numPas = self.uiR.lineEPasajeros.displayText()
        conductor = self.uiR.comboBIDConductor.currentText()
        unidad = self.uiR.comboBIDUnidad.currentText()
        indiceEstSal = self.uiR.comboBEstSalida.currentIndex() + 1
        indiceEstLleg = self.uiR.comboBEstLlegada.currentIndex() +1
        c = conductor.split('-')
        u = unidad.split('-')
        idCon = c[0]
        idUni = u[0]
        print idCon
        print idUni
        

        if idCon != '' and idUni != '' and numPas != '':    
            if self.toInt(idCon) == None:
                QtGui.QMessageBox.information(None, 'Ingreso erroneo','Solo se admite enteros en el campo ID Conductor')
                self.uiR.lineEIDConductor.setText("")
                
            elif self.toInt(idUni) == None:
                QtGui.QMessageBox.information(None, 'Ingreso erroneo','Solo se admite enteros en el campo ID Unidad')
                self.uiR.lineEIDUnidad.setText("")
                
            elif self.toInt(numPas) == None:
                QtGui.QMessageBox.information(None, 'Ingreso erroneo','Solo se admite enteros en el campo de num Pasajeros')
                self.uiR.lineEPasajeros.setText("")
            elif self.uiR.comboBEstLlegada.currentText() == self.uiR.comboBEstSalida.currentText(): 
                QtGui.QMessageBox.information(None, 'Ingreso erroneo','Estacion de destino incorrecta')
            elif indiceEstSal > 1 and indiceEstLleg >1  : 
                QtGui.QMessageBox.information(None, 'Ingreso erroneo','Recorrido no existente')
            else: 
                self.IngresarOperacion(idCon,idUni)
                self.hide()
                self.ventana.show()    
        else:
            self.uiR.setStyleSheet(("background-image: url()"))
            QtGui.QMessageBox.information(self, 'Campos vacios', 'Todos los campos deben contener informacion')

            
    def IngresarOperacion(self, idCo,idUn):
        idConductor = self.toInt(idCo)
        idUnidad = self.toInt(idUn)
        
        fecha = QtCore.QDate.currentDate()
        NoPasaj = self.toInt(self.uiR.lineEPasajeros.displayText())
        horaS = self.uiR.timeEHoraS.time()
        horaLl = self.uiR.timeEHoraLl.time()
        
        idEstS = self.uiR.comboBEstSalida.currentIndex() + 1
        idEstLl = self.uiR.comboBEstLlegada.currentIndex() + 1
        
        if not QtSql.QSqlDatabase.database().isOpen():
            if not QtSql.QSqlDatabase.database():
                print 'No se pudo abrir la BASES DE DATOS'
        
        query = QtSql.QSqlQuery()
        query.prepare("call PRInsertRecorrido(?,?,?,?,?,?,?,?)")

        query.addBindValue(fecha)
        query.addBindValue(idConductor)
        query.addBindValue(idUnidad)
        query.addBindValue(NoPasaj)
        query.addBindValue(horaS)
        query.addBindValue(horaLl)
        query.addBindValue(idEstS)
        query.addBindValue(idEstLl)
                
        if not query.exec_():
            QtGui.QMessageBox.warning( None, "Error al crear un Recorrido",\
                                          "No se pudo INSERTAR a un nuevo Recorrido" ) 
        else:
            QtGui.QMessageBox.information(None, "INFORMACION","Ah ingresado un  nuevo Recorrido")
            
    def toInt(self,num):
        try:
            return int(num)
        except exceptions.ValueError:
            return None

    def setConductores_Unidad(self):
        lista_Conductores = []
        lista_Unidades = [] 
        if not QtSql.QSqlDatabase.database().isOpen():
            if not QtSql.QSqlDatabase.database():
                print 'No se pudo abrir la BASES DE DATOS'
                
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
        print lista_Conductores
        self.uiR.comboBIDConductor.addItems(lista_Conductores)
        
        query = QtSql.QSqlQuery("call PRGetUnidad")
        fieldNo_Uni = query.record().indexOf("IdUnidad")
        fieldNo_Cap = query.record().indexOf("Capacidad")
        while query.next():
            idUni = query.value(fieldNo_Uni).toString()
            capacidad = query.value(fieldNo_Cap).toString()
            id_capacidad = idUni + '-Capacidad: ' + capacidad
            lista_Unidades.append(id_capacidad)
        self.uiR.comboBIDUnidad.addItems(lista_Unidades)

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
            
        

        