# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from classeAccueil import ClasseAccueil
from classeProgression import ClasseProgression
from classeGestion import ClasseGestion


class MindPassApp(object):
    def __init__(self):
        self.fenetre = QtWidgets.QMainWindow()
        ClasseAccueil.__init__(self, self.fenetre)
        self.fenetre.show()

    def fenetre_suivante(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    mindpass_app = MindPassApp()

    sys.exit(app.exec_())
