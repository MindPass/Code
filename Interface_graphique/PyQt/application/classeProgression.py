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
        user_email = identifiants[0] #+ "@laposte.net"
        mdp = identifiants[1]
        # à garder pendant le développement

        l = user_email.split('@')
        partie2 = l[1].split('.')[0]
        nom_table = l[0] + '_' + partie2  # vaut 'pseudo_laposte'

        table = Table(bdd, nom_table) #La table avec le bon nom n'existe pas forcément!

        if l[1]=='free.fr':
            serv='imap.free.fr'
            print(serv)
        elif l[1]=='laposte.net':
            serv='imap.laposte.net'
            print(serv)
        elif l[1]=='neuf.fr':
            serv='imap.sfr.fr'
            print(serv)
        elif l[1]=='bbox.fr':
            serv='imap4.bbox.fr'
            print(serv)
        elif l[1]=='numericable.fr':
            serv='imap.numericable.fr'
            print(serv)
        elif l[1]=='orange.fr':
            serv='imap.orange.fr'
            print(serv)
        elif l[1]=='sfr.fr':
            serv='imap.sfr.fr'
            print(serv)
        elif l[1]=='aol.fr':
            serv='imap.aol.com'
            print(serv)
        elif l[1]=='gmail.com':
            serv='imap.gmail.com'
            print(serv)
        elif l[1]=='outlook.com':
            serv='imap-mail.outlook.com'
            print(serv)
        elif l[1]=='hotmail.com':
            serv='imap-mail.outlook.com'
            print(serv)
        elif l[1]=='hotmail.fr':
            serv='imap-mail.outlook.com'
            print(serv)
        elif l[1]=='live.fr':
            serv='imap-mail.outlook.com'
            print(serv)
        elif l[1]=='yahoo.com':
            serv='imap.mail.yahoo.com'
            print(serv)        
        
        tableExterne = TableExterne(serv, user_email, mdp)
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


