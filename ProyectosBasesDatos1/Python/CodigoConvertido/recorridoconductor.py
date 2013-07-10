# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recorridoconductor.ui'
#
# Created: Tue Jul  9 17:55:28 2013
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

class Ui_RecorridoConductor(object):
    def setupUi(self, RecorridoConductor):
        RecorridoConductor.setObjectName(_fromUtf8("RecorridoConductor"))
        RecorridoConductor.resize(640, 520)
        self.lfechaFinalRC = QtGui.QLabel(RecorridoConductor)
        self.lfechaFinalRC.setGeometry(QtCore.QRect(180, 150, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lfechaFinalRC.setFont(font)
        self.lfechaFinalRC.setObjectName(_fromUtf8("lfechaFinalRC"))
        self.lineIDConductorRC = QtGui.QLineEdit(RecorridoConductor)
        self.lineIDConductorRC.setGeometry(QtCore.QRect(310, 190, 151, 27))
        self.lineIDConductorRC.setObjectName(_fromUtf8("lineIDConductorRC"))
        self.buscarRH = QtGui.QPushButton(RecorridoConductor)
        self.buscarRH.setGeometry(QtCore.QRect(110, 240, 401, 27))
        self.buscarRH.setObjectName(_fromUtf8("buscarRH"))
        self.lIDConductorRC = QtGui.QLabel(RecorridoConductor)
        self.lIDConductorRC.setGeometry(QtCore.QRect(160, 190, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lIDConductorRC.setFont(font)
        self.lIDConductorRC.setObjectName(_fromUtf8("lIDConductorRC"))
        self.fechaInicialRC = QtGui.QDateEdit(RecorridoConductor)
        self.fechaInicialRC.setGeometry(QtCore.QRect(310, 110, 151, 27))
        self.fechaInicialRC.setObjectName(_fromUtf8("fechaInicialRC"))
        self.lfechaInicialRC = QtGui.QLabel(RecorridoConductor)
        self.lfechaInicialRC.setGeometry(QtCore.QRect(160, 110, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lfechaInicialRC.setFont(font)
        self.lfechaInicialRC.setObjectName(_fromUtf8("lfechaInicialRC"))
        self.fechaInicialRC_2 = QtGui.QDateEdit(RecorridoConductor)
        self.fechaInicialRC_2.setGeometry(QtCore.QRect(310, 150, 151, 27))
        self.fechaInicialRC_2.setObjectName(_fromUtf8("fechaInicialRC_2"))
        self.TitleRecorridoConductor = QtGui.QLabel(RecorridoConductor)
        self.TitleRecorridoConductor.setGeometry(QtCore.QRect(110, 30, 411, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.TitleRecorridoConductor.setFont(font)
        self.TitleRecorridoConductor.setObjectName(_fromUtf8("TitleRecorridoConductor"))

        self.retranslateUi(RecorridoConductor)
        QtCore.QMetaObject.connectSlotsByName(RecorridoConductor)

    def retranslateUi(self, RecorridoConductor):
        RecorridoConductor.setWindowTitle(_translate("RecorridoConductor", "Form", None))
        self.lfechaFinalRC.setText(_translate("RecorridoConductor", "FECHA FINAL", None))
        self.buscarRH.setText(_translate("RecorridoConductor", "CONSULTAR", None))
        self.lIDConductorRC.setText(_translate("RecorridoConductor", "ID CONDUCTOR", None))
        self.lfechaInicialRC.setText(_translate("RecorridoConductor", " FECHA INICIAL", None))
        self.TitleRecorridoConductor.setText(_translate("RecorridoConductor", "RECORRIDOS POR CONDUCTOR", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    RecorridoConductor = QtGui.QWidget()
    ui = Ui_RecorridoConductor()
    ui.setupUi(RecorridoConductor)
    RecorridoConductor.show()
    sys.exit(app.exec_())

