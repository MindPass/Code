# -*- coding: utf-8 -*-

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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    premiere_fenetre = QtWidgets.QMainWindow()
    deuxieme_fenetre = QtWidgets.QMainWindow()
    troisieme_fenetre = QtWidgets.QMainWindow()

    objet_accueil = Accueil(premiere_fenetre)
    objet_progression = Progression(deuxieme_fenetre)
    objet_gestion = Gestion(troisieme_fenetre)

    sys.exit(app.exec_())
