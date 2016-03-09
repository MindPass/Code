# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from fenetreAccueil import Ui_fenetreAccueil
from fenetreProgression import Ui_fenetreProgression
from fenetreGestion import Ui_fenetreGestion

sys.path.append('../../Traitements_mail/objets/')
from librairie import *


class FenetreAccueil(Ui_fenetreAccueil):
    def __init__(self, fenetre):
        self.setupUi(fenetre)
        fenetre.show()

        self.pushButton.setAutoDefault(True)  # Taper sur entrée revient à cliquer
        self.pushButton.clicked.connect(self.check_login)

    def check_login(self):
        identifiants = [self.lineEdit_id.displayText(), self.lineEdit_mdp.displayText()]
        condition = identifiants == ["mindpasstest", "Verv00rt"]

        if condition:
            self.fenetre_suivante(identifiants)

    def fenetre_suivante(self, identifiants):
        print("Passage à la fenêtre de progression")
        premiere_fenetre.hide()
        deuxieme_fenetre.show()
        fenetre_progression.connexion(identifiants)


class FenetreProgression(Ui_fenetreProgression):
    def __init__(self, fenetre):
        self.setupUi(fenetre)

    def connexion(self, identifiants):
        # self.afficher_messages()  # faire défiler des images

        # et se connecter en même temps
        user_email = identifiants[0] + "@laposte.net"
        mdp = identifiants[1]
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
                    print("ID erreur:" + str(id_email) + ": "+ str(e))
                    fichier_erreurs.write(str(id_email) + "-Erreur : %s \n" % e)
            count += 1
            ratio = int(count / len(liste_externe_id) * 100)
            self.progressBar.setValue(ratio)
            QtWidgets.QApplication.processEvents()

        table.save()
        fichier_erreurs.close()
        table.close()
        tableExterne.close()

        self.fenetre_suivante()

    def fenetre_suivante(self):
        print("Passage à la fenêtre de gestion !")
        deuxieme_fenetre.hide()
        troisieme_fenetre.show()
        fenetre_gestion.afficher()


class FenetreGestion(Ui_fenetreGestion):
    def __init__(self, fenetre):
        self.setupUi(fenetre)

    def afficher(self):
        print("On gère les résultats maintenant.")


#
# Lancement de l'application
#

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    premiere_fenetre = QtWidgets.QMainWindow()
    fenetre_accueil = FenetreAccueil(premiere_fenetre)

    deuxieme_fenetre = QtWidgets.QMainWindow()
    fenetre_progression = FenetreProgression(deuxieme_fenetre)

    troisieme_fenetre = QtWidgets.QMainWindow()
    fenetre_gestion = FenetreGestion(troisieme_fenetre)

    sys.exit(app.exec_())
