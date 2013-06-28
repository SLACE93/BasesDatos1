# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Consultas.ui'
#
# Created: Mon Jun 24 13:40:25 2013
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(640, 515)
        self.labelConsultas = QtGui.QLabel(Form)
        self.labelConsultas.setGeometry(QtCore.QRect(250, 60, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelConsultas.setFont(font)
        self.labelConsultas.setObjectName(_fromUtf8("labelConsultas"))
        self.bRecorridoFecha = QtGui.QPushButton(Form)
        self.bRecorridoFecha.setGeometry(QtCore.QRect(170, 130, 301, 41))
        self.bRecorridoFecha.setObjectName(_fromUtf8("bRecorridoFecha"))
        self.bRecorridoConductor = QtGui.QPushButton(Form)
        self.bRecorridoConductor.setGeometry(QtCore.QRect(170, 190, 301, 41))
        self.bRecorridoConductor.setObjectName(_fromUtf8("bRecorridoConductor"))
        self.RecorridoUnidad = QtGui.QPushButton(Form)
        self.RecorridoUnidad.setGeometry(QtCore.QRect(170, 250, 301, 41))
        self.RecorridoUnidad.setObjectName(_fromUtf8("RecorridoUnidad"))
        self.bRecorridoHoras = QtGui.QPushButton(Form)
        self.bRecorridoHoras.setGeometry(QtCore.QRect(170, 310, 301, 41))
        self.bRecorridoHoras.setObjectName(_fromUtf8("bRecorridoHoras"))
        self.bRegresar = QtGui.QPushButton(Form)
        self.bRegresar.setGeometry(QtCore.QRect(350, 390, 211, 31))
        self.bRegresar.setObjectName(_fromUtf8("bRegresar"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.labelConsultas.setText(_translate("Form", "CONSULTAS", None))
        self.bRecorridoFecha.setText(_translate("Form", "RECORRIDOS POR FECHA", None))
        self.bRecorridoConductor.setText(_translate("Form", "RECORRIDOS POR CONDUCTOR", None))
        self.RecorridoUnidad.setText(_translate("Form", "RECORRIDOS POR UNIDAD", None))
        self.bRecorridoHoras.setText(_translate("Form", "RECORRIDOS POR HORAS", None))
        self.bRegresar.setText(_translate("Form", "REGRESAR", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

