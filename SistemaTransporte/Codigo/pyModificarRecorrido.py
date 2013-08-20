
from PyQt4 import QtCore, QtGui, QtSql
from ModificarRecorrido import Ui_ModificarRecorrido

class MyformModificarRecorrido(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uiMRec = Ui_ModificarRecorrido()
        self.uiMRec.setupUi(self)
        self.center()
        self.setRecorrido()
        
        self.connect(self.uiMRec.bRegresarRecorrido, QtCore.SIGNAL("clicked()"), self.regresarRecorrido)
        self.connect(self.uiMRec.bModificarRecorrido, QtCore.SIGNAL("clicked()"), self.modificarRecorrido)

    def setearBotones(self):
        iconReg = QtGui.QIcon()
        iconMod = QtGui.QIcon()
        
        iconReg.addPixmap(QtGui.QPixmap(("imagenes/bregresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiMRec.bRegresarRecorrido.setIcon(iconReg)
        self.uiMRec.bRegresarRecorrido.setIconSize(QtCore.QSize(240, 50))
        
        iconMod.addPixmap(QtGui.QPixmap(("imagenes/bingresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiMRec.bModificarRecorrido.setIcon(iconMod)
        self.uiMRec.bModificarRecorrido.setIconSize(QtCore.QSize(240, 50))
        
    def regresarVentana(self, ventana):
        self.principal = ventana
        
    def regresarRecorrido(self):
        self.hide()
        self.principal.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def setRecorrido(self):
        lista_Recorrido = []
        if not QtSql.QSqlDatabase.database().isOpen():
            if not QtSql.QSqlDatabase.database():
                QtGui.QMessageBox.information(None,'ERROR', 'No se pudo abrir la BASES DE DATOS')
                
        query = QtSql.QSqlQuery("select * from Recorrido")
        fieldNo_Id = query.record().indexOf("IdRecorrido")
        fieldFecha = query.record().indexOf("Fecha")
        "select Fecha,NoPasajeros,Hora_Salida, HoraLlegada from Recorrido  Where IdRecorrido="
        while query.next():
            idR = query.value(fieldNo_Id).toString()
            fecha = query.value(fieldFecha).toString()
            id_fecha = idR + '-Fecha: ' + fecha
            lista_Recorrido.append(id_fecha)
        
        self.uiMRec.cboxIDRecorrido.addItems(lista_Recorrido)
        
    def modificarRecorrido(self):
        QtGui.QMessageBox.information(None,'Modificar Recorrido', 'Usted podra modificar cualquier dato del Recorrido')
        idRecorrido = self.uiMRec.cboxIDRecorrido.currentText()
        lista = idRecorrido.split("-")
        
        if not QtSql.QSqlDatabase.database().isOpen():
            if not QtSql.QSqlDatabase.database():
                QtGui.QMessageBox.information(None,'ERROR', 'No se pudo abrir la BASES DE DATOS')
        
        model = QtSql.QSqlTableModel(self)
        model.setQuery(QtSql.QSqlQuery("select Fecha, NoPasajeros, Hora_Salida,  Hora_Llegada from Recorrido r Where IdRecorrido="+lista[0]+";"))

        self.uiMRec.tableViewMR.setModel(model)
        self.uiMRec.tableViewMR.resizeColumnsToContents()