import sys

sys.path.append('../fenetres/')

from PyQt5 import QtWidgets
from fenetreAccueil import Ui_fenetreAccueil
from classeProgression import ClasseProgression


# Classe qui s'applique à la premiere fenetre MainWindow

class ClasseAccueil(Ui_fenetreAccueil):
    def __init__(self, fenetre1, fenetre2):
        self.setupUi(fenetre1)
        fenetre1.show()

        self.pushButton.setAutoDefault(True)  # Taper sur entrée revient à cliquer
        self.pushButton.clicked.connect(self.check_login)

    def check_login(self, fenetre1, fenetre2):
        # identifiants = [self.lineEdit_id.displayText(), self.lineEdit_mdp.displayText()]
        identifiants = ["mindpasstest", "Verv00rt"]
        condition = identifiants == ["mindpasstest", "Verv00rt"]

        if condition:
            self.fenetre_suivante(identifiants, fenetre1, fenetre2)

    def fenetre_suivante(self, identifiants, fenetre1, fenetre2):
        print(identifiants)
        fenetre1.hide()
        fenetre2.show()
        # deuxieme_fenetre.show()
