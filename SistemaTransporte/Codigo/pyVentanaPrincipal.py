'''
Created on 27/07/2013

@author: josanvel
'''

import sys
from PyQt4 import QtCore, QtGui
from VentanaPrincipal import Ui_Principal
from pyRecorridos import MyformRecorridos
from pyConductor import MyformConductor
from pyUnidades import MyformUnidades
from pyConsultas import MyformConsultas
import mysql.connector as mdb

class pyVentanaP(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Principal()
        self.ui.setupUi(self)
        self.conexion()
        
        self.connect(self.ui.brecorridos, QtCore.SIGNAL("clicked()"), self.entrarRecorridos)
        self.connect(self.ui.bconductores, QtCore.SIGNAL("clicked()"), self.entrarConductor)
        self.connect(self.ui.bunidades, QtCore.SIGNAL("clicked()"), self.entrarUnidades)
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
        
    def entrarConsultas(self):
        self.hide()
        self.consultas = MyformConsultas()
        self.consultas.regresarVentanaCons(self)
        self.consultas.show()
        
    def conexion(self):
        try:
            con = mdb.connect(user='root', password='Joselito91', host='127.0.0.1', database='SCTE');
            cur = con.cursor()
            cur.execute("INSERT INTO Conductor VALUES('123',NULL,'jose.','1324501991','2013/07/2','1993/02/08',1)")
            
            ver = cur.fetchone()
            print "Database version : %s " % ver
        except mdb.Error as e:
            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)
        finally:     
            if con:    
                con.commit()
                con.close()