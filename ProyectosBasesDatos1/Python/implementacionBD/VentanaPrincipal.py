'''
Created on 09/07/2013

@author: josanvel
'''

from PyQt4 import QtCore, QtGui
from Recorridos import Ui_Recorridos
from Conductor import Ui_Conductor
from Unidades import Ui_Unidades
from Consultas import Ui_Consultas

import sys
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

class Ui_Principal(QtGui.QMainWindow):
    def setupUi(self, Principal):
        Principal.setObjectName(_fromUtf8("Principal"))
        Principal.resize(640, 520)
        self.centralWidget = QtGui.QWidget(Principal)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.brecorridos = QtGui.QPushButton(self.centralWidget)
        self.brecorridos.setGeometry(QtCore.QRect(70, 140, 220, 170))
        self.brecorridos.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../Descargas/IMAGENES/recorrido.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.brecorridos.setIcon(icon)
        self.brecorridos.setIconSize(QtCore.QSize(300, 161))
        self.brecorridos.setObjectName(_fromUtf8("brecorridos"))
        self.bconductores = QtGui.QPushButton(self.centralWidget)
        self.bconductores.setGeometry(QtCore.QRect(320, 140, 240, 70))
        self.bconductores.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../../Descargas/IMAGENES/conductor.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bconductores.setIcon(icon1)
        self.bconductores.setIconSize(QtCore.QSize(301, 100))
        self.bconductores.setObjectName(_fromUtf8("bconductores"))
        self.bconsultas = QtGui.QPushButton(self.centralWidget)
        self.bconsultas.setGeometry(QtCore.QRect(70, 340, 490, 50))
        self.bconsultas.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../../Descargas/IMAGENES/consultas.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bconsultas.setIcon(icon2)
        self.bconsultas.setIconSize(QtCore.QSize(521, 100))
        self.bconsultas.setObjectName(_fromUtf8("bconsultas"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 581, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Serif"))
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("background-font: rgb(255, 255, 255);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.bunidades = QtGui.QPushButton(self.centralWidget)
        self.bunidades.setGeometry(QtCore.QRect(320, 240, 240, 70))
        self.bunidades.setText(_fromUtf8(""))
        self.bunidades.setIcon(icon1)
        self.bunidades.setIconSize(QtCore.QSize(301, 100))
        self.bunidades.setObjectName(_fromUtf8("bunidades"))
        Principal.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(Principal)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 640, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        Principal.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(Principal)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        Principal.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(Principal)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        Principal.setStatusBar(self.statusBar)

        self.retranslateUi(Principal)
        QtCore.QMetaObject.connectSlotsByName(Principal)
        self.connect(self.brecorridos, QtCore.SIGNAL("clicked()"), self.abrirRecorrido)
        self.connect(self.bconductores, QtCore.SIGNAL("clicked()"), self.abrirConductor)
        self.connect(self.bunidades, QtCore.SIGNAL("clicked()"), self.abrirUnidades)
        self.connect(self.bconsultas, QtCore.SIGNAL("clicked()"), self.abrirConsultas)
        
    def retranslateUi(self, Principal):
        Principal.setWindowTitle(_translate("Principal", "Principal", None))
        self.label.setText(_translate("Principal", "SISTEMA DE CONTROL TRANSESPOL", None))
            
    def abrirRecorrido(self):
        Recorridos = QtGui.QWidget()
        uiR =  Ui_Recorridos()
        uiR.setupUi(Recorridos)
        Recorridos.show()
        uiR.exec_()
        
    def abrirConductor(self):
        self.close()
        Conductor = QtGui.QWidget()
        uiC =  Ui_Conductor()
        uiC.setupUi(Conductor)
        Conductor.show()
        uiC.exec_()

    def abrirUnidades(self):
        self.close()
        Unidades = QtGui.QWidget()
        uiU =  Ui_Unidades()
        uiU.setupUi(Unidades)
        Unidades.show()
        uiU.exec_()
        
    def abrirConsultas(self):
        self.close()
        Consultas = QtGui.QWidget()
        uiC =  Ui_Consultas()
        uiC.setupUi(Consultas)
        Consultas.show()
        uiC.exec_()
        
        
        
        
