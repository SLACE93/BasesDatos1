# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recorridounidad.ui'
#
# Created: Tue Jul  9 17:55:46 2013
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

class Ui_RecorridoUnidad(object):
    def setupUi(self, RecorridoUnidad):
        RecorridoUnidad.setObjectName(_fromUtf8("RecorridoUnidad"))
        RecorridoUnidad.resize(640, 520)
        self.TitleRecorridoUnidad = QtGui.QLabel(RecorridoUnidad)
        self.TitleRecorridoUnidad.setGeometry(QtCore.QRect(140, 40, 351, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.TitleRecorridoUnidad.setFont(font)
        self.TitleRecorridoUnidad.setObjectName(_fromUtf8("TitleRecorridoUnidad"))
        self.lineIDConductorRU = QtGui.QLineEdit(RecorridoUnidad)
        self.lineIDConductorRU.setGeometry(QtCore.QRect(270, 220, 211, 27))
        self.lineIDConductorRU.setObjectName(_fromUtf8("lineIDConductorRU"))
        self.fechaFinalRU = QtGui.QDateEdit(RecorridoUnidad)
        self.fechaFinalRU.setGeometry(QtCore.QRect(300, 170, 161, 27))
        self.fechaFinalRU.setObjectName(_fromUtf8("fechaFinalRU"))
        self.lIDConductorRU = QtGui.QLabel(RecorridoUnidad)
        self.lIDConductorRU.setGeometry(QtCore.QRect(150, 220, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lIDConductorRU.setFont(font)
        self.lIDConductorRU.setObjectName(_fromUtf8("lIDConductorRU"))
        self.lfechaFinalRU = QtGui.QLabel(RecorridoUnidad)
        self.lfechaFinalRU.setGeometry(QtCore.QRect(170, 170, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lfechaFinalRU.setFont(font)
        self.lfechaFinalRU.setObjectName(_fromUtf8("lfechaFinalRU"))
        self.buscarRH = QtGui.QPushButton(RecorridoUnidad)
        self.buscarRH.setGeometry(QtCore.QRect(120, 260, 401, 27))
        self.buscarRH.setObjectName(_fromUtf8("buscarRH"))
        self.fechaInicialRU = QtGui.QDateEdit(RecorridoUnidad)
        self.fechaInicialRU.setGeometry(QtCore.QRect(300, 120, 161, 27))
        self.fechaInicialRU.setObjectName(_fromUtf8("fechaInicialRU"))
        self.lfechaInicialRU = QtGui.QLabel(RecorridoUnidad)
        self.lfechaInicialRU.setGeometry(QtCore.QRect(150, 120, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lfechaInicialRU.setFont(font)
        self.lfechaInicialRU.setObjectName(_fromUtf8("lfechaInicialRU"))

        self.retranslateUi(RecorridoUnidad)
        QtCore.QMetaObject.connectSlotsByName(RecorridoUnidad)

    def retranslateUi(self, RecorridoUnidad):
        RecorridoUnidad.setWindowTitle(_translate("RecorridoUnidad", "Form", None))
        self.TitleRecorridoUnidad.setText(_translate("RecorridoUnidad", "RECORRIDOS POR UNIDAD", None))
        self.lIDConductorRU.setText(_translate("RecorridoUnidad", "ID UNIDAD", None))
        self.lfechaFinalRU.setText(_translate("RecorridoUnidad", "FECHA FINAL", None))
        self.buscarRH.setText(_translate("RecorridoUnidad", "CONSULTAR", None))
        self.lfechaInicialRU.setText(_translate("RecorridoUnidad", " FECHA INICIAL", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    RecorridoUnidad = QtGui.QWidget()
    ui = Ui_RecorridoUnidad()
    ui.setupUi(RecorridoUnidad)
    RecorridoUnidad.show()
    sys.exit(app.exec_())

