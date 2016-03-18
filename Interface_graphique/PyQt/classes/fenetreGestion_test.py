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
        fenetreGestion.resize(1145, 857)
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
"    color: black;\n"
"    padding-left: 10px;\n"
"}\n"
"")
        self.corps_gestion = QtWidgets.QWidget(fenetreGestion)
        self.corps_gestion.setObjectName("corps_gestion")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.corps_gestion)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 1121, 811))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_gestion = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_gestion.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_gestion.setObjectName("horizontalLayout_gestion")
        self.scrollArea = QtWidgets.QScrollArea(self.horizontalLayoutWidget_3)
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
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 890, 809))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 881, 122))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.ligne = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.ligne.setObjectName("ligne")
        self.site_web = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.site_web.setAlignment(QtCore.Qt.AlignCenter)
        self.site_web.setObjectName("site_web")
        self.ligne.addWidget(self.site_web)
        self.identifiant = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.identifiant.setAlignment(QtCore.Qt.AlignCenter)
        self.identifiant.setObjectName("identifiant")
        self.ligne.addWidget(self.identifiant)
        self.mdp = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.mdp.setObjectName("mdp")
        self.ligne.addWidget(self.mdp)
        self.categorie = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.categorie.setText("")
        self.categorie.setObjectName("categorie")
        self.ligne.addWidget(self.categorie)
        self.ligne.setStretch(0, 100)
        self.ligne.setStretch(1, 120)
        self.ligne.setStretch(2, 120)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_gestion.addWidget(self.scrollArea)
        self.Categories = QtWidgets.QVBoxLayout()
        self.Categories.setObjectName("Categories")
        self.titre_cat = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.titre_cat.setFont(font)
        self.titre_cat.setAlignment(QtCore.Qt.AlignCenter)
        self.titre_cat.setIndent(0)
        self.titre_cat.setObjectName("titre_cat")
        self.Categories.addWidget(self.titre_cat)
        self.scrollArea_cat = QtWidgets.QScrollArea(self.horizontalLayoutWidget_3)
        self.scrollArea_cat.setWidgetResizable(True)
        self.scrollArea_cat.setObjectName("scrollArea_cat")
        self.scrollAreaWidgetContents_cat = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_cat.setGeometry(QtCore.QRect(0, 0, 219, 742))
        self.scrollAreaWidgetContents_cat.setObjectName("scrollAreaWidgetContents_cat")
        self.scrollArea_cat.setWidget(self.scrollAreaWidgetContents_cat)
        self.Categories.addWidget(self.scrollArea_cat)
        self.ajouter_cat = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.ajouter_cat.setMinimumSize(QtCore.QSize(0, 30))
        self.ajouter_cat.setText("")
        self.ajouter_cat.setAlignment(QtCore.Qt.AlignCenter)
        self.ajouter_cat.setObjectName("ajouter_cat")
        self.Categories.addWidget(self.ajouter_cat)
        self.Categories.setStretch(2, 2)
        self.horizontalLayout_gestion.addLayout(self.Categories)
        self.horizontalLayout_gestion.setStretch(0, 8)
        self.horizontalLayout_gestion.setStretch(1, 2)
        fenetreGestion.setCentralWidget(self.corps_gestion)
        self.menubar = QtWidgets.QMenuBar(fenetreGestion)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1145, 21))
        self.menubar.setObjectName("menubar")
        self.menuAide = QtWidgets.QMenu(self.menubar)
        self.menuAide.setObjectName("menuAide")
        fenetreGestion.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuAide.menuAction())

        self.retranslateUi(fenetreGestion)
        QtCore.QMetaObject.connectSlotsByName(fenetreGestion)

    def retranslateUi(self, fenetreGestion):
        _translate = QtCore.QCoreApplication.translate
        fenetreGestion.setWindowTitle(_translate("fenetreGestion", "Fenêtre de Gestion - MindPass"))
        self.site_web.setText(_translate("fenetreGestion", "Site 1"))
        self.identifiant.setText(_translate("fenetreGestion", "Identifiant"))
        self.titre_cat.setText(_translate("fenetreGestion", "Catégories"))
        self.menuAide.setTitle(_translate("fenetreGestion", "Aide"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fenetreGestion = QtWidgets.QMainWindow()
    ui = Ui_fenetreGestion()
    ui.setupUi(fenetreGestion)
    fenetreGestion.show()
    sys.exit(app.exec_())

