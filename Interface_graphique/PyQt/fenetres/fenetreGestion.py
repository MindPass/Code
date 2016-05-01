# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../UI/fenetreGestion.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

"""<Mindpass is a intelligent password manager written in Python3
    that checks your mailbox for logins and passwords that you do not remember.>
    Copyright (C) <2016>  <Cantaluppi Thibaut, Garchery Martial, Domain Alexandre, Boulmane Yassine>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>."""




from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fenetreGestion(object):
    def setupUi(self, fenetreGestion):
        fenetreGestion.setObjectName("fenetreGestion")
        fenetreGestion.setEnabled(True)
        fenetreGestion.resize(1200, 873)
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
"#titre_cat, #titre_pwd {\n"
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
"\n"
"#ajouter_cat, #ajouter_pwd  {\n"
"    border: solid 3px white;\n"
"}\n"
"\n"
"QPushButton#pushButton_ajout_site {\n"
"     background-color: transparent;\n"
"     border: none;\n"
"     image: url(\"../ressources/icones/check.svg\");\n"
" }\n"
"\n"
"QPushButton:hover#pushButton_ajout_site {\n"
"     image: url(\"../ressources/icones/check-vertclair.svg\");\n"
" }\n"
"\n"
" QPushButton:pressed#pushButton_ajout_site {\n"
"     image: url(\"../ressources/icones/check-vertfonce.svg\");\n"
" }\n"
"\n"
"QPushButton#pushButton_pwd, QPushButton#pushButton_cat {\n"
"     background-color: transparent;\n"
"     border: none;\n"
"     image: url(\"../ressources/icones/croix_757575.svg\");\n"
" }\n"
"\n"
"QPushButton:hover#pushButton_pwd, QPushButton:hover#pushButton_cat {\n"
"     image: url(\"../ressources/icones/croix_929292.svg\");\n"
" }\n"
"\n"
" QPushButton:pressed#pushButton_pwd, QPushButton:pressed#pushButton_cat {\n"
"     image: url(\"../ressources/icones/croix_575757.svg\");\n"
" }\n"
"\n"
"QScrollArea {\n"
"    background: transparent;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#scrollAreaWidgetContents_cat, #scrollAreaWidgetContents_pwd {\n"
"    background : rgba(255,255,255,44);\n"
"}\n"
"\n"
"QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 transparent, stop: 1 rgba(117,117,117,22));\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 2.5ex;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0 10px;\n"
"    color: #757575;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox > QLabel {\n"
"    color: rgba(255,255,255,200);\n"
"}\n"
"\n"
"QVBoxLayout > QHBoxLayout#libelles > QLabel {\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QStringList, QString, QStringView, QListView {\n"
"    background-color: white;\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    padding: 1px 5px 0px 0px;\n"
"    border-left-width: 2px;\n"
"    border-left-color: #757575;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(\"../ressources/icones/derouler.svg\");\n"
"}\n"
"\n"
"QComboBox::down-arrow:on {\n"
"    image: url(\"../ressources/icones/enrouler.svg\");\n"
"}\n"
"\n"
"/* perso test : remplacer par D:/Users/Alexandre/Desktop/MindPass/Code/Interface_graphique/PyQt/ressources/icones/ */")
        self.corps_gestion = QtWidgets.QWidget(fenetreGestion)
        self.corps_gestion.setEnabled(True)
        self.corps_gestion.setStyleSheet("")
        self.corps_gestion.setObjectName("corps_gestion")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.corps_gestion)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.corps_gestion)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(0)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.Categories = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.Categories.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.Categories.setObjectName("Categories")
        self.titre_cat = QtWidgets.QLabel(self.layoutWidget)
        self.titre_cat.setMinimumSize(QtCore.QSize(210, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.titre_cat.setFont(font)
        self.titre_cat.setAlignment(QtCore.Qt.AlignCenter)
        self.titre_cat.setIndent(0)
        self.titre_cat.setObjectName("titre_cat")
        self.Categories.addWidget(self.titre_cat)
        self.scrollArea_cat = QtWidgets.QScrollArea(self.layoutWidget)
        self.scrollArea_cat.setWidgetResizable(True)
        self.scrollArea_cat.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea_cat.setObjectName("scrollArea_cat")
        self.scrollAreaWidgetContents_cat = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_cat.setGeometry(QtCore.QRect(0, 0, 250, 667))
        self.scrollAreaWidgetContents_cat.setMinimumSize(QtCore.QSize(250, 0))
        self.scrollAreaWidgetContents_cat.setObjectName("scrollAreaWidgetContents_cat")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_cat)
        self.verticalLayout_3.setContentsMargins(-1, -1, 14, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea_cat.setWidget(self.scrollAreaWidgetContents_cat)
        self.Categories.addWidget(self.scrollArea_cat)
        self.ajouter_cat = QtWidgets.QLineEdit(self.layoutWidget)
        self.ajouter_cat.setMinimumSize(QtCore.QSize(0, 30))
        self.ajouter_cat.setText("")
        self.ajouter_cat.setAlignment(QtCore.Qt.AlignCenter)
        self.ajouter_cat.setObjectName("ajouter_cat")
        self.Categories.addWidget(self.ajouter_cat)
        self.Categories.setStretch(1, 4)
        self.Categories.setStretch(2, 1)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.Sites = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.Sites.setObjectName("Sites")
        self.libelles = QtWidgets.QHBoxLayout()
        self.libelles.setObjectName("libelles")
        self.libelle_site = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.libelle_site.setFont(font)
        self.libelle_site.setAlignment(QtCore.Qt.AlignCenter)
        self.libelle_site.setObjectName("libelle_site")
        self.libelles.addWidget(self.libelle_site)
        self.libelle_id = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.libelle_id.setFont(font)
        self.libelle_id.setAlignment(QtCore.Qt.AlignCenter)
        self.libelle_id.setObjectName("libelle_id")
        self.libelles.addWidget(self.libelle_id)
        self.libelle_pwd = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.libelle_pwd.setFont(font)
        self.libelle_pwd.setAlignment(QtCore.Qt.AlignCenter)
        self.libelle_pwd.setObjectName("libelle_pwd")
        self.libelles.addWidget(self.libelle_pwd)
        self.libelle_categorie = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.libelle_categorie.setFont(font)
        self.libelle_categorie.setAlignment(QtCore.Qt.AlignCenter)
        self.libelle_categorie.setObjectName("libelle_categorie")
        self.libelles.addWidget(self.libelle_categorie)
        self.Sites.addLayout(self.libelles)
        self.scrollArea_sites = QtWidgets.QScrollArea(self.verticalLayoutWidget_2)
        self.scrollArea_sites.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_sites.sizePolicy().hasHeightForWidth())
        self.scrollArea_sites.setSizePolicy(sizePolicy)
        self.scrollArea_sites.setMinimumSize(QtCore.QSize(500, 0))
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
        self.scrollAreaWidgetContents_sites.setGeometry(QtCore.QRect(0, 0, 715, 703))
        self.scrollAreaWidgetContents_sites.setObjectName("scrollAreaWidgetContents_sites")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_sites)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea_sites.setWidget(self.scrollAreaWidgetContents_sites)
        self.Sites.addWidget(self.scrollArea_sites)
        self.ajout_site = QtWidgets.QHBoxLayout()
        self.ajout_site.setObjectName("ajout_site")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ajout_site.addItem(spacerItem)
        self.lineEdit_ajout_site = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_ajout_site.setObjectName("lineEdit_ajout_site")
        self.ajout_site.addWidget(self.lineEdit_ajout_site)
        self.pushButton_ajout_site = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_ajout_site.setText("")
        self.pushButton_ajout_site.setObjectName("pushButton_ajout_site")
        self.ajout_site.addWidget(self.pushButton_ajout_site)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ajout_site.addItem(spacerItem1)
        self.ajout_site.setStretch(0, 4)
        self.ajout_site.setStretch(1, 10)
        self.ajout_site.setStretch(2, 1)
        self.ajout_site.setStretch(3, 3)
        self.Sites.addLayout(self.ajout_site)
        self.Sites.setStretch(0, 1)
        self.Sites.setStretch(1, 20)
        self.Sites.setStretch(2, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.Passwords = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.Passwords.setObjectName("Passwords")
        self.titre_pwd = QtWidgets.QLabel(self.layoutWidget1)
        self.titre_pwd.setMinimumSize(QtCore.QSize(210, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.titre_pwd.setFont(font)
        self.titre_pwd.setAlignment(QtCore.Qt.AlignCenter)
        self.titre_pwd.setIndent(0)
        self.titre_pwd.setObjectName("titre_pwd")
        self.Passwords.addWidget(self.titre_pwd)
        self.scrollArea_pwd = QtWidgets.QScrollArea(self.layoutWidget1)
        self.scrollArea_pwd.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea_pwd.setWidgetResizable(True)
        self.scrollArea_pwd.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea_pwd.setObjectName("scrollArea_pwd")
        self.scrollAreaWidgetContents_pwd = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_pwd.setGeometry(QtCore.QRect(0, 0, 222, 701))
        self.scrollAreaWidgetContents_pwd.setObjectName("scrollAreaWidgetContents_pwd")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_pwd)
        self.verticalLayout_2.setContentsMargins(-1, -1, 14, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea_pwd.setWidget(self.scrollAreaWidgetContents_pwd)
        self.Passwords.addWidget(self.scrollArea_pwd)
        self.ajouter_pwd = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ajouter_pwd.setMinimumSize(QtCore.QSize(0, 30))
        self.ajouter_pwd.setText("")
        self.ajouter_pwd.setAlignment(QtCore.Qt.AlignCenter)
        self.ajouter_pwd.setObjectName("ajouter_pwd")
        self.Passwords.addWidget(self.ajouter_pwd)
        self.Passwords.setStretch(2, 1)
        self.horizontalLayout.addWidget(self.splitter)
        fenetreGestion.setCentralWidget(self.corps_gestion)
        self.menubar = QtWidgets.QMenuBar(fenetreGestion)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 38))
        self.menubar.setObjectName("menubar")
        self.menuAide = QtWidgets.QMenu(self.menubar)
        self.menuAide.setObjectName("menuAide")
        self.menuFichier = QtWidgets.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuOutils = QtWidgets.QMenu(self.menubar)
        self.menuOutils.setObjectName("menuOutils")
        self.menuConfidentialite = QtWidgets.QMenu(self.menuOutils)
        self.menuConfidentialite.setObjectName("menuConfidentialite")
        self.menuChanger_de_langue = QtWidgets.QMenu(self.menuOutils)
        self.menuChanger_de_langue.setObjectName("menuChanger_de_langue")
        fenetreGestion.setMenuBar(self.menubar)
        self.actionPreferences = QtWidgets.QAction(fenetreGestion)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../ressources/icones/paramètres.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreferences.setIcon(icon1)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionObtenir_de_l_aide = QtWidgets.QAction(fenetreGestion)
        self.actionObtenir_de_l_aide.setObjectName("actionObtenir_de_l_aide")
        self.actionA_propos_de_MindPass = QtWidgets.QAction(fenetreGestion)
        self.actionA_propos_de_MindPass.setObjectName("actionA_propos_de_MindPass")
        self.actionMode_deux_lettres = QtWidgets.QAction(fenetreGestion)
        self.actionMode_deux_lettres.setCheckable(True)
        self.actionMode_deux_lettres.setObjectName("actionMode_deux_lettres")
        self.actionMode_complet = QtWidgets.QAction(fenetreGestion)
        self.actionMode_complet.setCheckable(True)
        self.actionMode_complet.setChecked(True)
        self.actionMode_complet.setObjectName("actionMode_complet")
        self.actionFrancais = QtWidgets.QAction(fenetreGestion)
        self.actionFrancais.setCheckable(True)
        self.actionFrancais.setChecked(True)
        self.actionFrancais.setObjectName("actionFrancais")
        self.actionEnglish = QtWidgets.QAction(fenetreGestion)
        self.actionEnglish.setCheckable(True)
        self.actionEnglish.setObjectName("actionEnglish")
        self.actionFermer = QtWidgets.QAction(fenetreGestion)
        self.actionFermer.setObjectName("actionFermer")
        self.menuAide.addAction(self.actionObtenir_de_l_aide)
        self.menuAide.addSeparator()
        self.menuAide.addAction(self.actionA_propos_de_MindPass)
        self.menuFichier.addAction(self.actionFermer)
        self.menuConfidentialite.addAction(self.actionMode_deux_lettres)
        self.menuConfidentialite.addAction(self.actionMode_complet)
        self.menuChanger_de_langue.addAction(self.actionFrancais)
        self.menuChanger_de_langue.addAction(self.actionEnglish)
        self.menuOutils.addAction(self.menuChanger_de_langue.menuAction())
        self.menuOutils.addSeparator()
        self.menuOutils.addAction(self.menuConfidentialite.menuAction())
        self.menuOutils.addAction(self.actionPreferences)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuOutils.menuAction())
        self.menubar.addAction(self.menuAide.menuAction())

        self.retranslateUi(fenetreGestion)
        self.actionFermer.triggered.connect(fenetreGestion.close)
        QtCore.QMetaObject.connectSlotsByName(fenetreGestion)
        fenetreGestion.setTabOrder(self.scrollArea_cat, self.ajouter_cat)
        fenetreGestion.setTabOrder(self.ajouter_cat, self.scrollArea_pwd)
        fenetreGestion.setTabOrder(self.scrollArea_pwd, self.ajouter_pwd)

    def retranslateUi(self, fenetreGestion):
        _translate = QtCore.QCoreApplication.translate
        fenetreGestion.setWindowTitle(_translate("fenetreGestion", "Fenêtre de Gestion - MindPass"))
        self.titre_cat.setText(_translate("fenetreGestion", "Catégories"))
        self.libelle_site.setText(_translate("fenetreGestion", "Site"))
        self.libelle_id.setText(_translate("fenetreGestion", "Identifiant"))
        self.libelle_pwd.setText(_translate("fenetreGestion", "Mot de Passe"))
        self.libelle_categorie.setText(_translate("fenetreGestion", "Catégorie"))
        self.titre_pwd.setText(_translate("fenetreGestion", "Mots de Passe"))
        self.menuAide.setTitle(_translate("fenetreGestion", "Aide"))
        self.menuFichier.setTitle(_translate("fenetreGestion", "Fichier"))
        self.menuOutils.setTitle(_translate("fenetreGestion", "Outils"))
        self.menuConfidentialite.setTitle(_translate("fenetreGestion", "Affichage"))
        self.menuChanger_de_langue.setTitle(_translate("fenetreGestion", "Changer de langue"))
        self.actionPreferences.setText(_translate("fenetreGestion", "Préférences"))
        self.actionObtenir_de_l_aide.setText(_translate("fenetreGestion", "Obtenir de l\'aide"))
        self.actionObtenir_de_l_aide.setShortcut(_translate("fenetreGestion", "F1"))
        self.actionA_propos_de_MindPass.setText(_translate("fenetreGestion", "À propos de MindPass"))
        self.actionMode_deux_lettres.setText(_translate("fenetreGestion", "Mode \"deux lettres\""))
        self.actionMode_deux_lettres.setToolTip(_translate("fenetreGestion", "N\'affiche que les 2 premières lettres de tous vos mots de passe à l\'écran"))
        self.actionMode_complet.setText(_translate("fenetreGestion", "Mode complet"))
        self.actionMode_complet.setToolTip(_translate("fenetreGestion", "Affiche tous vos mots de passe de façon explicite à l\'écran"))
        self.actionFrancais.setText(_translate("fenetreGestion", "Français"))
        self.actionEnglish.setText(_translate("fenetreGestion", "English"))
        self.actionFermer.setText(_translate("fenetreGestion", "Fermer"))
        self.actionFermer.setShortcut(_translate("fenetreGestion", "Alt+F4"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fenetreGestion = QtWidgets.QMainWindow()
    ui = Ui_fenetreGestion()
    ui.setupUi(fenetreGestion)
    fenetreGestion.show()
    sys.exit(app.exec_())

