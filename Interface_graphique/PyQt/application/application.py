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
        ClasseAccueil.fenetre_suivante(self)
        fenetreAccueil.hide()
        fenetreProgression.show()
        objet_progression.lancement(self.serv, self.user_email, self.mdp, self.nom_table)

    def fenetre_suivante_hors_connexion(self):
        ClasseAccueil.fenetre_suivante_hors_connexion(self)
        fenetreAccueil.hide()
        fenetreGestion.show()
        objet_gestion.lancement(self.nom_table)


class Progression(ClasseProgression):
    def __init__(self, fenetre):
        super().__init__(fenetre)

    def fenetre_suivante(self):
        ClasseProgression.fenetre_suivante(self)
        fenetreProgression.hide()
        fenetreGestion.show()
        objet_gestion.lancement(self.nom_table)


class Gestion(ClasseGestion):
    def __init__(self, fenetre):
        super().__init__(fenetre)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    fenetreAccueil = QtWidgets.QMainWindow()
    fenetreProgression = QtWidgets.QMainWindow()
    fenetreGestion = QtWidgets.QMainWindow()

    objet_accueil = Accueil(fenetreAccueil)
    objet_progression = Progression(fenetreProgression)
    objet_gestion = Gestion(fenetreGestion)

    sys.exit(app.exec_())
