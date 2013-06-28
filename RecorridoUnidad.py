# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RecorridoUnidad.ui'
#
# Created: Mon Jun 24 13:29:53 2013
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
        self.fechaFinalRU = QtGui.QDateEdit(Form)
        self.fechaFinalRU.setGeometry(QtCore.QRect(310, 170, 161, 27))
        self.fechaFinalRU.setObjectName(_fromUtf8("fechaFinalRU"))
        self.fechaInicialRU = QtGui.QDateEdit(Form)
        self.fechaInicialRU.setGeometry(QtCore.QRect(310, 120, 161, 27))
        self.fechaInicialRU.setObjectName(_fromUtf8("fechaInicialRU"))
        self.lfechaInicialRU = QtGui.QLabel(Form)
        self.lfechaInicialRU.setGeometry(QtCore.QRect(160, 120, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lfechaInicialRU.setFont(font)
        self.lfechaInicialRU.setObjectName(_fromUtf8("lfechaInicialRU"))
        self.lIDConductorRU = QtGui.QLabel(Form)
        self.lIDConductorRU.setGeometry(QtCore.QRect(160, 220, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lIDConductorRU.setFont(font)
        self.lIDConductorRU.setObjectName(_fromUtf8("lIDConductorRU"))
        self.lfechaFinalRU = QtGui.QLabel(Form)
        self.lfechaFinalRU.setGeometry(QtCore.QRect(180, 170, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lfechaFinalRU.setFont(font)
        self.lfechaFinalRU.setObjectName(_fromUtf8("lfechaFinalRU"))
        self.TitleRecorridoUnidad = QtGui.QLabel(Form)
        self.TitleRecorridoUnidad.setGeometry(QtCore.QRect(160, 40, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.TitleRecorridoUnidad.setFont(font)
        self.TitleRecorridoUnidad.setObjectName(_fromUtf8("TitleRecorridoUnidad"))
        self.lineIDConductorRU = QtGui.QLineEdit(Form)
        self.lineIDConductorRU.setGeometry(QtCore.QRect(280, 220, 211, 27))
        self.lineIDConductorRU.setObjectName(_fromUtf8("lineIDConductorRU"))
        self.buscarRH = QtGui.QPushButton(Form)
        self.buscarRH.setGeometry(QtCore.QRect(130, 260, 401, 27))
        self.buscarRH.setObjectName(_fromUtf8("buscarRH"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.lfechaInicialRU.setText(_translate("Form", " FECHA INICIAL", None))
        self.lIDConductorRU.setText(_translate("Form", "ID UNIDAD", None))
        self.lfechaFinalRU.setText(_translate("Form", "FECHA FINAL", None))
        self.TitleRecorridoUnidad.setText(_translate("Form", "RECORRIDOS POR UNIDAD", None))
        self.buscarRH.setText(_translate("Form", "CONSULTAR", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

