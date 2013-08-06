'''
Created on 27/07/2013

@author: josanvel
'''
from PyQt4 import QtCore, QtGui, QtSql
from RecorridoFecha import Ui_RecorridoFecha

class MyformRecorridoFecha(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uiRF = Ui_RecorridoFecha()
        self.uiRF.setupUi(self)
        self.setearBotones()
        
        
        self.connect(self.uiRF.bRegresarRFecha, QtCore.SIGNAL("clicked()"), self.regresarFecha)
        self.connect(self.uiRF.bConsultarRFecha, QtCore.SIGNAL("clicked()"), self.consultarFecha)

    def setearBotones(self):
        iconReg = QtGui.QIcon()
        iconIng = QtGui.QIcon()
        
        iconReg.addPixmap(QtGui.QPixmap(("imagenes/bregresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiRF.bRegresarRFecha.setIcon(iconReg)
        self.uiRF.bRegresarRFecha.setIconSize(QtCore.QSize(240, 50))
        
        iconIng.addPixmap(QtGui.QPixmap(("imagenes/bingresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiRF.bConsultarRFecha.setIcon(iconIng)
        self.uiRF.bConsultarRFecha.setIconSize(QtCore.QSize(240, 50))            
    
    def consultarFecha(self):        
        if not QtSql.QSqlDatabase.database().isOpen():
            if not QtSql.QSqlDatabase.database():
                print 'No se pudo abrir la BASES DE DATOS'
        else: 
                print 'Bases de Datos Abierta'
        
        model = QtSql.QSqlTableModel(self);
        model.setQuery(QtSql.QSqlQuery("select * from Conductor where year(Fecha_Nacimiento)='2013'"))
        model.select();
    
        self.uiRF.tableViewRF.setModel(model)
        self.uiRF.tableViewRF.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
            
    def regresarVentanaF(self, ventana):
        self.principal = ventana
    
    def regresarFecha(self):
        self.hide()
        self.principal.show()