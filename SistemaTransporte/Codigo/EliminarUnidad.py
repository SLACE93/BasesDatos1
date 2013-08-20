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

class Ui_EliminarUnidad(object):
    def setupUi(self, EliminarUnidad):
        EliminarUnidad.setObjectName(_fromUtf8("EliminarUnidad"))
        EliminarUnidad.resize(640, 520)
        EliminarUnidad.setStyleSheet(("background-image: url(imagenes/principal.jpg)"))
        self.labelEliminar = QtGui.QLabel(EliminarUnidad)
        self.labelEliminar.setGeometry(QtCore.QRect(200, 60, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelEliminar.setFont(font)
        self.labelEliminar.setObjectName(_fromUtf8("labelEliminar"))
        self.bEliminarUnidad = QtGui.QPushButton(EliminarUnidad)
        self.bEliminarUnidad.setGeometry(QtCore.QRect(60, 430, 240, 50))
        self.bEliminarUnidad.setObjectName(_fromUtf8("bEliminarUnidad"))
        self.lIDUnidad = QtGui.QLabel(EliminarUnidad)
        self.lIDUnidad.setGeometry(QtCore.QRect(280, 200, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lIDUnidad.setFont(font)
        self.lIDUnidad.setObjectName(_fromUtf8("lIDUnidad"))
        self.cboxIDUnidad = QtGui.QComboBox(EliminarUnidad)
        self.cboxIDUnidad.setGeometry(QtCore.QRect(170, 260, 321, 31))
        self.cboxIDUnidad.setObjectName(_fromUtf8("cboxIDUnidad"))
        self.bRegresarEUnidad = QtGui.QPushButton(EliminarUnidad)
        self.bRegresarEUnidad.setGeometry(QtCore.QRect(340, 430, 240, 50))
        self.bRegresarEUnidad.setObjectName(_fromUtf8("bRegresarEUnidad"))

        self.retranslateUi(EliminarUnidad)
        QtCore.QMetaObject.connectSlotsByName(EliminarUnidad)

    def retranslateUi(self, EliminarUnidad):
        EliminarUnidad.setWindowTitle(_translate("EliminarUnidad", "EliminarUnidad", None))
        self.labelEliminar.setText(_translate("EliminarUnidad", "ELIMINAR UNIDAD", None))
        self.bEliminarUnidad.setText(_translate("EliminarUnidad", "ELIMINAR", None))
        self.lIDUnidad.setText(_translate("EliminarUnidad", "IDUnidad", None))
        self.bRegresarEUnidad.setText(_translate("EliminarUnidad", "REGRESAR", None))