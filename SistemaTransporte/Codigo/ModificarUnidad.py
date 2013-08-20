from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ModificarUnidad(object):
    def setupUi(self, ModificarUnidad):
        ModificarUnidad.setObjectName(_fromUtf8("ModificarUnidad"))
        ModificarUnidad.resize(640, 520)
        ModificarUnidad.setStyleSheet(("background-image: url(imagenes/principal.jpg)"))
        self.TitleModificarUnidad = QtGui.QLabel(ModificarUnidad)
        self.TitleModificarUnidad.setGeometry(QtCore.QRect(180, 50, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.TitleModificarUnidad.setFont(font)
        self.TitleModificarUnidad.setObjectName(_fromUtf8("TitleModificarUnidad"))
        self.lIDUnidad = QtGui.QLabel(ModificarUnidad)
        self.lIDUnidad.setGeometry(QtCore.QRect(280, 110, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lIDUnidad.setFont(font)
        self.lIDUnidad.setObjectName(_fromUtf8("lIDUnidad"))
        self.bModificarUnidad = QtGui.QPushButton(ModificarUnidad)
        self.bModificarUnidad.setGeometry(QtCore.QRect(330, 440, 240, 50))
        self.bModificarUnidad.setObjectName(_fromUtf8("bModificarUnidad"))
        self.bRegresarUnidad = QtGui.QPushButton(ModificarUnidad)
        self.bRegresarUnidad.setGeometry(QtCore.QRect(50, 440, 240, 50))
        self.bRegresarUnidad.setObjectName(_fromUtf8("bRegresarUnidad"))
        self.tableViewMU = QtGui.QTableView(ModificarUnidad)
        self.tableViewMU.setGeometry(QtCore.QRect(30, 221, 570, 200))
        self.tableViewMU.setObjectName(_fromUtf8("tableViewMU"))
        self.cboxIDUnidad = QtGui.QComboBox(ModificarUnidad)
        self.cboxIDUnidad.setGeometry(QtCore.QRect(170, 150, 321, 27))
        self.cboxIDUnidad.setObjectName(_fromUtf8("cboxIDUnidad"))

        self.retranslateUi(ModificarUnidad)
        QtCore.QMetaObject.connectSlotsByName(ModificarUnidad)

    def retranslateUi(self, ModificarUnidad):
        ModificarUnidad.setWindowTitle(_translate("ModificarUnidad", "Form", None))
        self.TitleModificarUnidad.setText(_translate("ModificarUnidad", "MODIFICAR UNIDAD", None))
        self.lIDUnidad.setText(_translate("ModificarUnidad", "ID UNIDAD", None))
        self.bModificarUnidad.setText(_translate("ModificarUnidad", "MODIFICAR", None))
        self.bRegresarUnidad.setText(_translate("ModificarUnidad", "REGRESAR", None))
