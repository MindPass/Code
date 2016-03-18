import sys

sys.path.append('../fenetres/')

from fenetreAccueil import Ui_fenetreAccueil


# Classe qui s'applique à la premiere fenetre MainWindow

class ClasseAccueil(Ui_fenetreAccueil):
    def __init__(self, fenetre):
        self.setupUi(fenetre)
        self.pushButton.setAutoDefault(True)  # Taper sur entrée revient à cliquer
        self.pushButton.clicked.connect(self.check_login)

    def check_login(self):
        # identifiants = [self.lineEdit_id.displayText(), self.lineEdit_mdp.displayText()]
        identifiants = ["mindpasstest", "Verv00rt"]
        condition = identifiants == ["mindpasstest", "Verv00rt"]

        if condition:
            self.fenetre_suivante()

    def fenetre_suivante(self):
        pass
        # fonction définissant les modalités du passage à une autre fenêtre
        # qui va être overwrite dans class Accueil()
