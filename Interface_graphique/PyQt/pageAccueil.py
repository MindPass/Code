# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pageAccueil.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        MainWindow.setMaximumSize(QtCore.QSize(800, 500))
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ressources/MindPass-icone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        
        with open("style/pageAccueil.css","r") as feuilleDeStyle:
            MainWindow.setStyleSheet(feuilleDeStyle.read())
            
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuMindPass = QtWidgets.QMenu(self.menubar)
        self.menuMindPass.setObjectName("menuMindPass")
        self.menuOutils = QtWidgets.QMenu(self.menubar)
        self.menuOutils.setObjectName("menuOutils")
        self.menuChanger_de_langue = QtWidgets.QMenu(self.menuOutils)
        self.menuChanger_de_langue.setObjectName("menuChanger_de_langue")
        self.menuAide = QtWidgets.QMenu(self.menubar)
        self.menuAide.setObjectName("menuAide")
        MainWindow.setMenuBar(self.menubar)
        self.actionFermer = QtWidgets.QAction(MainWindow)
        self.actionFermer.setObjectName("actionFermer")
        self.actionFran_ais = QtWidgets.QAction(MainWindow)
        self.actionFran_ais.setCheckable(True)
        self.actionFran_ais.setChecked(True)
        self.actionFran_ais.setObjectName("actionFran_ais")
        self.actionAnglais = QtWidgets.QAction(MainWindow)
        self.actionAnglais.setCheckable(True)
        self.actionAnglais.setObjectName("actionAnglais")
        self.actionObtenir_de_l_aide = QtWidgets.QAction(MainWindow)
        self.actionObtenir_de_l_aide.setObjectName("actionObtenir_de_l_aide")
        self.actionA_propos_de_MindPass = QtWidgets.QAction(MainWindow)
        self.actionA_propos_de_MindPass.setObjectName("actionA_propos_de_MindPass")
        self.actionPr_f_rences = QtWidgets.QAction(MainWindow)
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MindPass"))
        self.pushButton.setText(_translate("MainWindow", "Se connecter"))
        self.label_id.setText(_translate("MainWindow", "Adresse email"))
        self.label_mdp.setText(_translate("MainWindow", "Mot de passe"))
        self.menuMindPass.setTitle(_translate("MainWindow", "MindPass"))
        self.menuOutils.setTitle(_translate("MainWindow", "Outils"))
        self.menuChanger_de_langue.setTitle(_translate("MainWindow", "Changer de langue"))
        self.menuAide.setTitle(_translate("MainWindow", "Aide"))
        self.actionFermer.setText(_translate("MainWindow", "Fermer"))
        self.actionFermer.setShortcut(_translate("MainWindow", "Alt+F4"))
        self.actionFran_ais.setText(_translate("MainWindow", "Français"))
        self.actionAnglais.setText(_translate("MainWindow", "Anglais"))
        self.actionObtenir_de_l_aide.setText(_translate("MainWindow", "Obtenir de l\'aide"))
        self.actionObtenir_de_l_aide.setShortcut(_translate("MainWindow", "F1"))
        self.actionA_propos_de_MindPass.setText(_translate("MainWindow", "A propos de MindPass"))
        self.actionPr_f_rences.setText(_translate("MainWindow", "Préférences"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

