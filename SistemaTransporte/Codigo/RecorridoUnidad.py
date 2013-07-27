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
        RecorridoUnidad.resize(640, 515)
        self.DateEFechaF = QtGui.QDateEdit(RecorridoUnidad)
        self.DateEFechaF.setGeometry(QtCore.QRect(310, 150, 161, 27))
        self.DateEFechaF.setObjectName(_fromUtf8("DateEFechaF"))
        self.DateEFechaI = QtGui.QDateEdit(RecorridoUnidad)
        self.DateEFechaI.setGeometry(QtCore.QRect(310, 100, 161, 27))
        self.DateEFechaI.setObjectName(_fromUtf8("DateEFechaI"))
        self.lFechaI = QtGui.QLabel(RecorridoUnidad)
        self.lFechaI.setGeometry(QtCore.QRect(160, 100, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lFechaI.setFont(font)
        self.lFechaI.setObjectName(_fromUtf8("lFechaI"))
        self.lIDUnidad = QtGui.QLabel(RecorridoUnidad)
        self.lIDUnidad.setGeometry(QtCore.QRect(160, 200, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lIDUnidad.setFont(font)
        self.lIDUnidad.setObjectName(_fromUtf8("lIDUnidad"))
        self.lFechaF = QtGui.QLabel(RecorridoUnidad)
        self.lFechaF.setGeometry(QtCore.QRect(180, 150, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lFechaF.setFont(font)
        self.lFechaF.setObjectName(_fromUtf8("lFechaF"))
        self.TitleRecorridoUnidad = QtGui.QLabel(RecorridoUnidad)
        self.TitleRecorridoUnidad.setGeometry(QtCore.QRect(150, 30, 351, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.TitleRecorridoUnidad.setFont(font)
        self.TitleRecorridoUnidad.setObjectName(_fromUtf8("TitleRecorridoUnidad"))
        self.lineIDUnidad = QtGui.QLineEdit(RecorridoUnidad)
        self.lineIDUnidad.setGeometry(QtCore.QRect(280, 200, 211, 27))
        self.lineIDUnidad.setObjectName(_fromUtf8("lineIDUnidad"))
        self.bConsultarRUnidad = QtGui.QPushButton(RecorridoUnidad)
        self.bConsultarRUnidad.setGeometry(QtCore.QRect(350, 450, 240, 50))
        self.bConsultarRUnidad.setObjectName(_fromUtf8("bConsultarRUnidad"))
        self.bRegresarRUnidad = QtGui.QPushButton(RecorridoUnidad)
        self.bRegresarRUnidad.setGeometry(QtCore.QRect(50, 450, 240, 50))
        self.bRegresarRUnidad.setObjectName(_fromUtf8("bRegresarRUnidad"))

        self.retranslateUi(RecorridoUnidad)
        QtCore.QMetaObject.connectSlotsByName(RecorridoUnidad)

    def retranslateUi(self, RecorridoUnidad):
        RecorridoUnidad.setWindowTitle(_translate("RecorridoUnidad", "RecorridoUnidad", None))
        self.lFechaI.setText(_translate("RecorridoUnidad", " FECHA INICIAL", None))
        self.lIDUnidad.setText(_translate("RecorridoUnidad", "ID UNIDAD", None))
        self.lFechaF.setText(_translate("RecorridoUnidad", "FECHA FINAL", None))
        self.TitleRecorridoUnidad.setText(_translate("RecorridoUnidad", "RECORRIDOS POR UNIDAD", None))
        self.bConsultarRUnidad.setText(_translate("RecorridoUnidad", "CONSULTAR", None))
        self.bRegresarRUnidad.setText(_translate("FoRecorridoUnidadrm", "REGRESAR", None))
