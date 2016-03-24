# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../UI/fenetreGestion.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fenetreGestion(object):
    def setupUi(self, fenetreGestion):
        fenetreGestion.setObjectName("fenetreGestion")
        fenetreGestion.setEnabled(True)
        fenetreGestion.resize(1119, 873)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(fenetreGestion.sizePolicy().hasHeightForWidth())
        fenetreGestion.setSizePolicy(sizePolicy)
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
        self.corps_gestion.setEnabled(True)
        self.corps_gestion.setObjectName("corps_gestion")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.corps_gestion)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Passwords = QtWidgets.QVBoxLayout()
        self.Passwords.setObjectName("Passwords")
        self.titre_pwd = QtWidgets.QLabel(self.corps_gestion)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.titre_pwd.setFont(font)
        self.titre_pwd.setAlignment(QtCore.Qt.AlignCenter)
        self.titre_pwd.setIndent(0)
        self.titre_pwd.setObjectName("titre_pwd")
        self.Passwords.addWidget(self.titre_pwd)
        self.scrollArea_pwd = QtWidgets.QScrollArea(self.corps_gestion)
        self.scrollArea_pwd.setMaximumSize(QtCore.QSize(16777215, 767))
        self.scrollArea_pwd.setWidgetResizable(True)
        self.scrollArea_pwd.setObjectName("scrollArea_pwd")
        self.scrollAreaWidgetContents_pwd = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_pwd.setGeometry(QtCore.QRect(0, 0, 178, 765))
        self.scrollAreaWidgetContents_pwd.setObjectName("scrollAreaWidgetContents_pwd")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_pwd)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea_pwd.setWidget(self.scrollAreaWidgetContents_pwd)
        self.Passwords.addWidget(self.scrollArea_pwd)
        self.ajouter_pwd = QtWidgets.QLineEdit(self.corps_gestion)
        self.ajouter_pwd.setMinimumSize(QtCore.QSize(0, 30))
        self.ajouter_pwd.setText("")
        self.ajouter_pwd.setAlignment(QtCore.Qt.AlignCenter)
        self.ajouter_pwd.setObjectName("ajouter_pwd")
        self.Passwords.addWidget(self.ajouter_pwd)
        self.Passwords.setStretch(1, 4)
        self.Passwords.setStretch(2, 1)
        self.horizontalLayout.addLayout(self.Passwords)
        self.Sites = QtWidgets.QScrollArea(self.corps_gestion)
        self.Sites.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Sites.sizePolicy().hasHeightForWidth())
        self.Sites.setSizePolicy(sizePolicy)
        self.Sites.setStyleSheet("QWidget {\n"
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
        self.Sites.setWidgetResizable(True)
        self.Sites.setObjectName("Sites")
        self.scrollAreaWidgetContents_sites = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_sites.setGeometry(QtCore.QRect(0, 0, 726, 834))
        self.scrollAreaWidgetContents_sites.setObjectName("scrollAreaWidgetContents_sites")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_sites)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Sites.setWidget(self.scrollAreaWidgetContents_sites)
        self.horizontalLayout.addWidget(self.Sites)
        self.Categories = QtWidgets.QVBoxLayout()
        self.Categories.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.Categories.setObjectName("Categories")
        self.titre_cat = QtWidgets.QLabel(self.corps_gestion)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.titre_cat.setFont(font)
        self.titre_cat.setAlignment(QtCore.Qt.AlignCenter)
        self.titre_cat.setIndent(0)
        self.titre_cat.setObjectName("titre_cat")
        self.Categories.addWidget(self.titre_cat)
        self.scrollArea_cat = QtWidgets.QScrollArea(self.corps_gestion)
        self.scrollArea_cat.setWidgetResizable(True)
        self.scrollArea_cat.setObjectName("scrollArea_cat")
        self.scrollAreaWidgetContents_cat = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_cat.setGeometry(QtCore.QRect(0, 0, 177, 767))
        self.scrollAreaWidgetContents_cat.setObjectName("scrollAreaWidgetContents_cat")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_cat)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea_cat.setWidget(self.scrollAreaWidgetContents_cat)
        self.Categories.addWidget(self.scrollArea_cat)
        self.ajouter_cat = QtWidgets.QLineEdit(self.corps_gestion)
        self.ajouter_cat.setMinimumSize(QtCore.QSize(0, 30))
        self.ajouter_cat.setText("")
        self.ajouter_cat.setAlignment(QtCore.Qt.AlignCenter)
        self.ajouter_cat.setObjectName("ajouter_cat")
        self.Categories.addWidget(self.ajouter_cat)
        self.Categories.setStretch(1, 4)
        self.Categories.setStretch(2, 1)
        self.horizontalLayout.addLayout(self.Categories)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout.setStretch(2, 1)
        fenetreGestion.setCentralWidget(self.corps_gestion)
        self.menubar = QtWidgets.QMenuBar(fenetreGestion)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1119, 21))
        self.menubar.setObjectName("menubar")
        self.menuAide = QtWidgets.QMenu(self.menubar)
        self.menuAide.setObjectName("menuAide")
        fenetreGestion.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuAide.menuAction())

        self.retranslateUi(fenetreGestion)
        QtCore.QMetaObject.connectSlotsByName(fenetreGestion)
        fenetreGestion.setTabOrder(self.scrollArea_cat, self.ajouter_cat)
        fenetreGestion.setTabOrder(self.ajouter_cat, self.Sites)
        fenetreGestion.setTabOrder(self.Sites, self.scrollArea_pwd)
        fenetreGestion.setTabOrder(self.scrollArea_pwd, self.ajouter_pwd)

    def retranslateUi(self, fenetreGestion):
        _translate = QtCore.QCoreApplication.translate
        fenetreGestion.setWindowTitle(_translate("fenetreGestion", "Fenêtre de Gestion - MindPass"))
        self.titre_pwd.setText(_translate("fenetreGestion", "Mots de Passe"))
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

