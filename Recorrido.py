# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Recorrido.ui'
#
# Created: Mon Jun 24 13:29:47 2013
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

class Ui_hola(object):
    def setupUi(self, hola):
        hola.setObjectName(_fromUtf8("hola"))
        hola.resize(640, 515)
        self.dateEdit = QtGui.QDateEdit(hola)
        self.dateEdit.setGeometry(QtCore.QRect(110, 80, 110, 27))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.timeEdit = QtGui.QTimeEdit(hola)
        self.timeEdit.setGeometry(QtCore.QRect(140, 410, 151, 27))
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))
        self.timeEdit_2 = QtGui.QTimeEdit(hola)
        self.timeEdit_2.setGeometry(QtCore.QRect(350, 410, 161, 27))
        self.timeEdit_2.setObjectName(_fromUtf8("timeEdit_2"))
        self.label = QtGui.QLabel(hola)
        self.label.setGeometry(QtCore.QRect(50, 80, 66, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(hola)
        self.label_2.setGeometry(QtCore.QRect(140, 380, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(hola)
        self.label_3.setGeometry(QtCore.QRect(350, 380, 181, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(hola)
        self.label_4.setGeometry(QtCore.QRect(70, 150, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(hola)
        self.label_5.setGeometry(QtCore.QRect(110, 190, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit = QtGui.QLineEdit(hola)
        self.lineEdit.setGeometry(QtCore.QRect(230, 150, 301, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(hola)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 190, 301, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(hola)
        self.lineEdit_3.setGeometry(QtCore.QRect(350, 230, 81, 27))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_6 = QtGui.QLabel(hola)
        self.label_6.setGeometry(QtCore.QRect(230, 230, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.comboBox = QtGui.QComboBox(hola)
        self.comboBox.setGeometry(QtCore.QRect(290, 270, 251, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.label_7 = QtGui.QLabel(hola)
        self.label_7.setGeometry(QtCore.QRect(110, 270, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(hola)
        self.label_8.setGeometry(QtCore.QRect(90, 320, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.comboBox_2 = QtGui.QComboBox(hola)
        self.comboBox_2.setGeometry(QtCore.QRect(290, 320, 251, 27))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.label_9 = QtGui.QLabel(hola)
        self.label_9.setGeometry(QtCore.QRect(235, 20, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))

        self.retranslateUi(hola)
        QtCore.QMetaObject.connectSlotsByName(hola)

    def retranslateUi(self, hola):
        hola.setWindowTitle(_translate("hola", "Form", None))
        self.label.setText(_translate("hola", "FECHA", None))
        self.label_2.setText(_translate("hola", "HORA DE SALIDA", None))
        self.label_3.setText(_translate("hola", "HORA DE LLEGADA", None))
        self.label_4.setText(_translate("hola", "ID CONDUCTOR", None))
        self.label_5.setText(_translate("hola", "ID UNIDAD", None))
        self.label_6.setText(_translate("hola", "PASAJEROS", None))
        self.comboBox.setItemText(0, _translate("hola", "PISCINA OLIMPICA", None))
        self.comboBox.setItemText(1, _translate("hola", "ESPOL", None))
        self.comboBox.setItemText(2, _translate("hola", "ACACIAS", None))
        self.comboBox.setItemText(3, _translate("hola", "TERMINAL", None))
        self.comboBox.setItemText(4, _translate("hola", "ORQUIDEAS", None))
        self.comboBox.setItemText(5, _translate("hola", "DURAN", None))
        self.label_7.setText(_translate("hola", "ESTACION SALIDA", None))
        self.label_8.setText(_translate("hola", "ESTACION LLEGADA", None))
        self.comboBox_2.setItemText(0, _translate("hola", "PISCINA OLIMPICA", None))
        self.comboBox_2.setItemText(1, _translate("hola", "ESPOL", None))
        self.comboBox_2.setItemText(2, _translate("hola", "ACACIAS", None))
        self.comboBox_2.setItemText(3, _translate("hola", "TERMINAL", None))
        self.comboBox_2.setItemText(4, _translate("hola", "ORQUIDEAS", None))
        self.comboBox_2.setItemText(5, _translate("hola", "DURAN", None))
        self.label_9.setText(_translate("hola", "RECORRIDO", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    hola = QtGui.QWidget()
    ui = Ui_hola()
    ui.setupUi(hola)
    hola.show()
    sys.exit(app.exec_())

