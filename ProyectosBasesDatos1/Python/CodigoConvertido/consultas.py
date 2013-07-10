# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consultas.ui'
#
# Created: Tue Jul  9 17:53:49 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

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

class Ui_Consultas(object):
    def setupUi(self, Consultas):
        Consultas.setObjectName(_fromUtf8("Consultas"))
        Consultas.resize(640, 520)
        self.bRecorridoHoras = QtGui.QPushButton(Consultas)
        self.bRecorridoHoras.setGeometry(QtCore.QRect(170, 340, 301, 41))
        self.bRecorridoHoras.setObjectName(_fromUtf8("bRecorridoHoras"))
        self.RecorridoUnidad = QtGui.QPushButton(Consultas)
        self.RecorridoUnidad.setGeometry(QtCore.QRect(170, 280, 301, 41))
        self.RecorridoUnidad.setObjectName(_fromUtf8("RecorridoUnidad"))
        self.bRecorridoFecha = QtGui.QPushButton(Consultas)
        self.bRecorridoFecha.setGeometry(QtCore.QRect(170, 160, 301, 41))
        self.bRecorridoFecha.setObjectName(_fromUtf8("bRecorridoFecha"))
        self.bRegresar = QtGui.QPushButton(Consultas)
        self.bRegresar.setGeometry(QtCore.QRect(350, 420, 211, 31))
        self.bRegresar.setObjectName(_fromUtf8("bRegresar"))
        self.labelConsultas = QtGui.QLabel(Consultas)
        self.labelConsultas.setGeometry(QtCore.QRect(250, 90, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelConsultas.setFont(font)
        self.labelConsultas.setObjectName(_fromUtf8("labelConsultas"))
        self.bRecorridoConductor = QtGui.QPushButton(Consultas)
        self.bRecorridoConductor.setGeometry(QtCore.QRect(170, 220, 301, 41))
        self.bRecorridoConductor.setObjectName(_fromUtf8("bRecorridoConductor"))

        self.retranslateUi(Consultas)
        QtCore.QMetaObject.connectSlotsByName(Consultas)

    def retranslateUi(self, Consultas):
        Consultas.setWindowTitle(_translate("Consultas", "Form", None))
        self.bRecorridoHoras.setText(_translate("Consultas", "RECORRIDOS POR HORAS", None))
        self.RecorridoUnidad.setText(_translate("Consultas", "RECORRIDOS POR UNIDAD", None))
        self.bRecorridoFecha.setText(_translate("Consultas", "RECORRIDOS POR FECHA", None))
        self.bRegresar.setText(_translate("Consultas", "REGRESAR", None))
        self.labelConsultas.setText(_translate("Consultas", "CONSULTAS", None))
        self.bRecorridoConductor.setText(_translate("Consultas", "RECORRIDOS POR CONDUCTOR", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Consultas = QtGui.QWidget()
    ui = Ui_Consultas()
    ui.setupUi(Consultas)
    Consultas.show()
    sys.exit(app.exec_())

