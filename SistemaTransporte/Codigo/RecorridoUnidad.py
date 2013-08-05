
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

class Ui_RecorridoUnidad(object):
    def setupUi(self, RecorridoUnidad):
        RecorridoUnidad.setObjectName(_fromUtf8("RecorridoUnidad"))
        RecorridoUnidad.resize(640, 520)
        RecorridoUnidad.setStyleSheet(("background-image: url(imagenes/principal.jpg)"))
        self.TitleRecorridoUnidad = QtGui.QLabel(RecorridoUnidad)
        self.TitleRecorridoUnidad.setGeometry(QtCore.QRect(170, 20, 351, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.TitleRecorridoUnidad.setFont(font)
        self.TitleRecorridoUnidad.setObjectName(_fromUtf8("TitleRecorridoUnidad"))
        self.lineIDConductorRU = QtGui.QLineEdit(RecorridoUnidad)
        self.lineIDConductorRU.setGeometry(QtCore.QRect(290, 160, 211, 27))
        self.lineIDConductorRU.setObjectName(_fromUtf8("lineIDConductorRU"))
        self.dfechaFinalRU = QtGui.QDateEdit(RecorridoUnidad)
        self.dfechaFinalRU.setGeometry(QtCore.QRect(320, 120, 161, 27))
        self.dfechaFinalRU.setObjectName(_fromUtf8("dfechaFinalRU"))
        self.lIDUnidad = QtGui.QLabel(RecorridoUnidad)
        self.lIDUnidad.setGeometry(QtCore.QRect(170, 160, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lIDUnidad.setFont(font)
        self.lIDUnidad.setObjectName(_fromUtf8("lIDUnidad"))
        self.lFechaF = QtGui.QLabel(RecorridoUnidad)
        self.lFechaF.setGeometry(QtCore.QRect(190, 120, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lFechaF.setFont(font)
        self.lFechaF.setObjectName(_fromUtf8("lFechaF"))
        self.bConsultarRUnidad = QtGui.QPushButton(RecorridoUnidad)
        self.bConsultarRUnidad.setGeometry(QtCore.QRect(330, 440, 240, 50))
        self.bConsultarRUnidad.setObjectName(_fromUtf8("bConsultarRUnidad"))
        self.dfechaInicialRU = QtGui.QDateEdit(RecorridoUnidad)
        self.dfechaInicialRU.setGeometry(QtCore.QRect(320, 80, 161, 27))
        self.dfechaInicialRU.setObjectName(_fromUtf8("dfechaInicialRU"))
        self.lFechaI = QtGui.QLabel(RecorridoUnidad)
        self.lFechaI.setGeometry(QtCore.QRect(170, 80, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lFechaI.setFont(font)
        self.lFechaI.setObjectName(_fromUtf8("lFechaI"))
        self.bRegresarRUnidad = QtGui.QPushButton(RecorridoUnidad)
        self.bRegresarRUnidad.setGeometry(QtCore.QRect(50, 440, 240, 50))
        self.bRegresarRUnidad.setObjectName(_fromUtf8("bRegresarRUnidad"))
        self.tableViewRU = QtGui.QTableView(RecorridoUnidad)
        self.tableViewRU.setGeometry(QtCore.QRect(30, 221, 570, 200))
        self.tableViewRU.setObjectName(_fromUtf8("tableViewRU"))

        self.retranslateUi(RecorridoUnidad)
        QtCore.QMetaObject.connectSlotsByName(RecorridoUnidad)

    def retranslateUi(self, RecorridoUnidad):
        RecorridoUnidad.setWindowTitle(_translate("RecorridoUnidad", "Recorrido Unidad", None))
        self.TitleRecorridoUnidad.setText(_translate("RecorridoUnidad", "RECORRIDOS POR UNIDAD", None))
        self.lIDUnidad.setText(_translate("RecorridoUnidad", "ID UNIDAD", None))
        self.lFechaF.setText(_translate("RecorridoUnidad", "FECHA FINAL", None))
        self.lFechaI.setText(_translate("RecorridoUnidad", " FECHA INICIAL", None))