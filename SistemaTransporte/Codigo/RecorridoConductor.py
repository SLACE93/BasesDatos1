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
        RecorridoConductor.setStyleSheet(("background-image: url(imagenes/principal.jpg)"))
        self.lfechaFinalRC = QtGui.QLabel(RecorridoConductor)
        self.lfechaFinalRC.setGeometry(QtCore.QRect(190, 120, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lfechaFinalRC.setFont(font)
        self.lfechaFinalRC.setObjectName(_fromUtf8("lfechaFinalRC"))
        self.lineIDConductorRC = QtGui.QLineEdit(RecorridoConductor)
        self.lineIDConductorRC.setGeometry(QtCore.QRect(320, 160, 151, 27))
        self.lineIDConductorRC.setObjectName(_fromUtf8("lineIDConductorRC"))
        self.lIDConductorRC = QtGui.QLabel(RecorridoConductor)
        self.lIDConductorRC.setGeometry(QtCore.QRect(170, 160, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lIDConductorRC.setFont(font)
        self.lIDConductorRC.setObjectName(_fromUtf8("lIDConductorRC"))
        self.fechaInicialRC = QtGui.QDateEdit(RecorridoConductor)
        self.fechaInicialRC.setGeometry(QtCore.QRect(320, 80, 151, 27))
        self.fechaInicialRC.setObjectName(_fromUtf8("fechaInicialRC"))
        self.lfechaInicialRC = QtGui.QLabel(RecorridoConductor)
        self.lfechaInicialRC.setGeometry(QtCore.QRect(170, 80, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lfechaInicialRC.setFont(font)
        self.lfechaInicialRC.setObjectName(_fromUtf8("lfechaInicialRC"))
        self.fechaFinalRC = QtGui.QDateEdit(RecorridoConductor)
        self.fechaFinalRC.setDisplayFormat("dd/MM/yyyy")
        self.fechaFinalRC.setGeometry(QtCore.QRect(320, 120, 151, 27))
        self.fechaFinalRC.setObjectName(_fromUtf8("fechaFinalRC"))
        self.TitleRecorridoConductor = QtGui.QLabel(RecorridoConductor)
        self.TitleRecorridoConductor.setGeometry(QtCore.QRect(110, 30, 411, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.TitleRecorridoConductor.setFont(font)
        self.TitleRecorridoConductor.setObjectName(_fromUtf8("TitleRecorridoConductor"))
        self.tableViewRC = QtGui.QTableView(RecorridoConductor)
        self.tableViewRC.setGeometry(QtCore.QRect(30, 210, 570, 200))
        self.tableViewRC.setObjectName(_fromUtf8("tableViewRC"))
        self.bRegresarConductor = QtGui.QPushButton(RecorridoConductor)
        self.bRegresarConductor.setGeometry(QtCore.QRect(60, 440, 240, 50))
        self.bRegresarConductor.setObjectName(_fromUtf8("bRegresarConductor"))
        self.bConsultarConductor = QtGui.QPushButton(RecorridoConductor)
        self.bConsultarConductor.setGeometry(QtCore.QRect(320, 440, 240, 50))
        self.bConsultarConductor.setObjectName(_fromUtf8("bConsultarConductor"))

        self.retranslateUi(RecorridoConductor)
        QtCore.QMetaObject.connectSlotsByName(RecorridoConductor)

    def retranslateUi(self, RecorridoConductor):
        RecorridoConductor.setWindowTitle(_translate("RecorridoConductor", "Recorrido Conductor", None))
        self.lfechaFinalRC.setText(_translate("RecorridoConductor", "FECHA FINAL", None))
        self.lIDConductorRC.setText(_translate("RecorridoConductor", "ID CONDUCTOR", None))
        self.lfechaInicialRC.setText(_translate("RecorridoConductor", " FECHA INICIAL", None))
        self.TitleRecorridoConductor.setText(_translate("RecorridoConductor", "RECORRIDOS POR CONDUCTOR", None))