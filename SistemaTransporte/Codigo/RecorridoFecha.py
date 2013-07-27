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
    def setupUi(self, RecorridoFecha):
        RecorridoFecha.setObjectName(_fromUtf8("RecorridoFecha"))
        RecorridoFecha.resize(640, 516)
        self.RecorridosFecha = QtGui.QLabel(RecorridoFecha)
        self.RecorridosFecha.setGeometry(QtCore.QRect(160, 50, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.RecorridosFecha.setFont(font)
        self.RecorridosFecha.setObjectName(_fromUtf8("RecorridosFecha"))
        self.lFechaI = QtGui.QLabel(RecorridoFecha)
        self.lFechaI.setGeometry(QtCore.QRect(160, 120, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lFechaI.setFont(font)
        self.lFechaI.setObjectName(_fromUtf8("lFechaI"))
        self.lFechaF = QtGui.QLabel(RecorridoFecha)
        self.lFechaF.setGeometry(QtCore.QRect(170, 160, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lFechaF.setFont(font)
        self.lFechaF.setObjectName(_fromUtf8("lFechaF"))
        self.dateEFechaI = QtGui.QDateEdit(RecorridoFecha)
        self.dateEFechaI.setGeometry(QtCore.QRect(310, 120, 181, 27))
        self.dateEFechaI.setObjectName(_fromUtf8("dateEFechaI"))
        self.dateEFechaF = QtGui.QDateEdit(RecorridoFecha)
        self.dateEFechaF.setGeometry(QtCore.QRect(310, 160, 181, 27))
        self.dateEFechaF.setObjectName(_fromUtf8("dateEFechaF"))
        self.bConsultarRFecha = QtGui.QPushButton(RecorridoFecha)
        self.bConsultarRFecha.setGeometry(QtCore.QRect(350, 440, 240, 50))
        self.bConsultarRFecha.setObjectName(_fromUtf8("bConsultarRFecha"))
        self.bRegresarRFecha = QtGui.QPushButton(RecorridoFecha)
        self.bRegresarRFecha.setGeometry(QtCore.QRect(50, 440, 240, 50))
        self.bRegresarRFecha.setObjectName(_fromUtf8("bRegresarRFecha"))

        self.retranslateUi(RecorridoFecha)
        QtCore.QMetaObject.connectSlotsByName(RecorridoFecha)

    def retranslateUi(self, RecorridoFecha):
        RecorridoFecha.setWindowTitle(_translate("RecorridoFecha", "RecorridoFecha", None))
        self.RecorridosFecha.setText(_translate("RecorridoFecha", "RECORRIDOS POR FECHA", None))
        self.lFechaI.setText(_translate("RecorridoFecha", "FECHA INICIAL", None))
        self.lFechaF.setText(_translate("RecorridoFecha", "FECHA FINAL", None))
        self.bConsultarRFecha.setText(_translate("RecorridoFecha", "CONSULTAR", None))
        self.bRegresarRFecha.setText(_translate("RecorridoFecha", "REGRESAR", None))
