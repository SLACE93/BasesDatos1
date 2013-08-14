
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
        RecorridoHoras.setStyleSheet(("background-image: url(imagenes/principal.jpg)"))
        self.timeHoraInicialRH = QtGui.QTimeEdit(RecorridoHoras)
        self.timeHoraInicialRH.setGeometry(QtCore.QRect(170, 90, 118, 27))
        self.timeHoraInicialRH.setObjectName(_fromUtf8("timeHoraInicialRH"))
        '''self.lFechaRH = QtGui.QLabel(RecorridoHoras)
        self.lFechaRH.setStyleSheet("background-image: url()")
        self.lFechaRH.setGeometry(QtCore.QRect(240, 70, 71, 20))'''
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        '''self.lFechaRH.setFont(font)
        self.lFechaRH.setObjectName(_fromUtf8("lFechaRH"))'''
        self.timeHoraFinalRH = QtGui.QTimeEdit(RecorridoHoras)
        self.timeHoraFinalRH.setGeometry(QtCore.QRect(460, 90, 118, 27))
        self.timeHoraFinalRH.setObjectName(_fromUtf8("timeHoraFinalRH"))
        '''self.lEstacionLLRH = QtGui.QLabel(RecorridoHoras)
        self.lEstacionLLRH.setStyleSheet("background-image: url()")
        self.lEstacionLLRH.setGeometry(QtCore.QRect(90, 150, 191, 20))'''
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        '''self.lEstacionLLRH.setFont(font)
        self.lEstacionLLRH.setObjectName(_fromUtf8("lEstacionLLRH"))
        self.fechaInicialRU = QtGui.QDateEdit(RecorridoHoras)
        self.fechaInicialRU.setGeometry(QtCore.QRect(320, 70, 131, 27))
        self.fechaInicialRU.setObjectName(_fromUtf8("fechaInicialRU"))'''
        '''self.cbEstacionSRH = QtGui.QComboBox(RecorridoHoras)
        self.cbEstacionSRH.setGeometry(QtCore.QRect(290, 110, 231, 27))
        self.cbEstacionSRH.setObjectName(_fromUtf8("cbEstacionSRH"))
        self.cbEstacionSRH.addItem(_fromUtf8(""))
        self.cbEstacionSRH.addItem(_fromUtf8(""))
        self.cbEstacionSRH.addItem(_fromUtf8(""))
        self.cbEstacionSRH.addItem(_fromUtf8(""))
        self.cbEstacionSRH.addItem(_fromUtf8(""))
        self.cbEstacionSRH.addItem(_fromUtf8(""))'''
        self.lHoraFinalRH = QtGui.QLabel(RecorridoHoras)
        self.lHoraFinalRH.setStyleSheet("background-image: url()")
        self.lHoraFinalRH.setGeometry(QtCore.QRect(330, 90, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lHoraFinalRH.setFont(font)
        self.lHoraFinalRH.setObjectName(_fromUtf8("lHoraFinalRH"))
        self.TitleRecorridoHora = QtGui.QLabel(RecorridoHoras)
        self.TitleRecorridoHora.setStyleSheet("background-image: url()")
        self.TitleRecorridoHora.setGeometry(QtCore.QRect(170, 20, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.TitleRecorridoHora.setFont(font)
        self.TitleRecorridoHora.setObjectName(_fromUtf8("TitleRecorridoHora"))
        '''self.lEstacionSRH = QtGui.QLabel(RecorridoHoras)
        self.lEstacionSRH.setStyleSheet("background-image: url()")
        self.lEstacionSRH.setGeometry(QtCore.QRect(110, 110, 171, 20))'''
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        '''self.lEstacionSRH.setFont(font)
        self.lEstacionSRH.setObjectName(_fromUtf8("lEstacionSRH"))
        self.cbEstacionLLRH = QtGui.QComboBox(RecorridoHoras)
        self.cbEstacionLLRH.setGeometry(QtCore.QRect(290, 150, 231, 27))
        self.cbEstacionLLRH.setObjectName(_fromUtf8("cbEstacionLLRH"))
        self.cbEstacionLLRH.addItem(_fromUtf8(""))
        self.cbEstacionLLRH.addItem(_fromUtf8(""))
        self.cbEstacionLLRH.addItem(_fromUtf8(""))
        self.cbEstacionLLRH.addItem(_fromUtf8(""))
        self.cbEstacionLLRH.addItem(_fromUtf8(""))
        self.cbEstacionLLRH.addItem(_fromUtf8(""))'''
        self.lHoraInicialRH = QtGui.QLabel(RecorridoHoras)
        self.lHoraInicialRH.setStyleSheet("background-image: url()")
        self.lHoraInicialRH.setGeometry(QtCore.QRect(30, 90, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lHoraInicialRH.setFont(font)
        self.lHoraInicialRH.setObjectName(_fromUtf8("lHoraInicialRH"))
        self.bRegresarHoras = QtGui.QPushButton(RecorridoHoras)
        self.bRegresarHoras.setGeometry(QtCore.QRect(50, 450, 240, 50))
        self.bRegresarHoras.setObjectName(_fromUtf8("bRegresarHoras"))
        self.bConsultarHoras = QtGui.QPushButton(RecorridoHoras)
        self.bConsultarHoras.setGeometry(QtCore.QRect(330, 450, 240, 50))
        self.bConsultarHoras.setObjectName(_fromUtf8("bConsultarHoras"))
        self.tableViewRH = QtGui.QTableView(RecorridoHoras)
        self.tableViewRH.setGeometry(QtCore.QRect(30, 140, 570, 300))
        self.tableViewRH.setStyleSheet("background-image: url()")
        self.tableViewRH.setObjectName(_fromUtf8("tableViewRH"))

        self.retranslateUi(RecorridoHoras)
        QtCore.QMetaObject.connectSlotsByName(RecorridoHoras)

    def retranslateUi(self, RecorridoHoras):
        RecorridoHoras.setWindowTitle(_translate("RecorridoHoras", "Recorrido Hora", None))
        '''self.lFechaRH.setText(_translate("RecorridoHoras", " FECHA", None))
        self.lEstacionLLRH.setText(_translate("RecorridoHoras", "ESTACION LLEGADA", None))
        self.cbEstacionSRH.setItemText(0, _translate("RecorridoHoras", "PISCINA OLIMPICA", None))
        self.cbEstacionSRH.setItemText(1, _translate("RecorridoHoras", "ESPOL", None))
        self.cbEstacionSRH.setItemText(2, _translate("RecorridoHoras", "ACACIAS", None))
        self.cbEstacionSRH.setItemText(3, _translate("RecorridoHoras", "TERMINAL", None))
        self.cbEstacionSRH.setItemText(4, _translate("RecorridoHoras", "ORQUIDEAS", None))
        self.cbEstacionSRH.setItemText(5, _translate("RecorridoHoras", "DURAN", None))'''
        self.lHoraFinalRH.setText(_translate("RecorridoHoras", "HORA FINAL", None))
        self.TitleRecorridoHora.setText(_translate("RecorridoHoras", "RECORRIDOS POR HORAS", None))
        '''self.lEstacionSRH.setText(_translate("RecorridoHoras", "ESTACION SALIDA", None))
        self.cbEstacionLLRH.setItemText(0, _translate("RecorridoHoras", "PISCINA OLIMPICA", None))
        self.cbEstacionLLRH.setItemText(1, _translate("RecorridoHoras", "ESPOL", None))
        self.cbEstacionLLRH.setItemText(2, _translate("RecorridoHoras", "ACACIAS", None))
        self.cbEstacionLLRH.setItemText(3, _translate("RecorridoHoras", "TERMINAL", None))
        self.cbEstacionLLRH.setItemText(4, _translate("RecorridoHoras", "ORQUIDEAS", None))
        self.cbEstacionLLRH.setItemText(5, _translate("RecorridoHoras", "DURAN", None))'''
        self.lHoraInicialRH.setText(_translate("RecorridoHoras", "HORA INICIAL", None))
