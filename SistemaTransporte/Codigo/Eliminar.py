

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

class Ui_Eliminar(object):
    def setupUi(self, Eliminar):
        Eliminar.setObjectName(_fromUtf8("Eliminar"))
        Eliminar.resize(640, 520)
        Eliminar.setStyleSheet(("background-image: url(imagenes/principal.jpg)"))
        
        self.labelEliminar = QtGui.QLabel(Eliminar)
        self.labelEliminar.setGeometry(QtCore.QRect(250, 60, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelEliminar.setFont(font)
        self.labelEliminar.setObjectName(_fromUtf8("labelEliminar"))
        self.bEliminarUnidad = QtGui.QPushButton(Eliminar)
        self.bEliminarUnidad.setGeometry(QtCore.QRect(90, 320, 450, 50))
        self.bEliminarUnidad.setObjectName(_fromUtf8("bEliminarUnidad"))
        self.bEliminarRecorrido = QtGui.QPushButton(Eliminar)
        self.bEliminarRecorrido.setGeometry(QtCore.QRect(90, 230, 450, 50))
        self.bEliminarRecorrido.setObjectName(_fromUtf8("bEliminarRecorrido"))
        self.bEliminarConductor = QtGui.QPushButton(Eliminar)
        self.bEliminarConductor.setGeometry(QtCore.QRect(90, 140, 450, 50))
        self.bEliminarConductor.setObjectName(_fromUtf8("bEliminarConductor"))
        self.bRegresarEliminar = QtGui.QPushButton(Eliminar)
        self.bRegresarEliminar.setGeometry(QtCore.QRect(360, 430, 240, 50))
        self.bRegresarEliminar.setObjectName(_fromUtf8("bRegresarEliminar"))

        self.retranslateUi(Eliminar)
        QtCore.QMetaObject.connectSlotsByName(Eliminar)

    def retranslateUi(self, Eliminar):
        Eliminar.setWindowTitle(_translate("Eliminar", "Form", None))
        self.labelEliminar.setText(_translate("Eliminar", "ELIMINAR", None))
        self.bEliminarUnidad.setText(_translate("Eliminar", "ELIMINAR UNIDAD", None))
        self.bEliminarRecorrido.setText(_translate("Eliminar", "ELIMINAR RECORRIDO", None))
        self.bEliminarConductor.setText(_translate("Eliminar", "ELIMINAR CONDUCTOR", None))
        self.bRegresarEliminar.setText(_translate("Eliminar", "REGRESAR", None))
