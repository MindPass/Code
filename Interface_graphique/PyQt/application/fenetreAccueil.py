# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../UI/fenetreAccueil.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fenetreAccueil(object):
    def setupUi(self, fenetreAccueil):
        fenetreAccueil.setObjectName("fenetreAccueil")
        fenetreAccueil.resize(800, 500)
        fenetreAccueil.setMinimumSize(QtCore.QSize(800, 500))
        fenetreAccueil.setMaximumSize(QtCore.QSize(800, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ressources/MindPass-icone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        fenetreAccueil.setWindowIcon(icon)
        fenetreAccueil.setStyleSheet("QMainWindow {\n"
"    background: qradialgradient(spread:pad, cx:0, cy:1, radius:1.406, fx:0, fy:1, stop:0 rgba(244, 216, 148, 255), stop:1 rgba(255, 102, 102, 255));\n"
"}\n"
"\n"
"QLabel, QCheckBox {\n"
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
"\n"
"QLineEdit:hover {\n"
"    background: rgba(255,255,255,75);\n"
"}\n"
"\n"
"QPushButton {\n"
"    border-radius: 2px;\n"
"    padding: 0.2em 0.2em 0.3em 0.2em;\n"
"    border: 1px solid rgba(100, 100, 100, 200);\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #f4f4f4, stop:0.1 #8F8F8F, stop:1 #a1a1a1);\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 1px solid rgba(255, 255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-radius: 2px;\n"
"    padding: 0.2em 0.2em 0.3em 0.2em;\n"
"    border: 1px solid rgba(100, 100, 100, 200);\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #a1a1a1, stop:0.1 #8F8F8F, stop:1 #f4f4f4);\n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(fenetreAccueil)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 250, 168, 51))
        self.pushButton.setObjectName("pushButton")
        self.label_id = QtWidgets.QLabel(self.centralwidget)
        self.label_id.setGeometry(QtCore.QRect(80, 70, 148, 35))
        self.label_id.setAlignment(QtCore.Qt.AlignCenter)
        self.label_id.setObjectName("label_id")
        self.label_mdp = QtWidgets.QLabel(self.centralwidget)
        self.label_mdp.setGeometry(QtCore.QRect(80, 140, 148, 35))
        self.label_mdp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mdp.setObjectName("label_mdp")
        self.lineEdit_id = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_id.setGeometry(QtCore.QRect(310, 70, 390, 35))
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.lineEdit_mdp = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_mdp.setGeometry(QtCore.QRect(310, 140, 390, 35))
        self.lineEdit_mdp.setObjectName("lineEdit_mdp")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 350, 500, 100))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../ressources/MindPass-transparent.svg"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horsConnexion = QtWidgets.QCheckBox(self.centralwidget)
        self.horsConnexion.setGeometry(QtCore.QRect(310, 200, 161, 17))
        self.horsConnexion.setObjectName("horsConnexion")
        self.label_erreur = QtWidgets.QLabel(self.centralwidget)
        self.label_erreur.setGeometry(QtCore.QRect(310, 50, 381, 21))
        self.label_erreur.setText("")
        self.label_erreur.setObjectName("label_erreur")
        fenetreAccueil.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(fenetreAccueil)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFichier = QtWidgets.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuOutils = QtWidgets.QMenu(self.menubar)
        self.menuOutils.setObjectName("menuOutils")
        self.menuChanger_de_langue = QtWidgets.QMenu(self.menuOutils)
        self.menuChanger_de_langue.setObjectName("menuChanger_de_langue")
        self.menuAide = QtWidgets.QMenu(self.menubar)
        self.menuAide.setObjectName("menuAide")
        fenetreAccueil.setMenuBar(self.menubar)
        self.actionFermer = QtWidgets.QAction(fenetreAccueil)
        self.actionFermer.setObjectName("actionFermer")
        self.actionFrancais = QtWidgets.QAction(fenetreAccueil)
        self.actionFrancais.setCheckable(True)
        self.actionFrancais.setChecked(True)
        self.actionFrancais.setObjectName("actionFrancais")
        self.actionEnglish = QtWidgets.QAction(fenetreAccueil)
        self.actionEnglish.setCheckable(True)
        self.actionEnglish.setObjectName("actionEnglish")
        self.actionObtenir_de_l_aide = QtWidgets.QAction(fenetreAccueil)
        self.actionObtenir_de_l_aide.setObjectName("actionObtenir_de_l_aide")
        self.actionA_propos_de_MindPass = QtWidgets.QAction(fenetreAccueil)
        self.actionA_propos_de_MindPass.setObjectName("actionA_propos_de_MindPass")
        self.actionPreferences = QtWidgets.QAction(fenetreAccueil)
        self.actionPreferences.setObjectName("actionPreferences")
        self.menuFichier.addAction(self.actionFermer)
        self.menuChanger_de_langue.addAction(self.actionFrancais)
        self.menuChanger_de_langue.addAction(self.actionEnglish)
        self.menuOutils.addAction(self.menuChanger_de_langue.menuAction())
        self.menuOutils.addSeparator()
        self.menuOutils.addAction(self.actionPreferences)
        self.menuAide.addAction(self.actionObtenir_de_l_aide)
        self.menuAide.addSeparator()
        self.menuAide.addAction(self.actionA_propos_de_MindPass)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuOutils.menuAction())
        self.menubar.addAction(self.menuAide.menuAction())

        self.retranslateUi(fenetreAccueil)
        self.actionFermer.triggered.connect(fenetreAccueil.close)
        QtCore.QMetaObject.connectSlotsByName(fenetreAccueil)

    def retranslateUi(self, fenetreAccueil):
        _translate = QtCore.QCoreApplication.translate
        fenetreAccueil.setWindowTitle(_translate("fenetreAccueil", "MindPass"))
        self.pushButton.setText(_translate("fenetreAccueil", "Se connecter"))
        self.label_id.setText(_translate("fenetreAccueil", "Adresse email"))
        self.label_mdp.setText(_translate("fenetreAccueil", "Mot de passe"))
        self.horsConnexion.setText(_translate("fenetreAccueil", "Mode hors connexion"))
        self.menuFichier.setTitle(_translate("fenetreAccueil", "Fichier"))
        self.menuOutils.setTitle(_translate("fenetreAccueil", "Outils"))
        self.menuChanger_de_langue.setTitle(_translate("fenetreAccueil", "Changer de langue"))
        self.menuAide.setTitle(_translate("fenetreAccueil", "Aide"))
        self.actionFermer.setText(_translate("fenetreAccueil", "Fermer"))
        self.actionFermer.setShortcut(_translate("fenetreAccueil", "Alt+F4"))
        self.actionFrancais.setText(_translate("fenetreAccueil", "Français"))
        self.actionEnglish.setText(_translate("fenetreAccueil", "English"))
        self.actionObtenir_de_l_aide.setText(_translate("fenetreAccueil", "Obtenir de l\'aide"))
        self.actionObtenir_de_l_aide.setShortcut(_translate("fenetreAccueil", "F1"))
        self.actionA_propos_de_MindPass.setText(_translate("fenetreAccueil", "À propos de MindPass"))
        self.actionPreferences.setText(_translate("fenetreAccueil", "Préférences"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fenetreAccueil = QtWidgets.QMainWindow()
    ui = Ui_fenetreAccueil()
    ui.setupUi(fenetreAccueil)
    fenetreAccueil.show()
    sys.exit(app.exec_())

