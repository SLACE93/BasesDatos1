# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RecorridoFecha.ui'
#
# Created: Mon Jun 24 13:29:28 2013
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
        Form.resize(640, 516)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 50, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(160, 150, 131, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(170, 210, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.dateEdit = QtGui.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(300, 150, 181, 27))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.dateEdit_3 = QtGui.QDateEdit(Form)
        self.dateEdit_3.setGeometry(QtCore.QRect(300, 210, 181, 27))
        self.dateEdit_3.setObjectName(_fromUtf8("dateEdit_3"))
        self.buscarRH = QtGui.QPushButton(Form)
        self.buscarRH.setGeometry(QtCore.QRect(130, 260, 401, 27))
        self.buscarRH.setObjectName(_fromUtf8("buscarRH"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "RECORRIDOS POR FECHA", None))
        self.label_2.setText(_translate("Form", "FECHA INICIAL", None))
        self.label_3.setText(_translate("Form", "FECHA FINAL", None))
        self.buscarRH.setText(_translate("Form", "CONSULTAR", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

