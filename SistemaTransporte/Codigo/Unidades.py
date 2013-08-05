# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unidades.ui'
#
# Created: Tue Jul 9 17:54:07 2013
# by: PyQt4 UI code generator 4.10
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
        Unidades.setStyleSheet(("background-image: url(imagenes/principal.jpg)"))
        self.label = QtGui.QLabel(Unidades)
        self.label.setStyleSheet("background-image: url()")
        self.label.setGeometry(QtCore.QRect(240, 70, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.lMatricula = QtGui.QLabel(Unidades)
        self.lMatricula.setStyleSheet("background-image: url()")
        self.lMatricula.setGeometry(QtCore.QRect(140, 160, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lMatricula.setFont(font)
        self.lMatricula.setObjectName(_fromUtf8("lMatricula"))
        Unidades.setStyleSheet(("background-image: url(imagenes/principal.jpg)"))
        self.lCapacidad = QtGui.QLabel(Unidades)
        self.lCapacidad.setGeometry(QtCore.QRect(140, 230, 111, 20))
        self.lCapacidad.setStyleSheet("background-image: url()")
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lCapacidad.setFont(font)
        self.lCapacidad.setObjectName(_fromUtf8("lCapacidad"))
        self.lAnoFabricacion = QtGui.QLabel(Unidades)
        self.lAnoFabricacion.setStyleSheet("background-image: url()")
        self.lAnoFabricacion.setGeometry(QtCore.QRect(70, 300, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lAnoFabricacion.setFont(font)
        self.lAnoFabricacion.setObjectName(_fromUtf8("lAnoFabricacion"))
        self.lineEMatricula = QtGui.QLineEdit(Unidades)
        self.lineEMatricula.setGeometry(QtCore.QRect(260, 160, 261, 31))
        self.lineEMatricula.setObjectName(_fromUtf8("lineEMatricula"))
        self.lineECapacidad = QtGui.QLineEdit(Unidades)
        self.lineECapacidad.setGeometry(QtCore.QRect(260, 230, 261, 31))
        self.lineECapacidad.setObjectName(_fromUtf8("lineECapacidad"))
        self.lineEAnoFab = QtGui.QLineEdit(Unidades)
        self.lineEAnoFab.setGeometry(QtCore.QRect(260, 300, 261, 31))
        self.lineEAnoFab.setObjectName(_fromUtf8("lineEAnoFab"))
        self.bingresarUnidades = QtGui.QPushButton(Unidades)
        self.bingresarUnidades.setGeometry(QtCore.QRect(340, 400, 240, 50))
        self.bingresarUnidades.setObjectName(_fromUtf8("bingresarUnidades"))
        self.bRegresarUnidades = QtGui.QPushButton(Unidades)
        self.bRegresarUnidades.setGeometry(QtCore.QRect(50, 400, 240, 50))
        self.bRegresarUnidades.setObjectName(_fromUtf8("bRegresarUnidades"))

        self.retranslateUi(Unidades)
        QtCore.QMetaObject.connectSlotsByName(Unidades)

    def retranslateUi(self, Unidades):
        Unidades.setWindowTitle(_translate("Unidades", "Unidades", None))
        self.label.setText(_translate("Unidades", "UNIDADES", None))
        self.lMatricula.setText(_translate("Unidades", "MATRICULA", None))
        self.lCapacidad.setText(_translate("Unidades", "CAPACIDAD", None))
        self.lAnoFabricacion.setText(_translate("Unidades", "AÑO FABRICACION", None))
