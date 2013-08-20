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

class Ui_EliminarRecorrido(object):
    def setupUi(self, EliminarRecorrido):
        EliminarRecorrido.setObjectName(_fromUtf8("EliminarRecorrido"))
        EliminarRecorrido.resize(640, 520)
        EliminarRecorrido.setStyleSheet(("background-image: url(imagenes/principal.jpg)"))
        self.labelEliminar = QtGui.QLabel(EliminarRecorrido)
        self.labelEliminar.setStyleSheet(("background-image: url()")) 
        self.labelEliminar.setGeometry(QtCore.QRect(180, 60, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelEliminar.setFont(font)
        self.labelEliminar.setObjectName(_fromUtf8("labelEliminar"))
        self.bEliminarRecorrido = QtGui.QPushButton(EliminarRecorrido)
        self.bEliminarRecorrido.setGeometry(QtCore.QRect(60, 430, 240, 50))
        self.bEliminarRecorrido.setObjectName(_fromUtf8("bEliminarRecorrido"))
        self.lIDRecorrido = QtGui.QLabel(EliminarRecorrido)
        self.lIDRecorrido.setStyleSheet(("background-image: url()")) 
        self.lIDRecorrido.setGeometry(QtCore.QRect(270, 200, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lIDRecorrido.setFont(font)
        self.lIDRecorrido.setObjectName(_fromUtf8("lIDRecorrido"))
        self.cboxIDRecorrido = ExtendedComboBox(EliminarRecorrido)
        self.cboxIDRecorrido.setGeometry(QtCore.QRect(170, 260, 321, 31))
        self.cboxIDRecorrido.setObjectName(_fromUtf8("cboxIDRecorrido"))
        self.bRegresarERecorrido = QtGui.QPushButton(EliminarRecorrido)
        self.bRegresarERecorrido.setGeometry(QtCore.QRect(340, 430, 240, 50))
        self.bRegresarERecorrido.setObjectName(_fromUtf8("bRegresarERecorrido"))

        self.retranslateUi(EliminarRecorrido)
        QtCore.QMetaObject.connectSlotsByName(EliminarRecorrido)

    def retranslateUi(self, EliminarRecorrido):
        EliminarRecorrido.setWindowTitle(_translate("EliminarRecorrido", "EliminarRecorrido", None))
        self.labelEliminar.setText(_translate("EliminarRecorrido", "ELIMINAR RECORRIDO", None))
        self.bEliminarRecorrido.setText(_translate("EliminarRecorrido", "ELIMINAR", None))
        self.lIDRecorrido.setText(_translate("EliminarRecorrido", "IDRecorrido", None))
        self.bRegresarERecorrido.setText(_translate("EliminarRecorrido", "REGRESAR", None))
