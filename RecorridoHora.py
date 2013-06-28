# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RecorridoHora.ui'
#
# Created: Mon Jun 24 13:29:40 2013
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
        Form.resize(641, 515)
        self.lFechaRH = QtGui.QLabel(Form)
        self.lFechaRH.setGeometry(QtCore.QRect(240, 70, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lFechaRH.setFont(font)
        self.lFechaRH.setObjectName(_fromUtf8("lFechaRH"))
        self.buscarRH = QtGui.QPushButton(Form)
        self.buscarRH.setGeometry(QtCore.QRect(120, 300, 401, 27))
        self.buscarRH.setObjectName(_fromUtf8("buscarRH"))
        self.lestacionSalidaRH = QtGui.QLabel(Form)
        self.lestacionSalidaRH.setGeometry(QtCore.QRect(110, 110, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lestacionSalidaRH.setFont(font)
        self.lestacionSalidaRH.setObjectName(_fromUtf8("lestacionSalidaRH"))
        self.TitleRecorridoHora = QtGui.QLabel(Form)
        self.TitleRecorridoHora.setGeometry(QtCore.QRect(170, 20, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.TitleRecorridoHora.setFont(font)
        self.TitleRecorridoHora.setObjectName(_fromUtf8("TitleRecorridoHora"))
        self.fechaInicialRU = QtGui.QDateEdit(Form)
        self.fechaInicialRU.setGeometry(QtCore.QRect(320, 70, 131, 27))
        self.fechaInicialRU.setObjectName(_fromUtf8("fechaInicialRU"))
        self.lestacionLLegadaRH = QtGui.QLabel(Form)
        self.lestacionLLegadaRH.setGeometry(QtCore.QRect(100, 160, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lestacionLLegadaRH.setFont(font)
        self.lestacionLLegadaRH.setObjectName(_fromUtf8("lestacionLLegadaRH"))
        self.cbEstacionSRH = QtGui.QComboBox(Form)
        self.cbEstacionSRH.setGeometry(QtCore.QRect(290, 110, 231, 27))
        self.cbEstacionSRH.setObjectName(_fromUtf8("cbEstacionSRH"))
        self.cbEstacionSRH.addItem(_fromUtf8(""))
        self.cbEstacionSRH.addItem(_fromUtf8(""))
        self.cbEstacionSRH.addItem(_fromUtf8(""))
        self.cbEstacionSRH.addItem(_fromUtf8(""))
        self.cbEstacionSRH.addItem(_fromUtf8(""))
        self.cbEstacionSRH.addItem(_fromUtf8(""))
        self.cbEstacionLLRH = QtGui.QComboBox(Form)
        self.cbEstacionLLRH.setGeometry(QtCore.QRect(290, 160, 231, 27))
        self.cbEstacionLLRH.setObjectName(_fromUtf8("cbEstacionLLRH"))
        self.cbEstacionLLRH.addItem(_fromUtf8(""))
        self.cbEstacionLLRH.addItem(_fromUtf8(""))
        self.cbEstacionLLRH.addItem(_fromUtf8(""))
        self.cbEstacionLLRH.addItem(_fromUtf8(""))
        self.cbEstacionLLRH.addItem(_fromUtf8(""))
        self.cbEstacionLLRH.addItem(_fromUtf8(""))
        self.lHoraInicialRH = QtGui.QLabel(Form)
        self.lHoraInicialRH.setGeometry(QtCore.QRect(200, 210, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lHoraInicialRH.setFont(font)
        self.lHoraInicialRH.setObjectName(_fromUtf8("lHoraInicialRH"))
        self.lHoraFinalRH = QtGui.QLabel(Form)
        self.lHoraFinalRH.setGeometry(QtCore.QRect(200, 260, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lHoraFinalRH.setFont(font)
        self.lHoraFinalRH.setObjectName(_fromUtf8("lHoraFinalRH"))
        self.timeHoraInicialRH = QtGui.QTimeEdit(Form)
        self.timeHoraInicialRH.setGeometry(QtCore.QRect(340, 210, 118, 27))
        self.timeHoraInicialRH.setObjectName(_fromUtf8("timeHoraInicialRH"))
        self.timeHoraFinalRH = QtGui.QTimeEdit(Form)
        self.timeHoraFinalRH.setGeometry(QtCore.QRect(340, 260, 118, 27))
        self.timeHoraFinalRH.setObjectName(_fromUtf8("timeHoraFinalRH"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.lFechaRH.setText(_translate("Form", " FECHA", None))
        self.buscarRH.setText(_translate("Form", "CONSULTAR", None))
        self.lestacionSalidaRH.setText(_translate("Form", "ESTACION SALIDA", None))
        self.TitleRecorridoHora.setText(_translate("Form", "RECORRIDOS POR HORAS", None))
        self.lestacionLLegadaRH.setText(_translate("Form", "ESTACION LLEGADA", None))
        self.cbEstacionSRH.setItemText(0, _translate("Form", "PISCINA OLIMPICA", None))
        self.cbEstacionSRH.setItemText(1, _translate("Form", "ESPOL", None))
        self.cbEstacionSRH.setItemText(2, _translate("Form", "ACACIAS", None))
        self.cbEstacionSRH.setItemText(3, _translate("Form", "TERMINAL", None))
        self.cbEstacionSRH.setItemText(4, _translate("Form", "ORQUIDEAS", None))
        self.cbEstacionSRH.setItemText(5, _translate("Form", "DURAN", None))
        self.cbEstacionLLRH.setItemText(0, _translate("Form", "PISCINA OLIMPICA", None))
        self.cbEstacionLLRH.setItemText(1, _translate("Form", "ESPOL", None))
        self.cbEstacionLLRH.setItemText(2, _translate("Form", "ACACIAS", None))
        self.cbEstacionLLRH.setItemText(3, _translate("Form", "TERMINAL", None))
        self.cbEstacionLLRH.setItemText(4, _translate("Form", "ORQUIDEAS", None))
        self.cbEstacionLLRH.setItemText(5, _translate("Form", "DURAN", None))
        self.lHoraInicialRH.setText(_translate("Form", "HORA INICIAL", None))
        self.lHoraFinalRH.setText(_translate("Form", "HORA FINAL", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

