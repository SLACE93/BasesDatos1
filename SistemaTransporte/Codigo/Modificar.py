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

class Ui_Modificar(object):
    def setupUi(self, Modificar):
        Modificar.setObjectName(_fromUtf8("Modificar"))
        Modificar.resize(640, 520)
        Modificar.setStyleSheet(("background-image: url(imagenes/principal.jpg)"))
        self.labelConsultas = QtGui.QLabel(Modificar)
        self.labelConsultas.setGeometry(QtCore.QRect(250, 60, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelConsultas.setFont(font)
        self.labelConsultas.setObjectName(_fromUtf8("labelConsultas"))
        self.bModificarUnidad = QtGui.QPushButton(Modificar)
        self.bModificarUnidad.setGeometry(QtCore.QRect(90, 320, 450, 50))
        self.bModificarUnidad.setObjectName(_fromUtf8("bModificarUnidad"))
        self.bModificarRecorrido = QtGui.QPushButton(Modificar)
        self.bModificarRecorrido.setGeometry(QtCore.QRect(90, 230, 450, 50))
        self.bModificarRecorrido.setObjectName(_fromUtf8("bModificarRecorrido"))
        self.bModificarConductor = QtGui.QPushButton(Modificar)
        self.bModificarConductor.setGeometry(QtCore.QRect(90, 140, 450, 50))
        self.bModificarConductor.setObjectName(_fromUtf8("bModificarConductor"))
        self.bRegresar = QtGui.QPushButton(Modificar)
        self.bRegresar.setGeometry(QtCore.QRect(360, 430, 240, 50))
        self.bRegresar.setObjectName(_fromUtf8("bRegresar"))

        self.retranslateUi(Modificar)
        QtCore.QMetaObject.connectSlotsByName(Modificar)

    def retranslateUi(self, Modificar):
        Modificar.setWindowTitle(_translate("Modificar", "Modificar", None))
        self.labelConsultas.setText(_translate("Modificar", "MODIFICAR", None))
        self.bModificarUnidad.setText(_translate("Modificar", "MODIFICAR UNIDAD", None))
        self.bModificarRecorrido.setText(_translate("Modificar", "MODIFICAR RECORRIDO", None))
        self.bModificarConductor.setText(_translate("Modificar", "MODIFICAR CONDUCTOR", None))
        self.bRegresar.setText(_translate("Modificar", "REGRESAR", None))


