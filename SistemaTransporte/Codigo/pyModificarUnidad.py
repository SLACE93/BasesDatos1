
from PyQt4 import QtCore, QtGui, QtSql
from ModificarUnidad import Ui_ModificarUnidad

class MyformModificarUnidad(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uiMUnidad = Ui_ModificarUnidad()
        self.uiMUnidad.setupUi(self)
        self.center()
        self.setUnidad()
        
        self.connect(self.uiMUnidad.bRegresarUnidad, QtCore.SIGNAL("clicked()"), self.regresarUnidad)
        self.connect(self.uiMUnidad.bModificarUnidad, QtCore.SIGNAL("clicked()"), self.modificarUnidad)

    def setearBotones(self):
        iconReg = QtGui.QIcon()
        iconMod = QtGui.QIcon()
        
        iconReg.addPixmap(QtGui.QPixmap(("imagenes/bregresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiMUnidad.bRegresarUnidad.setIcon(iconReg)
        self.uiMUnidad.bRegresarUnidad.setIconSize(QtCore.QSize(240, 50))
        
        iconMod.addPixmap(QtGui.QPixmap(("imagenes/bingresar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uiMUnidad.bModificarUnidad.setIcon(iconMod)
        self.uiMUnidad.bModificarUnidad.setIconSize(QtCore.QSize(240, 50))
        
    def regresarVentana(self, ventana):
        self.principal = ventana
        
    def regresarUnidad(self):
        self.hide()
        self.principal.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def setUnidad(self):
        lista_Unidades = []
        if not QtSql.QSqlDatabase.database().isOpen():
            if not QtSql.QSqlDatabase.database():
                QtGui.QMessageBox.information(None,'ERROR', 'No se pudo abrir la BASES DE DATOS')
                
        query = QtSql.QSqlQuery("call PRGetUnidad")
        fieldNo_Uni = query.record().indexOf("IdUnidad")
        fieldNo_Cap = query.record().indexOf("Capacidad")
        
        while query.next():
            idU = query.value(fieldNo_Uni).toString()
            capacidad = query.value(fieldNo_Cap).toString()
            id_capacidad = idU + '-Capacidad:' + capacidad
            lista_Unidades.append(id_capacidad)
        
        self.uiMUnidad.cboxIDUnidad.addItems(lista_Unidades)

    def modificarUnidad(self):
        QtGui.QMessageBox.information(None,'Modificar Unidad', 'Usted podra modificar cualquier dato de las Unidades')
        idRecorrido = self.uiMUnidad.cboxIDUnidad.currentText()
        lista = idRecorrido.split("-")
        
        if not QtSql.QSqlDatabase.database().isOpen():
            if not QtSql.QSqlDatabase.database():
                QtGui.QMessageBox.information(None,'ERROR', 'No se pudo abrir la BASES DE DATOS')
        
        model = QtSql.QSqlTableModel(self)
        model.setQuery(QtSql.QSqlQuery("select Matricula, Capacidad, Anio_Fab,  Fecha_Adquisicion from Unidad Where IdUnidad="+lista[0]+";"))

        self.uiMUnidad.tableViewMU.setModel(model)
        self.uiMUnidad.tableViewMU.resizeColumnsToContents()
        
        
        