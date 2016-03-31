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
        icon.addPixmap(QtGui.QPixmap("ressources/MindPass-icone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        fenetreAccueil.setWindowIcon(icon)
        fenetreAccueil.setStyleSheet("")
        with open("../style/fenetreAccueil.css", "r") as feuilleDeStyle:
            fenetreAccueil.setStyleSheet(feuilleDeStyle.read())
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
        self.label.setPixmap(QtGui.QPixmap("ressources/MindPass-transparent.svg"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        fenetreAccueil.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(fenetreAccueil)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 38))
        self.menubar.setObjectName("menubar")
        self.menuMindPass = QtWidgets.QMenu(self.menubar)
        self.menuMindPass.setObjectName("menuMindPass")
        self.menuOutils = QtWidgets.QMenu(self.menubar)
        self.menuOutils.setObjectName("menuOutils")
        self.menuChanger_de_langue = QtWidgets.QMenu(self.menuOutils)
        self.menuChanger_de_langue.setObjectName("menuChanger_de_langue")
        self.menuAide = QtWidgets.QMenu(self.menubar)
        self.menuAide.setObjectName("menuAide")
        fenetreAccueil.setMenuBar(self.menubar)
        self.actionFermer = QtWidgets.QAction(fenetreAccueil)
        self.actionFermer.setObjectName("actionFermer")
        self.actionFran_ais = QtWidgets.QAction(fenetreAccueil)
        self.actionFran_ais.setCheckable(True)
        self.actionFran_ais.setChecked(True)
        self.actionFran_ais.setObjectName("actionFran_ais")
        self.actionAnglais = QtWidgets.QAction(fenetreAccueil)
        self.actionAnglais.setCheckable(True)
        self.actionAnglais.setObjectName("actionAnglais")
        self.actionObtenir_de_l_aide = QtWidgets.QAction(fenetreAccueil)
        self.actionObtenir_de_l_aide.setObjectName("actionObtenir_de_l_aide")
        self.actionA_propos_de_MindPass = QtWidgets.QAction(fenetreAccueil)
        self.actionA_propos_de_MindPass.setObjectName("actionA_propos_de_MindPass")
        self.actionPr_f_rences = QtWidgets.QAction(fenetreAccueil)
        self.actionPr_f_rences.setObjectName("actionPr_f_rences")
        self.menuMindPass.addAction(self.actionFermer)
        self.menuChanger_de_langue.addAction(self.actionFran_ais)
        self.menuChanger_de_langue.addAction(self.actionAnglais)
        self.menuOutils.addAction(self.menuChanger_de_langue.menuAction())
        self.menuOutils.addSeparator()
        self.menuOutils.addAction(self.actionPr_f_rences)
        self.menuAide.addAction(self.actionObtenir_de_l_aide)
        self.menuAide.addSeparator()
        self.menuAide.addAction(self.actionA_propos_de_MindPass)
        self.menubar.addAction(self.menuMindPass.menuAction())
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
        self.menuMindPass.setTitle(_translate("fenetreAccueil", "MindPass"))
        self.menuOutils.setTitle(_translate("fenetreAccueil", "Outils"))
        self.menuChanger_de_langue.setTitle(_translate("fenetreAccueil", "Changer de langue"))
        self.menuAide.setTitle(_translate("fenetreAccueil", "Aide"))
        self.actionFermer.setText(_translate("fenetreAccueil", "Fermer"))
        self.actionFermer.setShortcut(_translate("fenetreAccueil", "Alt+F4"))
        self.actionFran_ais.setText(_translate("fenetreAccueil", "Français"))
        self.actionAnglais.setText(_translate("fenetreAccueil", "Anglais"))
        self.actionObtenir_de_l_aide.setText(_translate("fenetreAccueil", "Obtenir de l\'aide"))
        self.actionObtenir_de_l_aide.setShortcut(_translate("fenetreAccueil", "F1"))
        self.actionA_propos_de_MindPass.setText(_translate("fenetreAccueil", "A propos de MindPass"))
        self.actionPr_f_rences.setText(_translate("fenetreAccueil", "Préférences"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fenetreAccueil = QtWidgets.QMainWindow()
    ui = Ui_fenetreAccueil()
    ui.setupUi(fenetreAccueil)
    fenetreAccueil.show()
    sys.exit(app.exec_())

