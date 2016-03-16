# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../UI/fenetreGestion_test.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fenetreGestion(object):
    def setupUi(self, fenetreGestion):
        fenetreGestion.setObjectName("fenetreGestion")
        fenetreGestion.resize(1200, 900)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ressources/MindPass-icone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        fenetreGestion.setWindowIcon(icon)
        fenetreGestion.setStyleSheet("QMainWindow {\n"
"    background: qradialgradient(spread:pad, cx:0, cy:1, radius:1.406, fx:0, fy:1, stop:0 rgba(244, 216, 148, 255), stop:1 rgba(255, 102, 102, 255));\n"
"}\n"
"\n"
"#catTitle {\n"
"    color: white;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background: rgba(255,255,255,100);\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    padding-left: 10px;\n"
"}\n"
"")
        self.corps_gestion = QtWidgets.QWidget(fenetreGestion)
        self.corps_gestion.setObjectName("corps_gestion")
        self.scrollArea = QtWidgets.QScrollArea(self.corps_gestion)
        self.scrollArea.setGeometry(QtCore.QRect(10, 70, 881, 750))
        self.scrollArea.setStyleSheet("QWidget {\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    background: rgba(255,255,255,50);\n"
"}\n"
"\n"
"QLabel {\n"
"    background-color: transparent;\n"
"    background: transparent;\n"
"}\n"
"")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 864, 750))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollAreaWidgetContents.setAutoFillBackground(False)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.line = QtWidgets.QFrame(self.corps_gestion)
        self.line.setGeometry(QtCore.QRect(930, 70, 3, 750))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.catTitle = QtWidgets.QLabel(self.corps_gestion)
        self.catTitle.setGeometry(QtCore.QRect(960, 50, 210, 60))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.catTitle.setFont(font)
        self.catTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.catTitle.setIndent(0)
        self.catTitle.setObjectName("catTitle")
        self.lineEdit = QtWidgets.QLineEdit(self.corps_gestion)
        self.lineEdit.setGeometry(QtCore.QRect(950, 130, 230, 45))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        fenetreGestion.setCentralWidget(self.corps_gestion)
        self.menubar = QtWidgets.QMenuBar(fenetreGestion)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        fenetreGestion.setMenuBar(self.menubar)

        self.retranslateUi(fenetreGestion)
        QtCore.QMetaObject.connectSlotsByName(fenetreGestion)

    def retranslateUi(self, fenetreGestion):
        _translate = QtCore.QCoreApplication.translate
        fenetreGestion.setWindowTitle(_translate("fenetreGestion", "Fenêtre de Gestion - MindPass"))
        self.catTitle.setText(_translate("fenetreGestion", "Catégories"))
        self.lineEdit.setText(_translate("fenetreGestion", "Ajouter une catégorie"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fenetreGestion = QtWidgets.QMainWindow()
    ui = Ui_fenetreGestion()
    ui.setupUi(fenetreGestion)
    fenetreGestion.show()
    sys.exit(app.exec_())

