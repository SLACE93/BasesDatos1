# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unidades.ui'
#
# Created: Tue Jul  9 17:54:07 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

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

class Ui_Unidades(object):
    def setupUi(self, Unidades):
        Unidades.setObjectName(_fromUtf8("Unidades"))
        Unidades.resize(640, 520)
        self.lineEAnoFabricacion = QtGui.QLineEdit(Unidades)
        self.lineEAnoFabricacion.setGeometry(QtCore.QRect(280, 210, 261, 31))
        self.lineEAnoFabricacion.setObjectName(_fromUtf8("lineEAnoFabricacion"))
        self.lMatricula = QtGui.QLabel(Unidades)
        self.lMatricula.setGeometry(QtCore.QRect(150, 110, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lMatricula.setFont(font)
        self.lMatricula.setObjectName(_fromUtf8("lMatricula"))
        self.lAoFabricacion = QtGui.QLabel(Unidades)
        self.lAoFabricacion.setGeometry(QtCore.QRect(90, 210, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lAoFabricacion.setFont(font)
        self.lAoFabricacion.setObjectName(_fromUtf8("lAoFabricacion"))
        self.lineEMatricula = QtGui.QLineEdit(Unidades)
        self.lineEMatricula.setGeometry(QtCore.QRect(280, 110, 261, 31))
        self.lineEMatricula.setObjectName(_fromUtf8("lineEMatricula"))
        self.bRegresarUnidades = QtGui.QPushButton(Unidades)
        self.bRegresarUnidades.setGeometry(QtCore.QRect(80, 300, 241, 31))
        self.bRegresarUnidades.setObjectName(_fromUtf8("bRegresarUnidades"))
        self.lCapacidad = QtGui.QLabel(Unidades)
        self.lCapacidad.setGeometry(QtCore.QRect(150, 160, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lCapacidad.setFont(font)
        self.lCapacidad.setObjectName(_fromUtf8("lCapacidad"))
        self.bingresarUnidades = QtGui.QPushButton(Unidades)
        self.bingresarUnidades.setGeometry(QtCore.QRect(330, 300, 241, 31))
        self.bingresarUnidades.setObjectName(_fromUtf8("bingresarUnidades"))
        self.titleUnidades = QtGui.QLabel(Unidades)
        self.titleUnidades.setGeometry(QtCore.QRect(260, 20, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.titleUnidades.setFont(font)
        self.titleUnidades.setObjectName(_fromUtf8("titleUnidades"))
        self.lineECapacidad = QtGui.QLineEdit(Unidades)
        self.lineECapacidad.setGeometry(QtCore.QRect(280, 160, 261, 31))
        self.lineECapacidad.setObjectName(_fromUtf8("lineECapacidad"))

        self.retranslateUi(Unidades)
        QtCore.QMetaObject.connectSlotsByName(Unidades)

    def retranslateUi(self, Unidades):
        Unidades.setWindowTitle(_translate("Unidades", "Form", None))
        self.lMatricula.setText(_translate("Unidades", "MATRICULA", None))
        self.lAoFabricacion.setText(_translate("Unidades", "AÑO FABRICACION", None))
        self.bRegresarUnidades.setText(_translate("Unidades", "REGRESAR", None))
        self.lCapacidad.setText(_translate("Unidades", "CAPACIDAD", None))
        self.bingresarUnidades.setText(_translate("Unidades", "INGRESAR", None))
        self.titleUnidades.setText(_translate("Unidades", "UNIDADES", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Unidades = QtGui.QWidget()
    ui = Ui_Unidades()
    ui.setupUi(Unidades)
    Unidades.show()
    sys.exit(app.exec_())

