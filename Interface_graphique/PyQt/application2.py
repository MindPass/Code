# -*- coding: utf-8 -*-

import sys

sys.path.append('../../Traitements_mail/objets/')
from librairie import *

from PyQt5 import QtWidgets
from fenetreAccueil import Ui_fenetreAccueil
from fenetreProgression import Ui_fenetreProgression
from fenetreGestion import Ui_fenetreGestion


class fenetreAccueil(Ui_fenetreAccueil):
    def __init__(self, fenetre):

        self.setupUi(fenetre)
        fenetre.show()


        self.pushButton.setAutoDefault(True)  # Taper sur entrée revient à cliquer
        self.pushButton.clicked.connect(fenetre.close)


class fenetreProgression(Ui_fenetreProgression):
    def __init__(self, fenetre):

        self.setupUi(fenetre)

        fenetre.show()
        fenetre.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    premiereFenetre = QtWidgets.QMainWindow()
    fenetreAccueil(premiereFenetre)


    deuxiemeFenetre = QtWidgets.QMainWindow()
    fenetreProgression(deuxiemeFenetre)


    sys.exit(app.exec_())


