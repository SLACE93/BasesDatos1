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
        self.center()
        self.setearBotones()
        
        
        self.connect(self.uiRF.bRegresarRFecha, QtCore.SIGNAL("clicked()"), self.regresarFecha)
        self.connect(self.uiRF.bConsultarRFecha, QtCore.SIGNAL("clicked()"), self.consultar)

    def setearBotones(self):
        iconReg = QtGui.QIcon()
        iconIng = QtGui.QIcon()
        
        iconReg.addPixmap(QtGui.QPixmap(("imagenes/bregresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiRF.bRegresarRFecha.setIcon(iconReg)
        self.uiRF.bRegresarRFecha.setIconSize(QtCore.QSize(240, 50))
        
        iconIng.addPixmap(QtGui.QPixmap(("imagenes/bingresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiRF.bConsultarRFecha.setIcon(iconIng)
        self.uiRF.bConsultarRFecha.setIconSize(QtCore.QSize(240, 50))            
    
    def consultar(self):
        fechaInicial = self.uiRF.dFechaInicial.date()
        fechaFinal = self.uiRF.dFechaFinal.date()
        if fechaInicial>=fechaFinal:
            QtGui.QMessageBox.information(None,"Ingreso erroneo","Fecha final incorrecta")
        else:
            self.consultarFecha()
        
    def consultarFecha(self):        
        if not QtSql.QSqlDatabase.database().isOpen():
            if not QtSql.QSqlDatabase.database():
                QtGui.QMessageBox.information(None,'ERROR', 'No se pudo abrir la BASES DE DATOS')
        
        model = QtSql.QSqlTableModel(self)
        
        dia1 = self.uiRF.dFechaInicial.date().day()
        mes1 = self.uiRF.dFechaInicial.date().month()
        ano1 = self.uiRF.dFechaInicial.date().year()
        fechaInicial = str(ano1)+"/"+str(mes1)+"/"+str(dia1)
        
        dia2 = self.uiRF.dFechaFinal.date().day()
        mes2 = self.uiRF.dFechaFinal.date().month()
        ano2 = self.uiRF.dFechaFinal.date().year()
        fechaFinal = str(ano2)+"/"+str(mes2)+"/"+str(dia2)
        
        model.setQuery(QtSql.QSqlQuery("call PRQueryRecorridoFecha('"+fechaInicial+"','"+fechaFinal+"')"))
        model.select();
    
        self.uiRF.tableViewRF.setModel(model)
        self.uiRF.tableViewRF.resizeColumnsToContents()
        self.uiRF.tableViewRF.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
            
    def regresarVentanaF(self, ventana):
        self.principal = ventana
    
    def regresarFecha(self):
        self.hide()
        self.principal.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())