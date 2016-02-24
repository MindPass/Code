# -*- coding: utf-8 -*-

import sys
sys.path.append('../../Traitements_mail/objets/')
from librairie import *

from PyQt5 import QtWidgets
from pageAccueil import Ui_MainWindow
from progressBar import Ui_Form


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow, Ui_Form):
    def __init__(self, fenetre):
        """

        Args:
            fenetre: La classe de la fenêtre voulue

        Returns: None

        """
        QtWidgets.QMainWindow.__init__(self)  # création de la fenêtre principale
        fenetre.setupUi(self, self)
        self.show()

        if fenetre == Ui_MainWindow:
            self.actionFermer.triggered.connect(self.close)
            self.pushButton.setAutoDefault(True)  # Taper sur entrée revient à cliquer
            self.pushButton.clicked.connect(self.check_login)
            with open("pageAccueil.css","r") as feuilleDeStyle:
                self.setStyleSheet(feuilleDeStyle.read())

        elif fenetre == Ui_Form:
            user_email = self.login + "@laposte.net"
            mdp = self.login_mdp
            # à garder pendant le développement

            l = user_email.split('@')
            l[1] = l[1].split('.')[0]
            nom_table = l[0] + '_' + l[1]  # vaut 'pseudo_laposte'

            table = Table(nom_table)
            tableExterne = TableExterne('imap.laposte.net', user_email, mdp)
            fichier_erreurs = open('fichier_erreurs.txt', 'a')

            liste_externe_id = tableExterne.liste_id()
            liste_interne_id = table.liste_id()

            count = 0
            for id_email in liste_externe_id:
                print(id_email)
                if id_email not in liste_interne_id:
                    try:
                        table.add_mail(tableExterne.email_as_list(id_email))
                    except Exception as e:
                        print("Il y a eu une erreur pour l'id suivant:" + str(id_email))
                        fichier_erreurs.write(str(id_email) + "-Erreur : %s \n" % e)
                count += 1
                ratio = int(count/len(liste_externe_id)*100)
                self.progressBar.setValue(ratio)
                QtWidgets.QApplication.processEvents()


            table.save()
            fichier_erreurs.close()
            table.close()
            tableExterne.close()



    def check_login(self):
        """
        Verifier l'existence des identifiants.
        Returns: None
        """
        print(self.lineEdit_id.displayText())
        condition = self.lineEdit_id.displayText() == 'mindpasstest' and self.lineEdit_mdp.displayText() == 'Verv00rt'
        self.login = self.lineEdit_id.displayText()
        self.login_mdp = self.lineEdit_mdp.displayText()

        if condition:  # on cache la page d'acceuil et on passe à la progressBar
            self.hide()
            MainWindow.__init__(self, Ui_Form)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    accueilWindow = MainWindow(Ui_MainWindow)
    sys.exit(app.exec_())
