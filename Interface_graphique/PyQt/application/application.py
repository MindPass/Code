# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from classeAccueil import ClasseAccueil
from classeProgression import ClasseProgression
from classeGestion import ClasseGestion



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    premiere_fenetre = QtWidgets.QMainWindow()
    deuxieme_fenetre = QtWidgets.QMainWindow()
    troisieme_fenetre = QtWidgets.QMainWindow()

    fenetre_accueil = ClasseAccueil(premiere_fenetre, deuxieme_fenetre)
    fenetre_progression = ClasseProgression(deuxieme_fenetre, troisieme_fenetre)
    fenetre_gestion = ClasseGestion(troisieme_fenetre)

    sys.exit(app.exec_())
