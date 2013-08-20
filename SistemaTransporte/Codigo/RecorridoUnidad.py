
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

class Ui_RecorridoUnidad(object):
    def setupUi(self, RecorridoUnidad):
        RecorridoUnidad.setObjectName(_fromUtf8("RecorridoUnidad"))
        RecorridoUnidad.resize(640, 520)
        RecorridoUnidad.setStyleSheet(("background-image: url(imagenes/principal.jpg)"))
        self.TitleRecorridoUnidad = QtGui.QLabel(RecorridoUnidad)
        self.TitleRecorridoUnidad.setStyleSheet("background-image: url()")
        self.TitleRecorridoUnidad.setGeometry(QtCore.QRect(170, 20, 351, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.TitleRecorridoUnidad.setFont(font)
        self.TitleRecorridoUnidad.setObjectName(_fromUtf8("TitleRecorridoUnidad"))
        self.comboBIDUnidadRU = ExtendedComboBox(RecorridoUnidad)
        self.comboBIDUnidadRU.setGeometry(QtCore.QRect(290, 70, 211, 27))
        self.comboBIDUnidadRU.setObjectName(_fromUtf8("comboBIDUnidadRU"))

        self.lIDUnidad = QtGui.QLabel(RecorridoUnidad)
        self.lIDUnidad.setStyleSheet("background-image: url()")
        self.lIDUnidad.setGeometry(QtCore.QRect(170, 70, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lIDUnidad.setFont(font)
        self.lIDUnidad.setObjectName(_fromUtf8("lIDUnidad"))

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.bConsultarRUnidad = QtGui.QPushButton(RecorridoUnidad)
        self.bConsultarRUnidad.setGeometry(QtCore.QRect(330, 440, 240, 50))
        self.bConsultarRUnidad.setObjectName(_fromUtf8("bConsultarRUnidad"))

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.bRegresarRUnidad = QtGui.QPushButton(RecorridoUnidad)
        self.bRegresarRUnidad.setGeometry(QtCore.QRect(50, 440, 240, 50))
        self.bRegresarRUnidad.setObjectName(_fromUtf8("bRegresarRUnidad"))
        self.tableViewRU = QtGui.QTableView(RecorridoUnidad)
        self.tableViewRU.setGeometry(QtCore.QRect(30, 120, 570, 300))
        self.tableViewRU.setStyleSheet("background-image: url()")
        self.tableViewRU.setObjectName(_fromUtf8("tableViewRU"))

        self.retranslateUi(RecorridoUnidad)
        QtCore.QMetaObject.connectSlotsByName(RecorridoUnidad)

    def retranslateUi(self, RecorridoUnidad):
        RecorridoUnidad.setWindowTitle(_translate("RecorridoUnidad", "Recorrido Unidad", None))
        self.TitleRecorridoUnidad.setText(_translate("RecorridoUnidad", "RECORRIDOS POR UNIDAD", None))
        self.lIDUnidad.setText(_translate("RecorridoUnidad", "ID UNIDAD", None))
