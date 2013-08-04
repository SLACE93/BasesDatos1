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
        self.connect(self.uiR.bRegresarRecorridos, QtCore.SIGNAL("clicked()"), self.regresarRecorrido)
        self.connect(self.uiR.bingresarRecorridos, QtCore.SIGNAL("clicked()"), self.ingresarRecorrido)
        
    def regresarVentanaR(self,ventanaAtras):
        self.ventana = ventanaAtras
    
    def regresarRecorrido(self):
        self.hide()
        self.ventana.show()
    
    def ingresarRecorrido(self):
        numPas = self.uiR.lineEPasajeros.displayText()
        idCon = self.uiR.lineEIDConductor.displayText()
        idUni = self.uiR.lineEIDUnidad.displayText()

        if idCon != '' and idUni != '' and numPas != '':    
            if self.toInt(idCon) == None:
                QtGui.QMessageBox.information(self, 'Ingreso erroneo','Solo se admite enteros en el campo ID Conductor')
                self.uiR.lineEIDConductor.setText("")
                
            elif self.toInt(idUni) == None:
                QtGui.QMessageBox.information(self, 'Ingreso erroneo','Solo se admite enteros en el campo ID Unidad')
                self.uiR.lineEIDUnidad.setText("")
                
            elif self.toInt(numPas) == None:
                QtGui.QMessageBox.information(self, 'Ingreso erroneo','Solo se admite enteros en el campo de num Pasajeros')
                self.uiR.lineEPasajeros.setText("")
                
            else: 
                self.IngresarOperacion()
                self.hide()
                self.ventana.show()    
        else:
            QtGui.QMessageBox.information(self, 'Campos vacios', 'Todos los campos deben contener informacion')
            

    def IngresarOperacion(self):
        idRecorrido = None
        fecha = QtCore.QDate.currentDate()
        NoPasaj = self.toInt(self.uiR.lineEPasajeros.displayText())
        horaS = self.uiR.timeEHoraS.time()
        horaLl = self.uiR.timeEHoraLl.time()
        
        idEstS = self.uiR.comboBEstSalida.currentText()
        idEstLl = self.uiR.comboBEstLlegada.currentText()
        idUsuario = self.toInt(1)
        
        if not QtSql.QSqlDatabase.database().isOpen():
            if not QtSql.QSqlDatabase.database():
                print 'No se pudo abrir la BASES DE DATOS'
            
        query = QtSql.QSqlQuery()
        query.prepare("""INSERT INTO Recorrido (IdRecorrido, Fecha, NoPasajeros, Hora_Salida, Hora_Llegada, IdEstacion_Salida, IdEstacion_Llegada, IdUsuario) VALUES(?,?,?,?,?,?,?,?)""")

        query.addBindValue(idRecorrido)
        query.addBindValue(fecha)
        query.addBindValue(NoPasaj)
        query.addBindValue(horaS)
        query.addBindValue(horaLl)
        query.addBindValue(idUsuario)
        query.addBindValue(idUsuario)
        query.addBindValue(idUsuario)
                
        if not query.exec_():
            QtGui.QMessageBox.warning( None, "Error al crear un Recorrido",\
                                          "No se pudo INSERTAR a un nuevo Recorrido" ) 
        else:
            QtGui.QMessageBox.information(self, "INFORMACION","Ah ingresado un  nuevo Recorrido")
            
    def toInt(self,num):
        try:
            return int(num)
        except exceptions.ValueError:
            return None
        
        

        