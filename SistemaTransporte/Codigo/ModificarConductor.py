from PyQt4 import QtCore, QtGui
from comboBox import ExtendedComboBox

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

class Ui_ModificarConductor(object):
    def setupUi(self, ModificarConductor):
        ModificarConductor.setObjectName(_fromUtf8("ModificarConductor"))
        ModificarConductor.resize(640, 520)
        ModificarConductor.setStyleSheet(("background-image: url(imagenes/principal.jpg)"))
        self.TitleModificarConductor = QtGui.QLabel(ModificarConductor)
        self.TitleModificarConductor.setStyleSheet(("background-image: url()")) 
        self.TitleModificarConductor.setGeometry(QtCore.QRect(150, 50, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.TitleModificarConductor.setFont(font)
        self.TitleModificarConductor.setObjectName(_fromUtf8("TitleModificarConductor"))
        self.lIDConductor = QtGui.QLabel(ModificarConductor)
        self.lIDConductor.setStyleSheet(("background-image: url()")) 
        self.lIDConductor.setGeometry(QtCore.QRect(240, 110, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lIDConductor.setFont(font)
        self.lIDConductor.setObjectName(_fromUtf8("lIDConductor"))
        self.bModificarConductor = QtGui.QPushButton(ModificarConductor)
        self.bModificarConductor.setGeometry(QtCore.QRect(330, 440, 240, 50))
        self.bModificarConductor.setObjectName(_fromUtf8("bModificarConductor"))
        self.bRegresarConductor = QtGui.QPushButton(ModificarConductor)
        self.bRegresarConductor.setGeometry(QtCore.QRect(50, 440, 240, 50))
        self.bRegresarConductor.setObjectName(_fromUtf8("bRegresarConductor"))
        self.tableViewMC = QtGui.QTableView(ModificarConductor)
        self.tableViewMC.setStyleSheet(("background-image: url()")) 
        self.tableViewMC.setGeometry(QtCore.QRect(30, 221, 570, 200))
        self.tableViewMC.setObjectName(_fromUtf8("tableViewMC"))
        
        self.cboxIDConductor = ExtendedComboBox(ModificarConductor)
        self.cboxIDConductor.setGeometry(QtCore.QRect(150, 150, 321, 27))
        self.cboxIDConductor.setObjectName(_fromUtf8("cboxIDConductor"))

        self.retranslateUi(ModificarConductor)
        QtCore.QMetaObject.connectSlotsByName(ModificarConductor)

    def retranslateUi(self, ModificarConductor):
        ModificarConductor.setWindowTitle(_translate("ModificarConductor", "Form", None))
        self.TitleModificarConductor.setText(_translate("ModificarConductor", "MODIFICAR CONDUCTOR", None))
        self.lIDConductor.setText(_translate("ModificarConductor", "ID CONDUCTOR", None))
        self.bModificarConductor.setText(_translate("ModificarConductor", "MODIFICAR", None))
        self.bRegresarConductor.setText(_translate("ModificarConductor", "REGRESAR", None))



