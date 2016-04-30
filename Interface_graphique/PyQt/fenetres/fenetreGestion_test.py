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
" QPushButton {\n"
"     background-color: transparent;\n"
"     border: none;\n"
"     image: url(\"D:/Users/Alexandre/Desktop/MindPass/croix_757575.svg\");\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"     image: url(\"D:/Users/Alexandre/Desktop/MindPass/croix_929292.svg\");\n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"     image: url(\"D:/Users/Alexandre/Desktop/MindPass/croix_575757.svg\");\n"
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
"    margin-top: 2.5ex; /* leave space at the top for the title */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 10px;\n"
"    color: #757575;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox > QLabel {\n"
"    color: rgba(255,255,255,200);\n"
"}")
        self.corps_gestion = QtWidgets.QWidget(fenetreGestion)
        self.corps_gestion.setEnabled(True)
        self.corps_gestion.setObjectName("corps_gestion")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.corps_gestion)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.corps_gestion)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(0)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.Passwords = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.Passwords.setObjectName("Passwords")
        self.titre_pwd = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.titre_pwd.setFont(font)
        self.titre_pwd.setAlignment(QtCore.Qt.AlignCenter)
        self.titre_pwd.setIndent(0)
        self.titre_pwd.setObjectName("titre_pwd")
        self.Passwords.addWidget(self.titre_pwd)
        self.scrollArea_pwd = QtWidgets.QScrollArea(self.layoutWidget)
        self.scrollArea_pwd.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea_pwd.setWidgetResizable(True)
        self.scrollArea_pwd.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea_pwd.setObjectName("scrollArea_pwd")
        self.scrollAreaWidgetContents_pwd = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_pwd.setGeometry(QtCore.QRect(0, 0, 196, 769))
        self.scrollAreaWidgetContents_pwd.setObjectName("scrollAreaWidgetContents_pwd")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_pwd)
        self.verticalLayout_2.setContentsMargins(-1, -1, 14, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ligne_pwd = QtWidgets.QHBoxLayout()
        self.ligne_pwd.setObjectName("ligne_pwd")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_pwd)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.sites_lies_pwd_2 = QtWidgets.QLabel(self.groupBox)
        self.sites_lies_pwd_2.setObjectName("sites_lies_pwd_2")
        self.verticalLayout_4.addWidget(self.sites_lies_pwd_2)
        self.sites_lies_pwd = QtWidgets.QLabel(self.groupBox)
        self.sites_lies_pwd.setObjectName("sites_lies_pwd")
        self.verticalLayout_4.addWidget(self.sites_lies_pwd)
        self.sites_lies_pwd_3 = QtWidgets.QLabel(self.groupBox)
        self.sites_lies_pwd_3.setObjectName("sites_lies_pwd_3")
        self.verticalLayout_4.addWidget(self.sites_lies_pwd_3)
        self.ligne_pwd.addWidget(self.groupBox)
        self.pushButton_pwd = QtWidgets.QPushButton(self.scrollAreaWidgetContents_pwd)
        self.pushButton_pwd.setEnabled(True)
        self.pushButton_pwd.setMaximumSize(QtCore.QSize(36, 36))
        self.pushButton_pwd.setText("")
        self.pushButton_pwd.setObjectName("pushButton_pwd")
        self.ligne_pwd.addWidget(self.pushButton_pwd)
        self.verticalLayout_2.addLayout(self.ligne_pwd)
        self.scrollArea_pwd.setWidget(self.scrollAreaWidgetContents_pwd)
        self.Passwords.addWidget(self.scrollArea_pwd)
        self.ajouter_pwd = QtWidgets.QLineEdit(self.layoutWidget)
        self.ajouter_pwd.setMinimumSize(QtCore.QSize(0, 30))
        self.ajouter_pwd.setText("")
        self.ajouter_pwd.setAlignment(QtCore.Qt.AlignCenter)
        self.ajouter_pwd.setObjectName("ajouter_pwd")
        self.Passwords.addWidget(self.ajouter_pwd)
        self.Passwords.setStretch(2, 1)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.Sites = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.Sites.setObjectName("Sites")
        self.intitule = QtWidgets.QHBoxLayout()
        self.intitule.setObjectName("intitule")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.intitule.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.intitule.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.intitule.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.intitule.addWidget(self.label)
        self.Sites.addLayout(self.intitule)
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
        self.scrollAreaWidgetContents_sites.setGeometry(QtCore.QRect(0, 0, 784, 746))
        self.scrollAreaWidgetContents_sites.setObjectName("scrollAreaWidgetContents_sites")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_sites)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ligne_site = QtWidgets.QHBoxLayout()
        self.ligne_site.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
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
        self.mdp = QtWidgets.QComboBox(self.scrollAreaWidgetContents_sites)
        self.mdp.setObjectName("mdp")
        self.ligne_site.addWidget(self.mdp)
        self.categorie = QtWidgets.QComboBox(self.scrollAreaWidgetContents_sites)
        self.categorie.setObjectName("categorie")
        self.ligne_site.addWidget(self.categorie)
        self.ligne_site.setStretch(0, 2)
        self.ligne_site.setStretch(1, 2)
        self.ligne_site.setStretch(2, 2)
        self.ligne_site.setStretch(3, 2)
        self.verticalLayout.addLayout(self.ligne_site)
        self.scrollArea_sites.setWidget(self.scrollAreaWidgetContents_sites)
        self.Sites.addWidget(self.scrollArea_sites)
        self.ajout_site = QtWidgets.QHBoxLayout()
        self.ajout_site.setObjectName("ajout_site")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.ajout_site.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.ajout_site.addWidget(self.pushButton)
        self.ajout_site.setStretch(0, 1)
        self.ajout_site.setStretch(1, 1)
        self.Sites.addLayout(self.ajout_site)
        self.Sites.setStretch(0, 1)
        self.Sites.setStretch(1, 20)
        self.Sites.setStretch(2, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.Categories = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.Categories.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.Categories.setObjectName("Categories")
        self.titre_cat = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.titre_cat.setFont(font)
        self.titre_cat.setAlignment(QtCore.Qt.AlignCenter)
        self.titre_cat.setIndent(0)
        self.titre_cat.setObjectName("titre_cat")
        self.Categories.addWidget(self.titre_cat)
        self.scrollArea_cat = QtWidgets.QScrollArea(self.layoutWidget1)
        self.scrollArea_cat.setWidgetResizable(True)
        self.scrollArea_cat.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea_cat.setObjectName("scrollArea_cat")
        self.scrollAreaWidgetContents_cat = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_cat.setGeometry(QtCore.QRect(0, 0, 196, 769))
        self.scrollAreaWidgetContents_cat.setObjectName("scrollAreaWidgetContents_cat")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_cat)
        self.verticalLayout_3.setContentsMargins(-1, -1, 14, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ligne_categorie = QtWidgets.QHBoxLayout()
        self.ligne_categorie.setObjectName("ligne_categorie")
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_cat)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.sites_lies_cat = QtWidgets.QLabel(self.groupBox_2)
        self.sites_lies_cat.setObjectName("sites_lies_cat")
        self.verticalLayout_5.addWidget(self.sites_lies_cat)
        self.sites_lies_cat_2 = QtWidgets.QLabel(self.groupBox_2)
        self.sites_lies_cat_2.setObjectName("sites_lies_cat_2")
        self.verticalLayout_5.addWidget(self.sites_lies_cat_2)
        self.sites_lies_cat_3 = QtWidgets.QLabel(self.groupBox_2)
        self.sites_lies_cat_3.setObjectName("sites_lies_cat_3")
        self.verticalLayout_5.addWidget(self.sites_lies_cat_3)
        self.ligne_categorie.addWidget(self.groupBox_2)
        self.pushButton_cat = QtWidgets.QPushButton(self.scrollAreaWidgetContents_cat)
        self.pushButton_cat.setEnabled(True)
        self.pushButton_cat.setMaximumSize(QtCore.QSize(36, 36))
        self.pushButton_cat.setText("")
        self.pushButton_cat.setObjectName("pushButton_cat")
        self.ligne_categorie.addWidget(self.pushButton_cat)
        self.verticalLayout_3.addLayout(self.ligne_categorie)
        self.scrollArea_cat.setWidget(self.scrollAreaWidgetContents_cat)
        self.Categories.addWidget(self.scrollArea_cat)
        self.ajouter_cat = QtWidgets.QLineEdit(self.layoutWidget1)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        self.menuAide = QtWidgets.QMenu(self.menubar)
        self.menuAide.setObjectName("menuAide")
        self.menuMindMap = QtWidgets.QMenu(self.menubar)
        self.menuMindMap.setObjectName("menuMindMap")
        fenetreGestion.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuMindMap.menuAction())
        self.menubar.addAction(self.menuAide.menuAction())

        self.retranslateUi(fenetreGestion)
        QtCore.QMetaObject.connectSlotsByName(fenetreGestion)
        fenetreGestion.setTabOrder(self.identifiant, self.pushButton_cat)
        fenetreGestion.setTabOrder(self.pushButton_cat, self.scrollArea_cat)
        fenetreGestion.setTabOrder(self.scrollArea_cat, self.ajouter_cat)
        fenetreGestion.setTabOrder(self.ajouter_cat, self.pushButton_pwd)
        fenetreGestion.setTabOrder(self.pushButton_pwd, self.scrollArea_pwd)
        fenetreGestion.setTabOrder(self.scrollArea_pwd, self.ajouter_pwd)

    def retranslateUi(self, fenetreGestion):
        _translate = QtCore.QCoreApplication.translate
        fenetreGestion.setWindowTitle(_translate("fenetreGestion", "Fenêtre de Gestion - MindPass"))
        self.titre_pwd.setText(_translate("fenetreGestion", "Mots de Passe"))
        self.groupBox.setTitle(_translate("fenetreGestion", "GroupBox"))
        self.sites_lies_pwd_2.setText(_translate("fenetreGestion", "TextLabel"))
        self.sites_lies_pwd.setText(_translate("fenetreGestion", "TextLabel"))
        self.sites_lies_pwd_3.setText(_translate("fenetreGestion", "TextLabel"))
        self.label_4.setText(_translate("fenetreGestion", "Site"))
        self.label_3.setText(_translate("fenetreGestion", "Identifiant"))
        self.label_2.setText(_translate("fenetreGestion", "Mot de Passe"))
        self.label.setText(_translate("fenetreGestion", "Catégorie"))
        self.site_web.setText(_translate("fenetreGestion", "Site 1"))
        self.identifiant.setText(_translate("fenetreGestion", "Identifiant"))
        self.pushButton.setText(_translate("fenetreGestion", "Ajouter"))
        self.titre_cat.setText(_translate("fenetreGestion", "Catégories"))
        self.groupBox_2.setTitle(_translate("fenetreGestion", "GroupBox"))
        self.sites_lies_cat.setText(_translate("fenetreGestion", "TextLabel"))
        self.sites_lies_cat_2.setText(_translate("fenetreGestion", "TextLabel"))
        self.sites_lies_cat_3.setText(_translate("fenetreGestion", "TextLabel"))
        self.menuAide.setTitle(_translate("fenetreGestion", "Aide"))
        self.menuMindMap.setTitle(_translate("fenetreGestion", "Voir la MindMap"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fenetreGestion = QtWidgets.QMainWindow()
    ui = Ui_fenetreGestion()
    ui.setupUi(fenetreGestion)
    fenetreGestion.show()
    sys.exit(app.exec_())

