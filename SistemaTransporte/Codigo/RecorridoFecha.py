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

class Ui_RecorridoFecha(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("RecorridoFecha"))
        Form.resize(640, 516)
        Form.setStyleSheet(("background-image: url(imagenes/principal.jpg)"))
        self.TitleRFecha = QtGui.QLabel(Form)
        self.TitleRFecha.setGeometry(QtCore.QRect(170, 20, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.TitleRFecha.setFont(font)
        self.TitleRFecha.setObjectName(_fromUtf8("TitleRFecha"))
        self.lFechaI = QtGui.QLabel(Form)
        self.lFechaI.setGeometry(QtCore.QRect(170, 100, 131, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lFechaI.setFont(font)
        self.lFechaI.setObjectName(_fromUtf8("lFechaI"))
        self.lFechaF = QtGui.QLabel(Form)
        self.lFechaF.setGeometry(QtCore.QRect(180, 160, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lFechaF.setFont(font)
        self.lFechaF.setObjectName(_fromUtf8("lFechaF"))
        self.dFechaInicial = QtGui.QDateEdit(Form)
        self.dFechaInicial.setGeometry(QtCore.QRect(310, 100, 181, 27))
        self.dFechaInicial.setObjectName(_fromUtf8("dFechaInicial"))
        self.dFechaFinal = QtGui.QDateEdit(Form)
        self.dFechaFinal.setGeometry(QtCore.QRect(310, 160, 181, 27))
        self.dFechaFinal.setObjectName(_fromUtf8("dFechaFinal"))
        self.bRegresarRFecha = QtGui.QPushButton(Form)
        self.bRegresarRFecha.setGeometry(QtCore.QRect(60, 450, 240, 50))
        self.bRegresarRFecha.setObjectName(_fromUtf8("bRegresarRFecha"))
        self.bConsultarRFecha = QtGui.QPushButton(Form)
        self.bConsultarRFecha.setGeometry(QtCore.QRect(320, 450, 240, 50))
        self.bConsultarRFecha.setObjectName(_fromUtf8("bConsultarRFecha"))
        self.tableViewRF = QtGui.QTableView(Form)
        self.tableViewRF.setGeometry(QtCore.QRect(30, 220, 570, 200))
        self.tableViewRF.setObjectName(_fromUtf8("tableViewRF"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("RecorridoFecha", "Recorrido Fecha", None))
        self.TitleRFecha.setText(_translate("RecorridoFecha", "RECORRIDOS POR FECHA", None))
        self.lFechaI.setText(_translate("RecorridoFecha", "FECHA INICIAL", None))
        self.lFechaF.setText(_translate("RecorridoFecha", "FECHA FINAL", None))
