
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

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)

        self.timeHoraFinalRH = QtGui.QTimeEdit(RecorridoHoras)
        self.timeHoraFinalRH.setGeometry(QtCore.QRect(460, 90, 118, 27))
        self.timeHoraFinalRH.setObjectName(_fromUtf8("timeHoraFinalRH"))

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)

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

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)

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
        self.lHoraFinalRH.setText(_translate("RecorridoHoras", "HORA FINAL", None))
        self.TitleRecorridoHora.setText(_translate("RecorridoHoras", "RECORRIDOS POR HORAS", None))
        self.lHoraInicialRH.setText(_translate("RecorridoHoras", "HORA INICIAL", None))
