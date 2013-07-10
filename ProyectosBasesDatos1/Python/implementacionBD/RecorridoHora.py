# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recorridohoras.ui'
#
# Created: Tue Jul  9 17:56:06 2013
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

class Ui_RecorridoHoras(object):
    def setupUi(self, RecorridoHoras):
        RecorridoHoras.setObjectName(_fromUtf8("RecorridoHoras"))
        RecorridoHoras.resize(640, 520)
        self.buscarRH = QtGui.QPushButton(RecorridoHoras)
        self.buscarRH.setGeometry(QtCore.QRect(120, 300, 401, 27))
        self.buscarRH.setObjectName(_fromUtf8("buscarRH"))
        self.timeHoraInicialRH = QtGui.QTimeEdit(RecorridoHoras)
        self.timeHoraInicialRH.setGeometry(QtCore.QRect(340, 210, 118, 27))
        self.timeHoraInicialRH.setObjectName(_fromUtf8("timeHoraInicialRH"))
        self.lFechaRH = QtGui.QLabel(RecorridoHoras)
        self.lFechaRH.setGeometry(QtCore.QRect(240, 70, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lFechaRH.setFont(font)
        self.lFechaRH.setObjectName(_fromUtf8("lFechaRH"))
        self.timeHoraFinalRH = QtGui.QTimeEdit(RecorridoHoras)
        self.timeHoraFinalRH.setGeometry(QtCore.QRect(340, 260, 118, 27))
        self.timeHoraFinalRH.setObjectName(_fromUtf8("timeHoraFinalRH"))
        self.lestacionLLegadaRH = QtGui.QLabel(RecorridoHoras)
        self.lestacionLLegadaRH.setGeometry(QtCore.QRect(100, 160, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lestacionLLegadaRH.setFont(font)
        self.lestacionLLegadaRH.setObjectName(_fromUtf8("lestacionLLegadaRH"))
        self.fechaInicialRU = QtGui.QDateEdit(RecorridoHoras)
        self.fechaInicialRU.setGeometry(QtCore.QRect(320, 70, 131, 27))
        self.fechaInicialRU.setObjectName(_fromUtf8("fechaInicialRU"))
        self.cbEstacionSRH = QtGui.QComboBox(RecorridoHoras)
        self.cbEstacionSRH.setGeometry(QtCore.QRect(290, 110, 231, 27))
        self.cbEstacionSRH.setObjectName(_fromUtf8("cbEstacionSRH"))
        self.cbEstacionSRH.addItem(_fromUtf8(""))
        self.cbEstacionSRH.addItem(_fromUtf8(""))
        self.cbEstacionSRH.addItem(_fromUtf8(""))
        self.cbEstacionSRH.addItem(_fromUtf8(""))
        self.cbEstacionSRH.addItem(_fromUtf8(""))
        self.cbEstacionSRH.addItem(_fromUtf8(""))
        self.lHoraFinalRH = QtGui.QLabel(RecorridoHoras)
        self.lHoraFinalRH.setGeometry(QtCore.QRect(200, 260, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lHoraFinalRH.setFont(font)
        self.lHoraFinalRH.setObjectName(_fromUtf8("lHoraFinalRH"))
        self.TitleRecorridoHora = QtGui.QLabel(RecorridoHoras)
        self.TitleRecorridoHora.setGeometry(QtCore.QRect(170, 20, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.TitleRecorridoHora.setFont(font)
        self.TitleRecorridoHora.setObjectName(_fromUtf8("TitleRecorridoHora"))
        self.lestacionSalidaRH = QtGui.QLabel(RecorridoHoras)
        self.lestacionSalidaRH.setGeometry(QtCore.QRect(110, 110, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lestacionSalidaRH.setFont(font)
        self.lestacionSalidaRH.setObjectName(_fromUtf8("lestacionSalidaRH"))
        self.cbEstacionLLRH = QtGui.QComboBox(RecorridoHoras)
        self.cbEstacionLLRH.setGeometry(QtCore.QRect(290, 160, 231, 27))
        self.cbEstacionLLRH.setObjectName(_fromUtf8("cbEstacionLLRH"))
        self.cbEstacionLLRH.addItem(_fromUtf8(""))
        self.cbEstacionLLRH.addItem(_fromUtf8(""))
        self.cbEstacionLLRH.addItem(_fromUtf8(""))
        self.cbEstacionLLRH.addItem(_fromUtf8(""))
        self.cbEstacionLLRH.addItem(_fromUtf8(""))
        self.cbEstacionLLRH.addItem(_fromUtf8(""))
        self.lHoraInicialRH = QtGui.QLabel(RecorridoHoras)
        self.lHoraInicialRH.setGeometry(QtCore.QRect(200, 210, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lHoraInicialRH.setFont(font)
        self.lHoraInicialRH.setObjectName(_fromUtf8("lHoraInicialRH"))

        self.retranslateUi(RecorridoHoras)
        QtCore.QMetaObject.connectSlotsByName(RecorridoHoras)

    def retranslateUi(self, RecorridoHoras):
        RecorridoHoras.setWindowTitle(_translate("RecorridoHoras", "Form", None))
        self.buscarRH.setText(_translate("RecorridoHoras", "CONSULTAR", None))
        self.lFechaRH.setText(_translate("RecorridoHoras", " FECHA", None))
        self.lestacionLLegadaRH.setText(_translate("RecorridoHoras", "ESTACION LLEGADA", None))
        self.cbEstacionSRH.setItemText(0, _translate("RecorridoHoras", "PISCINA OLIMPICA", None))
        self.cbEstacionSRH.setItemText(1, _translate("RecorridoHoras", "ESPOL", None))
        self.cbEstacionSRH.setItemText(2, _translate("RecorridoHoras", "ACACIAS", None))
        self.cbEstacionSRH.setItemText(3, _translate("RecorridoHoras", "TERMINAL", None))
        self.cbEstacionSRH.setItemText(4, _translate("RecorridoHoras", "ORQUIDEAS", None))
        self.cbEstacionSRH.setItemText(5, _translate("RecorridoHoras", "DURAN", None))
        self.lHoraFinalRH.setText(_translate("RecorridoHoras", "HORA FINAL", None))
        self.TitleRecorridoHora.setText(_translate("RecorridoHoras", "RECORRIDOS POR HORAS", None))
        self.lestacionSalidaRH.setText(_translate("RecorridoHoras", "ESTACION SALIDA", None))
        self.cbEstacionLLRH.setItemText(0, _translate("RecorridoHoras", "PISCINA OLIMPICA", None))
        self.cbEstacionLLRH.setItemText(1, _translate("RecorridoHoras", "ESPOL", None))
        self.cbEstacionLLRH.setItemText(2, _translate("RecorridoHoras", "ACACIAS", None))
        self.cbEstacionLLRH.setItemText(3, _translate("RecorridoHoras", "TERMINAL", None))
        self.cbEstacionLLRH.setItemText(4, _translate("RecorridoHoras", "ORQUIDEAS", None))
        self.cbEstacionLLRH.setItemText(5, _translate("RecorridoHoras", "DURAN", None))
        self.lHoraInicialRH.setText(_translate("RecorridoHoras", "HORA INICIAL", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    RecorridoHoras = QtGui.QWidget()
    ui = Ui_RecorridoHoras()
    ui.setupUi(RecorridoHoras)
    RecorridoHoras.show()
    sys.exit(app.exec_())
