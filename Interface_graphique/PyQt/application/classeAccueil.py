
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

from PyQt5 import QtWidgets
from PyQt5 import QtCore
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


    def check_login(self):
        identifiants = [self.lineEdit_id.displayText(), self.lineEdit_mdp.text()]
        #identifiants = ["mindpasstest", "Verv00rt"]
        #condition = identifiants == ["mindpasstest", "Verv00rt"]

        condition = identifiants[0] != "" and identifiants[1] != ""
        # Vérifier que l'identifiant a la bonne forme
        # et qu'une connexion s'établit

        if condition and not self.horsConnexion.isChecked():
            self.identifiants = identifiants
            self.fenetre_suivante()
        elif condition and self.horsConnexion.isChecked():
            self.identifiants = identifiants
            self.fenetre_suivante_hors_connexion()

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
