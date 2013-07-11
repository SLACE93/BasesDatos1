# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recorridofecha.ui'
#
# Created: Tue Jul 9 17:55:10 2013
# by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
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

class Ui_RecorridoFecha(object):
    def setupUi(self, RecorridoFecha):
        RecorridoFecha.setObjectName(_fromUtf8("RecorridoFecha"))
        RecorridoFecha.resize(640, 520)
        self.dateFechaInicial = QtGui.QDateEdit(RecorridoFecha)
        self.dateFechaInicial.setGeometry(QtCore.QRect(290, 150, 181, 27))
        self.dateFechaInicial.setObjectName(_fromUtf8("dateFechaInicial"))
        self.lFechaFinal = QtGui.QLabel(RecorridoFecha)
        self.lFechaFinal.setGeometry(QtCore.QRect(150, 210, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lFechaFinal.setFont(font)
        self.lFechaFinal.setObjectName(_fromUtf8("lFechaFinal"))
        self.dateFechaFinal = QtGui.QDateEdit(RecorridoFecha)
        self.dateFechaFinal.setGeometry(QtCore.QRect(290, 210, 181, 27))
        self.dateFechaFinal.setObjectName(_fromUtf8("dateFechaFinal"))
        self.buscarRH = QtGui.QPushButton(RecorridoFecha)
        self.buscarRH.setGeometry(QtCore.QRect(110, 260, 401, 27))
        self.buscarRH.setObjectName(_fromUtf8("buscarRH"))
        self.titleRecFecha = QtGui.QLabel(RecorridoFecha)
        self.titleRecFecha.setGeometry(QtCore.QRect(160, 50, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.titleRecFecha.setFont(font)
        self.titleRecFecha.setObjectName(_fromUtf8("titleRecFecha"))
        self.lFechaInicial = QtGui.QLabel(RecorridoFecha)
        self.lFechaInicial.setGeometry(QtCore.QRect(140, 150, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lFechaInicial.setFont(font)
        self.lFechaInicial.setObjectName(_fromUtf8("lFechaInicial"))

        self.retranslateUi(RecorridoFecha)
        QtCore.QMetaObject.connectSlotsByName(RecorridoFecha)

    def retranslateUi(self, RecorridoFecha):
        RecorridoFecha.setWindowTitle(_translate("RecorridoFecha", "Form", None))
        self.lFechaFinal.setText(_translate("RecorridoFecha", "FECHA FINAL", None))
        self.buscarRH.setText(_translate("RecorridoFecha", "CONSULTAR", None))
        self.titleRecFecha.setText(_translate("RecorridoFecha", "RECORRIDOS POR FECHA", None))
        self.lFechaInicial.setText(_translate("RecorridoFecha", "FECHA INICIAL", None))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    RecorridoFecha = QtGui.QWidget()
    ui = Ui_RecorridoFecha()
    ui.setupUi(RecorridoFecha)
    RecorridoFecha.show()
    sys.exit(app.exec_())