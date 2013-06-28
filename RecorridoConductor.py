# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RecorridoConductor.ui'
#
# Created: Mon Jun 24 13:29:09 2013
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
        Form.resize(640, 516)
        self.TitleRecorridoConductor = QtGui.QLabel(Form)
        self.TitleRecorridoConductor.setGeometry(QtCore.QRect(130, 50, 411, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.TitleRecorridoConductor.setFont(font)
        self.TitleRecorridoConductor.setObjectName(_fromUtf8("TitleRecorridoConductor"))
        self.lfechaFinalRC = QtGui.QLabel(Form)
        self.lfechaFinalRC.setGeometry(QtCore.QRect(200, 170, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lfechaFinalRC.setFont(font)
        self.lfechaFinalRC.setObjectName(_fromUtf8("lfechaFinalRC"))
        self.lfechaInicialRC = QtGui.QLabel(Form)
        self.lfechaInicialRC.setGeometry(QtCore.QRect(180, 130, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lfechaInicialRC.setFont(font)
        self.lfechaInicialRC.setObjectName(_fromUtf8("lfechaInicialRC"))
        self.fechaInicialRC = QtGui.QDateEdit(Form)
        self.fechaInicialRC.setGeometry(QtCore.QRect(330, 130, 151, 27))
        self.fechaInicialRC.setObjectName(_fromUtf8("fechaInicialRC"))
        self.lIDConductorRC = QtGui.QLabel(Form)
        self.lIDConductorRC.setGeometry(QtCore.QRect(180, 210, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lIDConductorRC.setFont(font)
        self.lIDConductorRC.setObjectName(_fromUtf8("lIDConductorRC"))
        self.lineIDConductorRC = QtGui.QLineEdit(Form)
        self.lineIDConductorRC.setGeometry(QtCore.QRect(330, 210, 151, 27))
        self.lineIDConductorRC.setObjectName(_fromUtf8("lineIDConductorRC"))
        self.buscarRH = QtGui.QPushButton(Form)
        self.buscarRH.setGeometry(QtCore.QRect(130, 260, 401, 27))
        self.buscarRH.setObjectName(_fromUtf8("buscarRH"))
        self.fechaInicialRC_2 = QtGui.QDateEdit(Form)
        self.fechaInicialRC_2.setGeometry(QtCore.QRect(330, 170, 151, 27))
        self.fechaInicialRC_2.setObjectName(_fromUtf8("fechaInicialRC_2"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.TitleRecorridoConductor.setText(_translate("Form", "RECORRIDOS POR CONDUCTOR", None))
        self.lfechaFinalRC.setText(_translate("Form", "FECHA FINAL", None))
        self.lfechaInicialRC.setText(_translate("Form", " FECHA INICIAL", None))
        self.lIDConductorRC.setText(_translate("Form", "ID CONDUCTOR", None))
        self.buscarRH.setText(_translate("Form", "CONSULTAR", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

