'''
Created on 27/07/2013

@author: josanvel
'''
from PyQt4 import QtCore, QtGui, QtSql
from RecorridoHora import Ui_RecorridoHoras

class MyformRecorridoHoras(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uiRH = Ui_RecorridoHoras()
        self.uiRH.setupUi(self)
        self.center()
        self.setearBotones()
        
        self.connect(self.uiRH.bRegresarHoras, QtCore.SIGNAL("clicked()"), self.regresarHora)
        self.connect(self.uiRH.bConsultarHoras, QtCore.SIGNAL("clicked()"), self.consultarRecorridoHora)

    def setearBotones(self):
        iconReg = QtGui.QIcon()
        iconCons = QtGui.QIcon()
        
        iconReg.addPixmap(QtGui.QPixmap(("imagenes/bregresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiRH.bRegresarHoras.setIcon(iconReg)
        self.uiRH.bRegresarHoras.setIconSize(QtCore.QSize(240, 50))
        
        iconCons.addPixmap(QtGui.QPixmap(("imagenes/bingresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiRH.bConsultarHoras.setIcon(iconCons)
        self.uiRH.bConsultarHoras.setIconSize(QtCore.QSize(240, 50))
        
    
    def consultarRecorridoHora(self):
        horaInic = self.uiRH.timeHoraInicialRH.time().toString("hh:mm:ss")
        horaFinal = self.uiRH.timeHoraFinalRH.time().toString("hh:mm:ss")
        print horaInic
        print horaFinal
        if horaInic >= horaFinal:
            QtGui.QMessageBox.information(None, 'Ingreso erroneo','Hora final incorrecta')
        else:
            self.consultar(horaInic, horaFinal)

    def consultar(self, horaI, horaF):
        if not QtSql.QSqlDatabase.database().isOpen():
            if not QtSql.QSqlDatabase.database():
                print 'No se pudo abrir la BASES DE DATOS'
        model = QtSql.QSqlTableModel(self)
        horaInicial = horaI
        horaFinal = horaF
        print horaInicial
        print horaFinal
        
        model.setQuery(QtSql.QSqlQuery("call PRQueryRecorridoHora('"+horaInicial+"','"+horaFinal+"')"))
        model.select();
    
        self.uiRH.tableViewRH.setModel(model)
        self.uiRH.tableViewRH.resizeColumnsToContents()
        self.uiRH.tableViewRH.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        
        
    def regresarVentanaH(self, ventana):
        self.principal = ventana
    
    def regresarHora(self):
        self.hide()
        self.principal.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())