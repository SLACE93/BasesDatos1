# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Unidades.ui'
#
# Created: Mon Jun 24 13:40:51 2013
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
        Form.resize(639, 517)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(240, 70, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(140, 160, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(140, 210, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(80, 260, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(260, 160, 261, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 210, 261, 31))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(260, 260, 261, 31))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.bingresarUnidades = QtGui.QPushButton(Form)
        self.bingresarUnidades.setGeometry(QtCore.QRect(310, 350, 241, 31))
        self.bingresarUnidades.setObjectName(_fromUtf8("bingresarUnidades"))
        self.bRegresarUnidades = QtGui.QPushButton(Form)
        self.bRegresarUnidades.setGeometry(QtCore.QRect(60, 350, 241, 31))
        self.bRegresarUnidades.setObjectName(_fromUtf8("bRegresarUnidades"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "UNIDADES", None))
        self.label_2.setText(_translate("Form", "MATRICULA", None))
        self.label_3.setText(_translate("Form", "CAPACIDAD", None))
        self.label_4.setText(_translate("Form", "AÑO FABRICACION", None))
        self.bingresarUnidades.setText(_translate("Form", "INGRESAR", None))
        self.bRegresarUnidades.setText(_translate("Form", "REGRESAR", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

