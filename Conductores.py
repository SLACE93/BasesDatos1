# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Conductores.ui'
#
# Created: Mon Jun 24 13:40:29 2013
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(639, 516)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 110, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 170, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(140, 230, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(170, 200, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(110, 260, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(90, 290, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.dateEdit = QtGui.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(100, 110, 171, 27))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(20, 340, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(320, 340, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(290, 170, 281, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 200, 281, 21))
        font = QtGui.QFont()
        font.setItalic(False)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(290, 230, 281, 21))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(290, 260, 281, 21))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(290, 290, 281, 21))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.timeEdit = QtGui.QTimeEdit(Form)
        self.timeEdit.setGeometry(QtCore.QRect(160, 340, 118, 27))
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))
        self.timeEdit_2 = QtGui.QTimeEdit(Form)
        self.timeEdit_2.setGeometry(QtCore.QRect(480, 340, 118, 27))
        self.timeEdit_2.setObjectName(_fromUtf8("timeEdit_2"))
        self.bRegresarConductor = QtGui.QPushButton(Form)
        self.bRegresarConductor.setGeometry(QtCore.QRect(130, 410, 161, 31))
        self.bRegresarConductor.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../Descargas/IMAGENES/Regresar.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bRegresarConductor.setIcon(icon)
        self.bRegresarConductor.setIconSize(QtCore.QSize(500, 1000))
        self.bRegresarConductor.setObjectName(_fromUtf8("bRegresarConductor"))
        self.bingresarConductor = QtGui.QPushButton(Form)
        self.bingresarConductor.setGeometry(QtCore.QRect(350, 410, 161, 31))
        self.bingresarConductor.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../../Descargas/IMAGENES/Ingresar.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bingresarConductor.setIcon(icon1)
        self.bingresarConductor.setIconSize(QtCore.QSize(600, 360))
        self.bingresarConductor.setObjectName(_fromUtf8("bingresarConductor"))
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(250, 50, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "FECHA", None))
        self.label_2.setText(_translate("Form", "ID CONDUCTOR", None))
        self.label_3.setText(_translate("Form", "N° PASAJEROS", None))
        self.label_4.setText(_translate("Form", "N° UNIDAD", None))
        self.label_5.setText(_translate("Form", "ESTACION SALIDA", None))
        self.label_6.setText(_translate("Form", "ESTACION LLEGADA", None))
        self.label_7.setText(_translate("Form", "HORA SALIDA", None))
        self.label_8.setText(_translate("Form", "HORA LLEGADA", None))
        self.label_9.setText(_translate("Form", "CONDUCTOR", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
