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
        troisieme_fenetre.show()
        objet_gestion.lancement()


class Gestion(ClasseGestion):
    def __init__(self, fenetre):
        super().__init__(fenetre)

    def afficher(self):
        print("On gère les résultats maintenant.")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    premiere_fenetre = QtWidgets.QMainWindow()
    objet_accueil = Accueil(premiere_fenetre)

    deuxieme_fenetre = QtWidgets.QMainWindow()
    objet_progression = Progression(deuxieme_fenetre)

    troisieme_fenetre = QtWidgets.QMainWindow()
    objet_gestion = Gestion(troisieme_fenetre)

    sys.exit(app.exec_())