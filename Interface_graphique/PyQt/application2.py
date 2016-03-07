# -*- coding: utf-8 -*-

import sys

sys.path.append('../../Traitements_mail/objets/')
from librairie import *

from PyQt5 import QtWidgets
from fenetreAccueil import Ui_fenetreAccueil
from fenetreProgression import Ui_fenetreProgression


class fenetreAccueil(Ui_fenetreAccueil):
    def __init__(self, fenetre):

        self.setupUi(fenetre)
        fenetre.show()

        self.pushButton.clicked.connect(self.fenetre_suivante)
        self.pushButton.clicked.connect(self.afficher)

    def afficher(self):
        print("salut")

    def fenetre_suivante(self):
        print("va te faire foutre")




class fenetreProgression(Ui_fenetreProgression):
    def __init__(self, fenetre):

        self.setupUi(fenetre)
        fenetre.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    premiereFenetre = QtWidgets.QMainWindow()
    fenetreAccueil(premiereFenetre)

    sys.exit(app.exec_())


