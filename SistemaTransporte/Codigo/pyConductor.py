'''
Created on 27/07/2013

@author: josanvel
'''
from PyQt4 import QtCore, QtGui, QtSql
from Conductor import Ui_Conductor
import exceptions


class MyformConductor(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uiCond = Ui_Conductor()
        self.uiCond.setupUi(self)
        self.setearBotones()
        
        self.connect(self.uiCond.bRegresarConductores, QtCore.SIGNAL("clicked()"),self.regresarConductor)
        self.connect(self.uiCond.bingresarConductores, QtCore.SIGNAL("clicked()"),self.ingresarConductor)


    def setearBotones(self):
        iconReg = QtGui.QIcon()
        iconIng = QtGui.QIcon()
        
        iconReg.addPixmap(QtGui.QPixmap(("imagenes/bregresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiCond.bRegresarConductores.setIcon(iconReg)
        self.uiCond.bRegresarConductores.setIconSize(QtCore.QSize(240, 50))
        
        iconIng.addPixmap(QtGui.QPixmap(("imagenes/bingresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiCond.bingresarConductores.setIcon(iconIng)
        self.uiCond.bingresarConductores.setIconSize(QtCore.QSize(240, 50))
        
    def regresarVentanaCond(self, ventanaAtras):
        self.ventana = ventanaAtras
        
    def regresarConductor(self):
        self.hide()
        self.ventana.show()
    
    def ingresarConductor(self):
        cedula = self.uiCond.lineEIDCedula.displayText()
        licencia = self.uiCond.lineENLicencia.displayText()
        nombre = self.uiCond.lineENombre.displayText()
        
        if cedula!='' and licencia!='' and nombre!='':    
            if len(cedula) != 10 or self.toInt(cedula)==None:
                QtGui.QMessageBox.information(self, 'Ingreso erroneo','Numero de cedula incorrecto')
                self.uiCond.lineEIDCedula.setText("")
                
            elif len(licencia) != 10 or self.toInt(licencia)==None:
                QtGui.QMessageBox.information(self, 'Ingreso erroneo','Numero de licencia incorrecto')
                self.uiCond.lineENLicencia.setText("")
                               
            elif self.toInt(nombre):
                QtGui.QMessageBox.information(self, 'Ingreso erroneo','Nombre incorrecto')
                self.uiCond.lineENombre.setText("")
            else:
                self.IngresarOperacion() 
                self.hide()
                self.ventana.show()
        else:
            QtGui.QMessageBox.information(self, 'Campos vacios', 'Todos los campos deben contener informacion')

    def IngresarOperacion(self):
        idCed = self.toInt(self.uiCond.lineEIDCedula.displayText())
        nom = str(self.uiCond.lineENombre.displayText())
        licencia = str(self.uiCond.lineENLicencia.displayText())
        fechaHoy = QtCore.QDate.currentDate()
        fechaNac = self.uiCond.dEditFNac.date()
        user = self.toInt(1)
        ic = None

  
        if not QtSql.QSqlDatabase.database().isOpen():
            if not QtSql.QSqlDatabase.database():
                print 'No se pudo abrir la BASES DE DATOS'
            
        query = QtSql.QSqlQuery()
        query.prepare("""INSERT INTO Conductor (Cedula, IdConductor,cNombre, NoLicencia, Fecha_Ingreso, Fecha_Nacimiento, IdUsuario) VALUES(?,?,?,?,?,?,?)""")

        query.addBindValue(idCed)
        query.addBindValue(ic)
        query.addBindValue(nom)
        query.addBindValue(licencia)
        query.addBindValue(fechaHoy)
        query.addBindValue(fechaNac)
        query.addBindValue(user)
                
        if not query.exec_():
            QtGui.QMessageBox.warning( None, "Error al crear un conductor",\
                                          "No se pudo INSERTAR a un nuevo Conductor" ) 
        else:
            QtGui.QMessageBox.information(self, "INFORMACION","Ah ingresado un  nuevo Conductor") 

    def toInt(self,num):
        try:
            return int(num)
        except exceptions.ValueError:
            return None

        