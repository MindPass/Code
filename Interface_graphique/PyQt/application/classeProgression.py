import sys 
import os
sys.path.append('../fenetres/')
sys.path.append('../../../Traitement_mails/objets/')

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



from PyQt5 import QtWidgets
from PyQt5 import QtGui
from fenetreProgression import Ui_fenetreProgression
from classeGestion import ClasseGestion
from librairie import *
import time
from recon_id import *
bdd = "../../../Traitement_mails/bdd.sq3"


class ClasseProgression(Ui_fenetreProgression):
    def __init__(self, fenetre):
        self.setupUi(fenetre)
        self.bouton_page_suiv.hide()
        self.compteurImage = 0

        # evenements
        self.pushButton_image_prec.clicked.connect(self.image_precedente)
        self.pushButton_image_suiv.clicked.connect(self.image_suivante)


    def lancement(self, serv, user_email, mdp, nom_table):

        self.nom_table = nom_table

        table = Table(bdd, nom_table) #La table avec le bon nom n'existe pas forcément!
        tableExterne = TableExterne(serv, user_email, mdp)
        tableExterne.connexionMail()

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

            if(count % 3 ==0):
                ratio = int(count / len(liste_externe_id) * 100)
                self.progressBar.setValue(ratio)
                QtWidgets.QApplication.processEvents()
                if(count % 10 ==0):
                    table.save()

        table.save()
        fichier_erreurs.close()
        table.close()
        tableExterne.close()

        
        creation_tables(nom_table, user_email)
        
        # si suivant est cliqué, on passe à la fenetre suivante
        self.bouton_page_suiv.show()
        self.bouton_page_suiv.clicked.connect(self.fenetre_suivante)

    def image_suivante(self):
        listeImages = os.listdir('../ressources/images/')
        self.compteurImage = (self.compteurImage+1) % len(listeImages)
        self.imageDefil.setPixmap(QtGui.QPixmap("../ressources/images/"+listeImages[self.compteurImage]))

    def image_precedente(self):
        listeImages = os.listdir('../ressources/images/')
        self.compteurImage = (self.compteurImage-1) % len(listeImages)
        self.imageDefil.setPixmap(QtGui.QPixmap("../ressources/images/"+listeImages[self.compteurImage]))

    def fenetre_suivante(self):
        print("fenêtre suivante")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    fenetreProgression = QtWidgets.QMainWindow()

    classProgression = ClasseProgression(fenetreProgression)

    fenetreProgression.show()
    sys.exit(app.exec_())