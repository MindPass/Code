# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets
from pageAccueil import Ui_MainWindow
from progressBar import Ui_Form


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow, Ui_Form):
    def __init__(self, fenetre):
        """

        Args:
            fenetre: La classe de la fenêtre voulue

        Returns: None

        """
        QtWidgets.QMainWindow.__init__(self)  # création de la fenêtre principale
        fenetre.setupUi(self, self)

        if fenetre == Ui_MainWindow:
            self.actionFermer.triggered.connect(self.close)
            self.pushButton.setAutoDefault(True)  # Taper sur entrée revient à cliquer
            self.pushButton.clicked.connect(self.check_login)
        elif fenetre == Ui_Form:
            pass

    def check_login(self):
        """

        Verifier l'existence des identifiants.
        Returns: None

        """
        print(self.lineEdit_id.displayText())

        condition = self.lineEdit_id.displayText() == 'a' and self.lineEdit_mdp.displayText() == 'b'

        if condition:  # on cache la page d'acceuil et on passe à la progressBar
            self.hide()
            MainWindow.__init__(self, Ui_Form)
            self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    accueilWindow = MainWindow(Ui_MainWindow)
    accueilWindow.show()
    sys.exit(app.exec_())
