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

class Ui_Consultas(QtGui.QMainWindow):
    def setupUi(self, Consultas):
        Consultas.setObjectName(_fromUtf8("Consultas"))
        Consultas.resize(640, 515)
        self.labelConsultas = QtGui.QLabel(Consultas)
        self.labelConsultas.setGeometry(QtCore.QRect(250, 40, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelConsultas.setFont(font)
        self.labelConsultas.setObjectName(_fromUtf8("labelConsultas"))
        self.bRecorridoFecha = QtGui.QPushButton(Consultas)
        self.bRecorridoFecha.setGeometry(QtCore.QRect(100, 110, 450, 50))
        self.bRecorridoFecha.setObjectName(_fromUtf8("bRecorridoFecha"))
        self.bRecorridoConductor = QtGui.QPushButton(Consultas)
        self.bRecorridoConductor.setGeometry(QtCore.QRect(100, 180, 450, 50))
        self.bRecorridoConductor.setObjectName(_fromUtf8("bRecorridoConductor"))
        self.RecorridoUnidad = QtGui.QPushButton(Consultas)
        self.RecorridoUnidad.setGeometry(QtCore.QRect(100, 250, 450, 50))
        self.RecorridoUnidad.setObjectName(_fromUtf8("RecorridoUnidad"))
        self.bRecorridoHoras = QtGui.QPushButton(Consultas)
        self.bRecorridoHoras.setGeometry(QtCore.QRect(100, 320, 450, 50))
        self.bRecorridoHoras.setObjectName(_fromUtf8("bRecorridoHoras"))
        self.bRegresar = QtGui.QPushButton(Consultas)
        self.bRegresar.setGeometry(QtCore.QRect(340, 420, 240, 50))
        self.bRegresar.setObjectName(_fromUtf8("bRegresar"))

        self.retranslateUi(Consultas)
        QtCore.QMetaObject.connectSlotsByName(Consultas)

    def retranslateUi(self, Consultas):
        Consultas.setWindowTitle(_translate("Consultas", "Consultas", None))
        self.labelConsultas.setText(_translate("Consultas", "CONSULTAS", None))
        