from PyQt4 import QtCore, QtGui
from comboBox import ExtendedComboBox

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

class Ui_ModificarRecorrido(object):
    def setupUi(self, ModificarRecorrido):
        ModificarRecorrido.setObjectName(_fromUtf8("ModificarRecorrido"))
        ModificarRecorrido.resize(640, 520)
        ModificarRecorrido.setStyleSheet(("background-image: url(imagenes/principal.jpg)"))
        self.TitleModificarRecorrido = QtGui.QLabel(ModificarRecorrido)
        self.TitleModificarRecorrido.setStyleSheet(("background-image: url()")) 
        self.TitleModificarRecorrido.setGeometry(QtCore.QRect(170, 50, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.TitleModificarRecorrido.setFont(font)
        self.TitleModificarRecorrido.setObjectName(_fromUtf8("TitleModificarRecorrido"))
        self.lIDRecorrido = QtGui.QLabel(ModificarRecorrido)
        self.lIDRecorrido.setStyleSheet(("background-image: url()")) 
        self.lIDRecorrido.setGeometry(QtCore.QRect(260, 110, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lIDRecorrido.setFont(font)
        self.lIDRecorrido.setObjectName(_fromUtf8("lIDRecorrido"))
        self.bModificarRecorrido = QtGui.QPushButton(ModificarRecorrido)
        self.bModificarRecorrido.setGeometry(QtCore.QRect(330, 440, 240, 50))
        self.bModificarRecorrido.setObjectName(_fromUtf8("bModificarRecorrido"))
        self.bRegresarRecorrido = QtGui.QPushButton(ModificarRecorrido)
        self.bRegresarRecorrido.setGeometry(QtCore.QRect(50, 440, 240, 50))
        self.bRegresarRecorrido.setObjectName(_fromUtf8("bRegresarRecorrido"))
        self.tableViewMR = QtGui.QTableView(ModificarRecorrido)
        self.tableViewMR.setStyleSheet(("background-image: url()")) 
        self.tableViewMR.setGeometry(QtCore.QRect(30, 221, 570, 200))
        self.tableViewMR.setObjectName(_fromUtf8("tableViewMR"))
        self.cboxIDRecorrido = ExtendedComboBox(ModificarRecorrido)
        self.cboxIDRecorrido.setGeometry(QtCore.QRect(170, 150, 321, 27))
        self.cboxIDRecorrido.setObjectName(_fromUtf8("cboxIDRecorrido"))

        self.retranslateUi(ModificarRecorrido)
        QtCore.QMetaObject.connectSlotsByName(ModificarRecorrido)

    def retranslateUi(self, ModificarRecorrido):
        ModificarRecorrido.setWindowTitle(_translate("ModificarRecorrido", "ModificarRecorrido", None))
        self.TitleModificarRecorrido.setText(_translate("ModificarRecorrido", "MODIFICAR RECORRIDO", None))
        self.lIDRecorrido.setText(_translate("ModificarRecorrido", "ID RECORRIDO", None))
        self.bModificarRecorrido.setText(_translate("ModificarRecorrido", "MODIFICAR", None))
        self.bRegresarRecorrido.setText(_translate("ModificarRecorrido", "REGRESAR", None))


