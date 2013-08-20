from PyQt4 import QtCore, QtGui
from comboBox import ExtendedComboBox

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

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)

        self.comboBIDConductorRC = ExtendedComboBox(RecorridoConductor)
        self.comboBIDConductorRC.setGeometry(QtCore.QRect(280, 85, 240, 27))
        self.comboBIDConductorRC.setObjectName(_fromUtf8("lineIDConductorRC"))

        self.lIDConductorRC = QtGui.QLabel(RecorridoConductor)
        self.lIDConductorRC.setStyleSheet("background-image: url()")
        self.lIDConductorRC.setGeometry(QtCore.QRect(100, 85, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lIDConductorRC.setFont(font)
        self.lIDConductorRC.setObjectName(_fromUtf8("lIDConductorRC"))

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)

        self.TitleRecorridoConductor = QtGui.QLabel(RecorridoConductor)
        self.TitleRecorridoConductor.setStyleSheet("background-image: url()")
        self.TitleRecorridoConductor.setGeometry(QtCore.QRect(110, 30, 411, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.TitleRecorridoConductor.setFont(font)
        self.TitleRecorridoConductor.setObjectName(_fromUtf8("TitleRecorridoConductor"))
        self.tableViewRC = QtGui.QTableView(RecorridoConductor)
        self.tableViewRC.setGeometry(QtCore.QRect(30, 130, 570, 300))
        self.tableViewRC.setStyleSheet("background-image: url()")
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
        self.lIDConductorRC.setText(_translate("RecorridoConductor", "ID CONDUCTOR", None))
        self.TitleRecorridoConductor.setText(_translate("RecorridoConductor", "RECORRIDOS POR CONDUCTOR", None))