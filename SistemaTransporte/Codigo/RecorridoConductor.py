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

class Ui_RecorridoConductor(object):
    def setupUi(self, RecorridoConductor):
        RecorridoConductor.setObjectName(_fromUtf8("RecorridoConductor"))
        RecorridoConductor.resize(640, 520)
        self.TitleRecorridoConductor = QtGui.QLabel(RecorridoConductor)
        self.TitleRecorridoConductor.setGeometry(QtCore.QRect(120, 50, 411, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.TitleRecorridoConductor.setFont(font)
        self.TitleRecorridoConductor.setObjectName(_fromUtf8("TitleRecorridoConductor"))
        self.lfechaFinalRC = QtGui.QLabel(RecorridoConductor)
        self.lfechaFinalRC.setGeometry(QtCore.QRect(190, 160, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lfechaFinalRC.setFont(font)
        self.lfechaFinalRC.setObjectName(_fromUtf8("lfechaFinalRC"))
        self.lfechaInicialRC = QtGui.QLabel(RecorridoConductor)
        self.lfechaInicialRC.setGeometry(QtCore.QRect(170, 120, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lfechaInicialRC.setFont(font)
        self.lfechaInicialRC.setObjectName(_fromUtf8("lfechaInicialRC"))
        self.fechaInicialRC = QtGui.QDateEdit(RecorridoConductor)
        self.fechaInicialRC.setGeometry(QtCore.QRect(330, 120, 151, 27))
        self.fechaInicialRC.setObjectName(_fromUtf8("fechaInicialRC"))
        self.lIDConductorRC = QtGui.QLabel(RecorridoConductor)
        self.lIDConductorRC.setGeometry(QtCore.QRect(160, 200, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lIDConductorRC.setFont(font)
        self.lIDConductorRC.setObjectName(_fromUtf8("lIDConductorRC"))
        self.lineIDConductorRC = QtGui.QLineEdit(RecorridoConductor)
        self.lineIDConductorRC.setGeometry(QtCore.QRect(330, 200, 151, 27))
        self.lineIDConductorRC.setObjectName(_fromUtf8("lineIDConductorRC"))
        self.fechaInicialRC_2 = QtGui.QDateEdit(RecorridoConductor)
        self.fechaInicialRC_2.setGeometry(QtCore.QRect(330, 160, 151, 27))
        self.fechaInicialRC_2.setObjectName(_fromUtf8("fechaInicialRC_2"))
        self.bRegresarConductor = QtGui.QPushButton(RecorridoConductor)
        self.bRegresarConductor.setGeometry(QtCore.QRect(50, 450, 240, 50))
        self.bRegresarConductor.setObjectName(_fromUtf8("bRegresarConductor"))
        self.bConsultarConductor = QtGui.QPushButton(RecorridoConductor)
        self.bConsultarConductor.setGeometry(QtCore.QRect(350, 450, 240, 50))
        self.bConsultarConductor.setObjectName(_fromUtf8("bConsultarConductor"))

        self.retranslateUi(RecorridoConductor)
        QtCore.QMetaObject.connectSlotsByName(RecorridoConductor)

    def retranslateUi(self, RecorridoConductor):
        RecorridoConductor.setWindowTitle(_translate("RecorridoConductor", "RecorridoConductor", None))
        self.TitleRecorridoConductor.setText(_translate("RecorridoConductor", "RECORRIDOS POR CONDUCTOR", None))
        self.lfechaFinalRC.setText(_translate("RecorridoConductor", "FECHA FINAL", None))
        self.lfechaInicialRC.setText(_translate("RecorridoConductor", " FECHA INICIAL", None))
        self.lIDConductorRC.setText(_translate("RecorridoConductor", "ID CONDUCTOR", None))
        self.bRegresarConductor.setText(_translate("RecorridoConductor", "REGRESAR", None))
        self.bConsultarConductor.setText(_translate("RecorridoConductor", "CONSULTAR", None))
