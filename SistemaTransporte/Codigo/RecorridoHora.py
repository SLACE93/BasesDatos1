# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RecorridoHora.ui'
#
# Created: Sat Jul 27 13:12:23 2013
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
        self.lFechaRH = QtGui.QLabel(RecorridoHoras)
        self.lFechaRH.setGeometry(QtCore.QRect(240, 80, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lFechaRH.setFont(font)
        self.lFechaRH.setObjectName(_fromUtf8("lFechaRH"))
        self.lestacionSalidaRH = QtGui.QLabel(RecorridoHoras)
        self.lestacionSalidaRH.setGeometry(QtCore.QRect(110, 120, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lestacionSalidaRH.setFont(font)
        self.lestacionSalidaRH.setObjectName(_fromUtf8("lestacionSalidaRH"))
        self.TitleRecorridoHora = QtGui.QLabel(RecorridoHoras)
        self.TitleRecorridoHora.setGeometry(QtCore.QRect(160, 20, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.TitleRecorridoHora.setFont(font)
        self.TitleRecorridoHora.setObjectName(_fromUtf8("TitleRecorridoHora"))
        self.fechaInicialRU = QtGui.QDateEdit(RecorridoHoras)
        self.fechaInicialRU.setGeometry(QtCore.QRect(320, 80, 131, 27))
        self.fechaInicialRU.setObjectName(_fromUtf8("fechaInicialRU"))
        self.lestacionLLegadaRH = QtGui.QLabel(RecorridoHoras)
        self.lestacionLLegadaRH.setGeometry(QtCore.QRect(90, 160, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lestacionLLegadaRH.setFont(font)
        self.lestacionLLegadaRH.setObjectName(_fromUtf8("lestacionLLegadaRH"))
        self.cbEstacionSRH = QtGui.QComboBox(RecorridoHoras)
        self.cbEstacionSRH.setGeometry(QtCore.QRect(290, 120, 231, 27))
        self.cbEstacionSRH.setObjectName(_fromUtf8("cbEstacionSRH"))
        self.cbEstacionSRH.addItem(_fromUtf8(""))
        self.cbEstacionSRH.addItem(_fromUtf8(""))
        self.cbEstacionSRH.addItem(_fromUtf8(""))
        self.cbEstacionSRH.addItem(_fromUtf8(""))
        self.cbEstacionSRH.addItem(_fromUtf8(""))
        self.cbEstacionSRH.addItem(_fromUtf8(""))
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
        self.lHoraInicialRH.setGeometry(QtCore.QRect(40, 200, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lHoraInicialRH.setFont(font)
        self.lHoraInicialRH.setObjectName(_fromUtf8("lHoraInicialRH"))
        self.lHoraFinalRH = QtGui.QLabel(RecorridoHoras)
        self.lHoraFinalRH.setGeometry(QtCore.QRect(330, 200, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lHoraFinalRH.setFont(font)
        self.lHoraFinalRH.setObjectName(_fromUtf8("lHoraFinalRH"))
        self.timeHoraInicialRH = QtGui.QTimeEdit(RecorridoHoras)
        self.timeHoraInicialRH.setGeometry(QtCore.QRect(180, 200, 118, 27))
        self.timeHoraInicialRH.setObjectName(_fromUtf8("timeHoraInicialRH"))
        self.timeHoraFinalRH = QtGui.QTimeEdit(RecorridoHoras)
        self.timeHoraFinalRH.setGeometry(QtCore.QRect(460, 200, 118, 27))
        self.timeHoraFinalRH.setObjectName(_fromUtf8("timeHoraFinalRH"))
        self.bingresarHoras = QtGui.QPushButton(RecorridoHoras)
        self.bingresarHoras.setGeometry(QtCore.QRect(350, 450, 240, 50))
        self.bingresarHoras.setObjectName(_fromUtf8("bingresarHoras"))
        self.bRegresarHoras = QtGui.QPushButton(RecorridoHoras)
        self.bRegresarHoras.setGeometry(QtCore.QRect(50, 450, 240, 50))
        self.bRegresarHoras.setObjectName(_fromUtf8("bRegresarHoras"))

        self.retranslateUi(RecorridoHoras)
        QtCore.QMetaObject.connectSlotsByName(RecorridoHoras)

    def retranslateUi(self, RecorridoHoras):
        RecorridoHoras.setWindowTitle(_translate("RecorridoHoras", "RecorridoHoras", None))
        self.lFechaRH.setText(_translate("RecorridoHoras", " FECHA", None))
        self.lestacionSalidaRH.setText(_translate("RecorridoHoras", "ESTACION SALIDA", None))
        self.TitleRecorridoHora.setText(_translate("RecorridoHoras", "RECORRIDOS POR HORAS", None))
        self.lestacionLLegadaRH.setText(_translate("RecorridoHoras", "ESTACION LLEGADA", None))
        self.cbEstacionSRH.setItemText(0, _translate("RecorridoHoras", "PISCINA OLIMPICA", None))
        self.cbEstacionSRH.setItemText(1, _translate("RecorridoHoras", "ESPOL", None))
        self.cbEstacionSRH.setItemText(2, _translate("RecorridoHoras", "ACACIAS", None))
        self.cbEstacionSRH.setItemText(3, _translate("RecorridoHoras", "TERMINAL", None))
        self.cbEstacionSRH.setItemText(4, _translate("RecorridoHoras", "ORQUIDEAS", None))
        self.cbEstacionSRH.setItemText(5, _translate("RecorridoHoras", "DURAN", None))
        self.cbEstacionLLRH.setItemText(0, _translate("RecorridoHoras", "PISCINA OLIMPICA", None))
        self.cbEstacionLLRH.setItemText(1, _translate("RecorridoHoras", "ESPOL", None))
        self.cbEstacionLLRH.setItemText(2, _translate("RecorridoHoras", "ACACIAS", None))
        self.cbEstacionLLRH.setItemText(3, _translate("RecorridoHoras", "TERMINAL", None))
        self.cbEstacionLLRH.setItemText(4, _translate("RecorridoHoras", "ORQUIDEAS", None))
        self.cbEstacionLLRH.setItemText(5, _translate("RecorridoHoras", "DURAN", None))
        self.lHoraInicialRH.setText(_translate("RecorridoHoras", "HORA INICIAL", None))
        self.lHoraFinalRH.setText(_translate("RecorridoHoras", "HORA FINAL", None))
        self.bingresarHoras.setText(_translate("RecorridoHoras", "CONSULTAR", None))
        self.bRegresarHoras.setText(_translate("RecorridoHoras", "REGRESAR", None))

