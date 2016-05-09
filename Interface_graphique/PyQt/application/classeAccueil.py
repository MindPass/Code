
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

import sys

sys.path.append('../fenetres/')
sys.path.append('../../../Traitement_mails/objets/')
from functools import partial
from PyQt5 import QtWidgets
from PyQt5 import QtCore
import re
from librairie import *
from fenetreAccueil import Ui_fenetreAccueil

def print_(arg):
    """
    Args:
        arg: la valeur à afficher

    Returns: la valeur à afficher ainsi qu'une série de '-', afin d'espacer l'affichage

    """
    print(arg)
    print("-------------------------------------")
# Classe qui s'applique à la premiere fenetre MainWindow

class ClasseAccueil(Ui_fenetreAccueil):
    def __init__(self, fenetre):
        self.setupUi(fenetre)
        # modifications supplémentaires
        self.lineEdit_mdp.setEchoMode(2) 
        """Le mot de passe est masqué ->utiliser self.lineEdit.text()
        pour récupérer le contenu.
        """
        # event
        self.lineEdit_mdp.returnPressed.connect(self.check_login)  # Taper sur entrée revient à cliquer
        self.pushButton.clicked.connect(self.check_login)

        # Quand le texte change
        self.lineEdit_id.textEdited.connect(self.check_format_mail)
        self.lineEdit_mdp.textEdited.connect(partial(self.setColor, self.lineEdit_mdp, "white"))


    def check_login(self):
        self.label_erreur.setText("")
        identifiants = [self.lineEdit_id.displayText(), self.lineEdit_mdp.text()]

        formatMailOk = self.check_format_mail()

        if formatMailOk:
            user_email = identifiants[0] 
            mdp = identifiants[1]

            l = user_email.split('@')

            l2 = l[1].split(".")
            
            nom_table = l[0]
            for element in l2:
                nom_table += "_"+element

            messagerie = l2[-2] + "." + l2[-1]

            dic = { "free.fr":          "imap.free.fr",
                    "laposte.net":      "imap.laposte.net",
                    "neuf.fr":          "imap.sfr.fr",
                    "bbox.fr":          "imap4.bbox.fr",
                    "numericable.fr":   "imap.numericable.fr",
                    "orange.fr":        "imap.orange.fr",
                    "sfr.fr":           "imap.sfr.fr",
                    "aol.fr":           "imap.aol.com",
                    "gmail.com":        "imap.gmail.com",
                    "outlook.com":      "imap-mail.outlook.com",
                    "hotmail.com":      "imap-mail.outlook.com",
                    "hotmail.fr":       "imap-mail.outlook.com",
                    "live.fr":          "imap-mail.outlook.com",
                    "yahoo.com":        "imap.mail.yahoo.com",
                    "me.com":           "imap.mail.me.com",
                    "icloud.com":       "imap.mail.me.com",
                    }


            messagerieCompatible = False

            for element in dic:
                if(messagerie == element):
                    print(dic[element])
                    serv = dic[element]
                    messagerieCompatible =True

            if(not messagerieCompatible):
                self.label_erreur.setText("La messagerie "+messagerie+" n'est pas prise en charge.")
            else:
                horsConnexion = self.horsConnexion.isChecked() 

                if(horsConnexion):
                    # vérifier qu'il existe un couple adresse_mail/mdp_hash qui correspondent
                    # dans CONNEXIONS
                    """
                    self.serv = serv
                    self.user_email = user_email
                    self.mdp = mdp
                    self.nom_table = nom_table
                    self.fenetre_suivante()
                    """
                    
                    pass
                else:
                    if(serv == "imap.gmail.com"):
                        print("Adresse gmail")
                        # A continuer
                    else:
                        tableE = TableExterne(serv, user_email, mdp)

                        if(tableE.test_connexion(serv, user_email, mdp)):

                            print("connexion faite")
                            self.serv = serv
                            self.user_email = user_email
                            self.mdp = mdp
                            self.nom_table = nom_table
                            self.fenetre_suivante()

                            """

                            if(TableExterne.test_connexion())

                                table = Table(bdd, nom_table) #La table avec le bon nom n'existe pas forcément!
                            # Vérifier que l'identifiant a la bonne forme
                            # et qu'une connexion s'établit

                            if formatMailOk and not self.horsConnexion.isChecked() and connexion_existe:
                                self.identifiants = identifiants
                                self.fenetre_suivante()
                            elif formatMailOk and self.horsConnexion.isChecked():
                                self.identifiants = identifiants
                                self.fenetre_suivante_hors_connexion()

                            """
                        else:
                            self.label_erreur.setText("Problème de connexion ou d'identifiants.")


    
    def check_format_mail(self):
        result = re.fullmatch("^[a-z0-9._-]+@[a-z0-9._-]{2,}\.[a-z]{2,4}$", self.lineEdit_id.displayText())
        if(not result):
            self.setColor(self.lineEdit_id, "red")
            return False
        else:
            self.setColor(self.lineEdit_id, "white")
            return True


    def setColor(self, lineEdit, couleur="white"):
        lineEdit.setStyleSheet("QLineEdit { border: 1px solid " + couleur + "; }")


    def fenetre_suivante(self):
        pass
        # fonction définissant les modalités du passage à une autre fenêtre
        # qui va être overwrite dans class Accueil()

    def fenetre_suivante_hors_connexion(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    fenetreAccueil = QtWidgets.QMainWindow()

    classAccueil = ClasseAccueil(fenetreAccueil)

    fenetreAccueil.show()
    sys.exit(app.exec_())
