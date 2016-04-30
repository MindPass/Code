# -*- coding: utf-8 -*-
import sys
import time
from PyQt5 import QtWidgets
from classeAccueil import ClasseAccueil
from classeProgression import ClasseProgression
from classeGestion import ClasseGestion


class Accueil(ClasseAccueil):
    def __init__(self, fenetre):
        super().__init__(fenetre)
        fenetre.show()

    def fenetre_suivante(self):
        print(self.identifiants)
        print("Passage à la fenêtre de progression")
        premiere_fenetre.hide()
        deuxieme_fenetre.show()
        objet_progression.lancement(self.identifiants)


class Progression(ClasseProgression):
    def __init__(self, fenetre):
        super().__init__(fenetre)

    def fenetre_suivante(self):
        print("Passage à la fenêtre de gestion !")
        time.sleep(1.5)
        deuxieme_fenetre.hide()
        troisieme_fenetre.showMaximized()
        objet_gestion.lancement()


class Gestion(ClasseGestion):
    def __init__(self, fenetre):
        super().__init__(fenetre)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    premiere_fenetre = QtWidgets.QMainWindow()
    deuxieme_fenetre = QtWidgets.QMainWindow()
    troisieme_fenetre = QtWidgets.QMainWindow()

    objet_accueil = Accueil(premiere_fenetre)
    objet_progression = Progression(deuxieme_fenetre)
    objet_gestion = Gestion(troisieme_fenetre)

    sys.exit(app.exec_())
