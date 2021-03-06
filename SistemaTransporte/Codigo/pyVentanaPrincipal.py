'''
Created on 27/07/2013

@author: josanvel
'''

from PyQt4 import QtCore, QtGui, QtSql
from VentanaPrincipal import Ui_Principal
from pyRecorridos import MyformRecorridos
from pyConductor import MyformConductor
from pyUnidades import MyformUnidades
from pyModificar import MyformModificar
from pyEliminar import MyformEliminar
from pyConsultas import MyformConsultas

class pyVentanaP(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Principal()
        self.ui.setupUi(self)
        self.IniciarBase()
        self.center()
        
        self.connect(self.ui.brecorridos, QtCore.SIGNAL("clicked()"), self.entrarRecorridos)
        self.connect(self.ui.bconductores, QtCore.SIGNAL("clicked()"), self.entrarConductor)
        self.connect(self.ui.bunidades, QtCore.SIGNAL("clicked()"), self.entrarUnidades)
        self.connect(self.ui.beliminar, QtCore.SIGNAL("clicked()"), self.entrarEliminar)
        self.connect(self.ui.bmodificar, QtCore.SIGNAL("clicked()"), self.entrarModificar)
        self.connect(self.ui.bconsultas, QtCore.SIGNAL("clicked()"), self.entrarConsultas)

        
    def entrarRecorridos(self):
        self.hide()
        self.recorridos = MyformRecorridos()
        self.recorridos.regresarVentanaR(self)
        self.recorridos.show()
        
    def entrarConductor(self):
        self.hide()
        self.conductor = MyformConductor()
        self.conductor.regresarVentanaCond(self)
        self.conductor.show()
        
    def entrarUnidades(self):
        self.hide()
        self.unidades = MyformUnidades()
        self.unidades.regresarVentanaU(self)
        self.unidades.show()
        

    def entrarEliminar(self):
        self.hide()
        self.eliminar = MyformEliminar()
        self.eliminar.regresarVentanaEliminar(self)
        self.eliminar.show()
        
    def entrarModificar(self):
        self.hide()
        self.modificar = MyformModificar()
        self.modificar.regresarVentanaModificar(self)
        self.modificar.show()
        
    def entrarConsultas(self):
        self.hide()
        self.consultas = MyformConsultas()
        self.consultas.regresarVentanaCons(self)
        self.consultas.show()
        
    def IniciarBase(self):
        self.db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
        self.db.setUserName("root");
        self.db.setPassword("Joselito91");
        self.db.setHostName("127.0.0.1");
        self.db.setDatabaseName("SCTE")
        self.db.open()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        