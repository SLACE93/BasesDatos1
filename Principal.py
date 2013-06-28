# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Principal.ui'
#
# Created: Mon Jun 24 13:40:20 2013
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(641, 517)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("background-color:rgb(219, 219, 255)"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.bconsultas = QtGui.QPushButton(self.centralwidget)
        self.bconsultas.setGeometry(QtCore.QRect(50, 350, 501, 51))
        self.bconsultas.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../Descargas/IMAGENES/consultas.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bconsultas.setIcon(icon)
        self.bconsultas.setIconSize(QtCore.QSize(521, 100))
        self.bconsultas.setObjectName(_fromUtf8("bconsultas"))
        self.bconductores = QtGui.QPushButton(self.centralwidget)
        self.bconductores.setGeometry(QtCore.QRect(310, 160, 241, 71))
        self.bconductores.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../../Descargas/IMAGENES/conductor.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bconductores.setIcon(icon1)
        self.bconductores.setIconSize(QtCore.QSize(301, 100))
        self.bconductores.setObjectName(_fromUtf8("bconductores"))
        self.brecorridos = QtGui.QPushButton(self.centralwidget)
        self.brecorridos.setGeometry(QtCore.QRect(60, 160, 201, 161))
        self.brecorridos.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../../Descargas/IMAGENES/recorrido.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.brecorridos.setIcon(icon2)
        self.brecorridos.setIconSize(QtCore.QSize(300, 161))
        self.brecorridos.setObjectName(_fromUtf8("brecorridos"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 581, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Serif"))
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("background-font: rgb(255, 255, 255);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.bunidades = QtGui.QPushButton(self.centralwidget)
        self.bunidades.setGeometry(QtCore.QRect(310, 250, 241, 71))
        self.bunidades.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("../../Descargas/IMAGENES/unidades.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bunidades.setIcon(icon3)
        self.bunidades.setIconSize(QtCore.QSize(301, 100))
        self.bunidades.setObjectName(_fromUtf8("bunidades"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "SISTEMA DE CONTROL TRANSESPOL", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

