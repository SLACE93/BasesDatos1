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

class Ui_Conductor(object):
    def setupUi(self, Conductor):
        Conductor.setObjectName(_fromUtf8("Conductor"))
        Conductor.resize(640, 520)
        self.lEstSalida = QtGui.QLabel(Conductor)
        self.lEstSalida.setGeometry(QtCore.QRect(380, 310, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lEstSalida.setFont(font)
        self.lEstSalida.setObjectName(_fromUtf8("lEstSalida"))
        self.lIDConductor = QtGui.QLabel(Conductor)
        self.lIDConductor.setGeometry(QtCore.QRect(140, 130, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lIDConductor.setFont(font)
        self.lIDConductor.setObjectName(_fromUtf8("lIDConductor"))
        self.lNLicencia = QtGui.QLabel(Conductor)
        self.lNLicencia.setGeometry(QtCore.QRect(130, 230, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lNLicencia.setFont(font)
        self.lNLicencia.setObjectName(_fromUtf8("lNLicencia"))
        self.lNombre = QtGui.QLabel(Conductor)
        self.lNombre.setGeometry(QtCore.QRect(160, 180, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lNombre.setFont(font)
        self.lNombre.setObjectName(_fromUtf8("lNombre"))
        self.lineENLicencia = QtGui.QLineEdit(Conductor)
        self.lineENLicencia.setGeometry(QtCore.QRect(280, 230, 281, 31))
        self.lineENLicencia.setObjectName(_fromUtf8("lineENLicencia"))
        self.titleConductores = QtGui.QLabel(Conductor)
        self.titleConductores.setGeometry(QtCore.QRect(220, 40, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.titleConductores.setFont(font)
        self.titleConductores.setObjectName(_fromUtf8("titleConductores"))
        self.lineENombre = QtGui.QLineEdit(Conductor)
        self.lineENombre.setGeometry(QtCore.QRect(280, 180, 281, 31))
        font = QtGui.QFont()
        font.setItalic(False)
        self.lineENombre.setFont(font)
        self.lineENombre.setObjectName(_fromUtf8("lineENombre"))
        self.lineEIDCedula = QtGui.QLineEdit(Conductor)
        self.lineEIDCedula.setGeometry(QtCore.QRect(280, 130, 281, 31))
        self.lineEIDCedula.setObjectName(_fromUtf8("lineEIDCedula"))
        self.dEditFNac = QtGui.QDateEdit(Conductor)
        self.dEditFNac.setGeometry(QtCore.QRect(410, 340, 151, 27))
        self.dEditFNac.setObjectName(_fromUtf8("dEditFNac"))
        self.bRegresarConductores = QtGui.QPushButton(Conductor)
        self.bRegresarConductores.setGeometry(QtCore.QRect(50, 420, 240, 50))
        self.bRegresarConductores.setObjectName(_fromUtf8("bRegresarConductores"))
        self.bingresarConductores = QtGui.QPushButton(Conductor)
        self.bingresarConductores.setGeometry(QtCore.QRect(340, 420, 240, 50))
        self.bingresarConductores.setObjectName(_fromUtf8("bingresarConductores"))

        self.retranslateUi(Conductor)
        QtCore.QMetaObject.connectSlotsByName(Conductor)

    def retranslateUi(self, Conductor):
        Conductor.setWindowTitle(_translate("Conductor", "Form", None))
        self.lEstSalida.setText(_translate("Conductor", "FECHA NACIMIENTO", None))
        self.lIDConductor.setText(_translate("Conductor", "ID CEDULA", None))
        self.lNLicencia.setText(_translate("Conductor", "N.LICENCIA", None))
        self.lNombre.setText(_translate("Conductor", "NOMBRE", None))
        self.titleConductores.setText(_translate("Conductor", "CONDUCTORES", None))
        self.bRegresarConductores.setText(_translate("Conductor", "REGRESAR", None))
        self.bingresarConductores.setText(_translate("Conductor", "INGRESAR", None))