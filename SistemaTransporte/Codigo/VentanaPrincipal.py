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

class Ui_Principal(QtGui.QMainWindow):
    def setupUi(self, Principal):
        Principal.setObjectName(_fromUtf8("Principal"))
        Principal.resize(640, 520)
        Principal.setLayoutDirection(QtCore.Qt.LeftToRight)
        Principal.setAutoFillBackground(False)
        Principal.setStyleSheet(("background-image: url(imagenes/principal.jpg)"))
        self.centralwidget = QtGui.QWidget(Principal)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.bconsultas = QtGui.QPushButton(self.centralwidget)
        self.bconsultas.setGeometry(QtCore.QRect(60, 400, 500, 50))
        self.bconsultas.setText(_fromUtf8(""))
       
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagenes/bconsulta.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bconsultas.setIcon(icon)
        self.bconsultas.setIconSize(QtCore.QSize(521, 100))
        self.bconsultas.setObjectName(_fromUtf8("bconsultas"))
        
        self.bconductores = QtGui.QPushButton(self.centralwidget)
        self.bconductores.setGeometry(QtCore.QRect(320, 160, 240, 60))
        self.bconductores.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("imagenes/bconductor.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bconductores.setIcon(icon1)
        self.bconductores.setIconSize(QtCore.QSize(301, 100))
        self.bconductores.setObjectName(_fromUtf8("bconductores"))
        
        self.brecorridos = QtGui.QPushButton(self.centralwidget)
        self.brecorridos.setGeometry(QtCore.QRect(60, 160, 240, 140))
        self.brecorridos.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("imagenes/brecorrido.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.brecorridos.setIcon(icon2)
        self.brecorridos.setIconSize(QtCore.QSize(300, 161))
        self.brecorridos.setObjectName(_fromUtf8("brecorridos"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setStyleSheet("background-image: url()")
        self.label.setGeometry(QtCore.QRect(20, 95, 581, 31))
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
        self.bunidades.setGeometry(QtCore.QRect(320, 240, 240, 60))
        self.bunidades.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("imagenes/bunidad.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bunidades.setIcon(icon3)
        self.bunidades.setIconSize(QtCore.QSize(301, 100))
        self.bunidades.setObjectName(_fromUtf8("bunidades"))
        
        self.bmodificar = QtGui.QPushButton(self.centralwidget)
        self.bmodificar.setGeometry(QtCore.QRect(60, 320, 240, 60))
        self.bmodificar.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("imagenes/bunidad.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bmodificar.setIcon(icon4)
        self.bmodificar.setIconSize(QtCore.QSize(301, 100))
        self.bmodificar.setObjectName(_fromUtf8("bmodificar"))
        
        self.beliminar = QtGui.QPushButton(self.centralwidget)
        self.beliminar.setGeometry(QtCore.QRect(320, 320, 240, 60))
        self.beliminar.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("imagenes/bunidad.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.beliminar.setIcon(icon5)
        self.beliminar.setIconSize(QtCore.QSize(301, 100))
        self.beliminar.setObjectName(_fromUtf8("beliminar"))
        
        Principal.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Principal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Principal.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Principal)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Principal.setStatusBar(self.statusbar)

        self.retranslateUi(Principal)
        QtCore.QMetaObject.connectSlotsByName(Principal)

    def retranslateUi(self, Principal):
        Principal.setWindowTitle(_translate("Principal", "Principal", None))
        self.label.setText(_translate("Principal", "SISTEMA DE CONTROL TRANSESPOL", None))
        self.label.setStyleSheet("background-image: url()")
