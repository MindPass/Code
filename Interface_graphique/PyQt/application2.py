# -*- coding: utf-8 -*-

import sys

sys.path.append('../../Traitements_mail/objets/')
from librairie import *

from PyQt5 import QtWidgets
from fenetreAccueil import Ui_fenetreAccueil
from fenetreProgression import Ui_fenetreProgression
from fenetreGestion import Ui_fenetreGestion


class MainWindow(object):
    def __init__(self, fenetre):

        Ui_fenetreAccueil.__init__(self)
        self.setupUi(self, fenetre)
        self.show()


        if fenetre == Ui_fenetreAccueil:
            self.actionFermer.triggered.connect(self.close)
            self.pushButton.setAutoDefault(True)  # Taper sur entrée revient à cliquer
            self.pushButton.clicked.connect(self.check_login)


    def check_login(self):


        condition = 1

        self.login = self.lineEdit_id.displayText()
        self.login_mdp = self.lineEdit_mdp.displayText()

        if condition:  # on cache la page d'acceuil et on passe à la progressBar
            self.deleteLater()

            print('objet supprimé')

            self = MainWindow.__init__(self, Ui_fenetreProgression)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    fenetreAccueil = QtWidgets.QMainWindow()
    ui = MainWindow(fenetreAccueil)

    sys.exit(app.exec_())


