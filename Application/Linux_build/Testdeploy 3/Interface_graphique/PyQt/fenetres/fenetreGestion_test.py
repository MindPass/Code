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
        self.splitter = QtWidgets.QSplitter(self.corps_gestion)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(0)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.Passwords = QtWidgets.QVBoxLayout(self.widget)
        self.Passwords.setObjectName("Passwords")
        self.titre_pwd = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.titre_pwd.setFont(font)
        self.titre_pwd.setAlignment(QtCore.Qt.AlignCenter)
        self.titre_pwd.setIndent(0)
        self.titre_pwd.setObjectName("titre_pwd")
        self.Passwords.addWidget(self.titre_pwd)
        self.scrollArea_pwd = QtWidgets.QScrollArea(self.widget)
        self.scrollArea_pwd.setMaximumSize(QtCore.QSize(16777215, 767))
        self.scrollArea_pwd.setWidgetResizable(True)
        self.scrollArea_pwd.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea_pwd.setObjectName("scrollArea_pwd")
        self.scrollAreaWidgetContents_pwd = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_pwd.setGeometry(QtCore.QRect(0, 0, 238, 765))
        self.scrollAreaWidgetContents_pwd.setObjectName("scrollAreaWidgetContents_pwd")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_pwd)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.ligne_pwd = QtWidgets.QHBoxLayout()
        self.ligne_pwd.setObjectName("ligne_pwd")
        self.label_pwd = QtWidgets.QLabel(self.scrollAreaWidgetContents_pwd)
        self.label_pwd.setMaximumSize(QtCore.QSize(16777215, 745))
        self.label_pwd.setObjectName("label_pwd")
        self.ligne_pwd.addWidget(self.label_pwd)
        self.pushButton_pwd = QtWidgets.QPushButton(self.scrollAreaWidgetContents_pwd)
        self.pushButton_pwd.setEnabled(True)
        self.pushButton_pwd.setObjectName("pushButton_pwd")
        self.ligne_pwd.addWidget(self.pushButton_pwd)
        self.verticalLayout_2.addLayout(self.ligne_pwd)

        self.scrollArea_pwd.setWidget(self.scrollAreaWidgetContents_pwd)
        self.Passwords.addWidget(self.scrollArea_pwd)
        self.ajouter_pwd = QtWidgets.QLineEdit(self.widget)
        self.ajouter_pwd.setMinimumSize(QtCore.QSize(0, 30))
        self.ajouter_pwd.setText("")
        self.ajouter_pwd.setAlignment(QtCore.Qt.AlignCenter)
        self.ajouter_pwd.setObjectName("ajouter_pwd")
        self.Passwords.addWidget(self.ajouter_pwd)
        self.Passwords.setStretch(1, 4)
        self.Passwords.setStretch(2, 1)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.Sites = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.Sites.setObjectName("Sites")
        self.scrollArea_sites = QtWidgets.QScrollArea(self.verticalLayoutWidget_2)
        self.scrollArea_sites.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_sites.sizePolicy().hasHeightForWidth())
        self.scrollArea_sites.setSizePolicy(sizePolicy)
        self.scrollArea_sites.setStyleSheet("QWidget {\n"
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
        self.scrollArea_sites.setWidgetResizable(True)
        self.scrollArea_sites.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea_sites.setObjectName("scrollArea_sites")
        self.scrollAreaWidgetContents_sites = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_sites.setGeometry(QtCore.QRect(0, 0, 613, 832))
        self.scrollAreaWidgetContents_sites.setObjectName("scrollAreaWidgetContents_sites")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_sites)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ligne_site = QtWidgets.QHBoxLayout()
        self.ligne_site.setContentsMargins(5, 10, 5, 10)
        self.ligne_site.setObjectName("ligne_site")
        self.site_web = QtWidgets.QLabel(self.scrollAreaWidgetContents_sites)
        self.site_web.setAlignment(QtCore.Qt.AlignCenter)
        self.site_web.setObjectName("site_web")
        self.ligne_site.addWidget(self.site_web)
        self.identifiant = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_sites)
        self.identifiant.setAlignment(QtCore.Qt.AlignCenter)
        self.identifiant.setObjectName("identifiant")
        self.ligne_site.addWidget(self.identifiant)
        self.mdp = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_sites)
        self.mdp.setMaximumSize(QtCore.QSize(16777215, 40))
        self.mdp.setObjectName("mdp")
        self.ligne_site.addWidget(self.mdp)
        self.categorie = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_sites)
        self.categorie.setEnabled(True)
        self.categorie.setText("")
        self.categorie.setObjectName("categorie")
        self.ligne_site.addWidget(self.categorie)
        self.verticalLayout.addLayout(self.ligne_site)
        self.scrollArea_sites.setWidget(self.scrollAreaWidgetContents_sites)
        self.Sites.addWidget(self.scrollArea_sites)
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.Categories = QtWidgets.QVBoxLayout(self.widget1)
        self.Categories.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.Categories.setObjectName("Categories")
        self.titre_cat = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.titre_cat.setFont(font)
        self.titre_cat.setAlignment(QtCore.Qt.AlignCenter)
        self.titre_cat.setIndent(0)
        self.titre_cat.setObjectName("titre_cat")
        self.Categories.addWidget(self.titre_cat)
        self.scrollArea_cat = QtWidgets.QScrollArea(self.widget1)
        self.scrollArea_cat.setWidgetResizable(True)
        self.scrollArea_cat.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea_cat.setObjectName("scrollArea_cat")
        self.scrollAreaWidgetContents_cat = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_cat.setGeometry(QtCore.QRect(0, 0, 240, 767))
        self.scrollAreaWidgetContents_cat.setObjectName("scrollAreaWidgetContents_cat")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_cat)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ligne_categorie = QtWidgets.QHBoxLayout()
        self.ligne_categorie.setObjectName("ligne_categorie")
        self.label_cat = QtWidgets.QLabel(self.scrollAreaWidgetContents_cat)
        self.label_cat.setMaximumSize(QtCore.QSize(16777215, 608))
        self.label_cat.setObjectName("label_cat")
        self.ligne_categorie.addWidget(self.label_cat)
        self.pushButton_cat = QtWidgets.QPushButton(self.scrollAreaWidgetContents_cat)
        self.pushButton_cat.setEnabled(True)
        self.pushButton_cat.setObjectName("pushButton_cat")
        self.ligne_categorie.addWidget(self.pushButton_cat)
        self.verticalLayout_3.addLayout(self.ligne_categorie)
        self.scrollArea_cat.setWidget(self.scrollAreaWidgetContents_cat)
        self.Categories.addWidget(self.scrollArea_cat)
        self.ajouter_cat = QtWidgets.QLineEdit(self.widget1)
        self.ajouter_cat.setMinimumSize(QtCore.QSize(0, 30))
        self.ajouter_cat.setText("")
        self.ajouter_cat.setAlignment(QtCore.Qt.AlignCenter)
        self.ajouter_cat.setObjectName("ajouter_cat")
        self.Categories.addWidget(self.ajouter_cat)
        self.Categories.setStretch(1, 4)
        self.Categories.setStretch(2, 1)
        self.horizontalLayout.addWidget(self.splitter)
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
        fenetreGestion.setTabOrder(self.identifiant, self.mdp)
        fenetreGestion.setTabOrder(self.mdp, self.categorie)
        fenetreGestion.setTabOrder(self.categorie, self.pushButton_cat)
        fenetreGestion.setTabOrder(self.pushButton_cat, self.scrollArea_cat)
        fenetreGestion.setTabOrder(self.scrollArea_cat, self.ajouter_cat)
        fenetreGestion.setTabOrder(self.ajouter_cat, self.pushButton_pwd)
        fenetreGestion.setTabOrder(self.pushButton_pwd, self.scrollArea_pwd)
        fenetreGestion.setTabOrder(self.scrollArea_pwd, self.ajouter_pwd)

    def retranslateUi(self, fenetreGestion):
        _translate = QtCore.QCoreApplication.translate
        fenetreGestion.setWindowTitle(_translate("fenetreGestion", "Fenêtre de Gestion - MindPass"))
        self.titre_pwd.setText(_translate("fenetreGestion", "Mots de Passe"))
        self.label_pwd.setText(_translate("fenetreGestion", "mdp"))
        self.pushButton_pwd.setText(_translate("fenetreGestion", "X"))
        self.site_web.setText(_translate("fenetreGestion", "Site 1"))
        self.identifiant.setText(_translate("fenetreGestion", "Identifiant"))
        self.mdp.setText(_translate("fenetreGestion", "mdp"))
        self.titre_cat.setText(_translate("fenetreGestion", "Catégories"))
        self.label_cat.setText(_translate("fenetreGestion", "cat1"))
        self.pushButton_cat.setText(_translate("fenetreGestion", "X"))
        self.menuAide.setTitle(_translate("fenetreGestion", "Aide"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fenetreGestion = QtWidgets.QMainWindow()
    ui = Ui_fenetreGestion()
    ui.setupUi(fenetreGestion)
    fenetreGestion.show()
    sys.exit(app.exec_())

