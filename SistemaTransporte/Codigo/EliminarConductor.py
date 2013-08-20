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

class Ui_EliminarConductor(object):
    def setupUi(self, EliminarConductor):
        EliminarConductor.setObjectName(_fromUtf8("EliminarConductor"))
        EliminarConductor.resize(640, 520)
        EliminarConductor.setStyleSheet(("background-image: url(imagenes/principal.jpg)"))
        self.labelConsultas = QtGui.QLabel(EliminarConductor)
        self.labelConsultas.setGeometry(QtCore.QRect(170, 60, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelConsultas.setFont(font)
        self.labelConsultas.setObjectName(_fromUtf8("labelConsultas"))
        self.bEliminarConductor = QtGui.QPushButton(EliminarConductor)
        self.bEliminarConductor.setGeometry(QtCore.QRect(60, 430, 240, 50))
        self.bEliminarConductor.setObjectName(_fromUtf8("bEliminarConductor"))
        self.lIDConductor = QtGui.QLabel(EliminarConductor)
        self.lIDConductor.setGeometry(QtCore.QRect(260, 200, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lIDConductor.setFont(font)
        self.lIDConductor.setObjectName(_fromUtf8("lIDConductor"))
        self.cboxIDConductor = QtGui.QComboBox(EliminarConductor)
        self.cboxIDConductor.setGeometry(QtCore.QRect(160, 260, 321, 31))
        self.cboxIDConductor.setObjectName(_fromUtf8("cboxIDConductor"))
        self.bRegresarEConductor = QtGui.QPushButton(EliminarConductor)
        self.bRegresarEConductor.setGeometry(QtCore.QRect(340, 430, 240, 50))
        self.bRegresarEConductor.setObjectName(_fromUtf8("bRegresarEConductor"))

        self.retranslateUi(EliminarConductor)
        QtCore.QMetaObject.connectSlotsByName(EliminarConductor)

    def retranslateUi(self, EliminarConductor):
        EliminarConductor.setWindowTitle(_translate("EliminarConductor", "EliminarConductor", None))
        self.labelConsultas.setText(_translate("EliminarConductor", "ELIMINAR CONDUCTOR", None))
        self.bEliminarConductor.setText(_translate("EliminarConductor", "ELIMINAR", None))
        self.lIDConductor.setText(_translate("EliminarConductor", "IDConductor", None))
        self.bRegresarEConductor.setText(_translate("EliminarConductor", "REGRESAR", None))

