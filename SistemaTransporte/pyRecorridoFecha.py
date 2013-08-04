'''
Created on 27/07/2013

@author: josanvel
'''
from PyQt4 import QtCore, QtGui
from RecorridoFecha import Ui_RecorridoFecha
from PyQt4.QtSql import *

class MyformRecorridoFecha(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uiRF = Ui_RecorridoFecha()
        self.uiRF.setupUi(self)
        #self.setCentralWidget(self.uiRF.tableViewRF)
        
        self.connect(self.uiRF.bRegresarRFecha, QtCore.SIGNAL("clicked()"), self.regresarFecha)
        self.connect(self.uiRF.bConsultarRFecha, QtCore.SIGNAL("clicked()"), self.consultarFecha)
        
                     
    
    def consultarFecha(self):
        

        db = QSqlDatabase("QMYSQL");
        db.setUserName("root")
        db.setPassword("Joselito91")
        db.setHostName("127.0.0.1")
        db.setDatabaseName("SCTE")
        
        if not db.open():
            self.setCentralWidget(self.uiRF.tableViewRF);
            model = QSqlTableModel(self);
            model.setTable("Conductor");
            model.select();
    
            self.uiRF.tableViewRF.setModel(model);
            self.uiRF.tableViewRF.setDisabled(True)
            
        
    def regresarVentanaF(self, ventana):
        self.principal = ventana
    
    def regresarFecha(self):
        self.hide()
        self.principal.show()