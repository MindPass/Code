import sys 
sys.path.append('../fenetres/')
sys.path.append('../../../Traitement_mails/objets/')

from PyQt5 import QtWidgets
from fenetreProgression import Ui_fenetreProgression
from classeGestion import ClasseGestion
from librairie import *
import time
bdd = "../../../Traitement_mails/bdd.sq3"


class ClasseProgression(Ui_fenetreProgression):
    def __init__(self, fenetre):
        self.setupUi(fenetre)

    def lancement(self, identifiants):
        # self.afficher_messages()  # faire défiler des images

        # et se connecter en même temps
        user_email = identifiants[0] + "@laposte.net"
        mdp = identifiants[1]
        # à garder pendant le développement

        l = user_email.split('@')
        l[1] = l[1].split('.')[0]
        nom_table = l[0] + '_' + l[1]  # vaut 'pseudo_laposte'

        table = Table(bdd, nom_table)
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
                    print("ID erreur:" + str(id_email) + ": " + str(e))
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
        pass


