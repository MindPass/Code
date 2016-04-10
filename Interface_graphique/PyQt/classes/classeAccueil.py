import sys

sys.path.append('../fenetres/')

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from fenetreAccueil import Ui_fenetreAccueil

def print_(arg):
    """
    Args:
        arg: la valeur à afficher

    Returns: la valeur à afficher ainsi qu'une série de '-', afin d'espacer l'affichage

    """
    print(arg)
    print("-------------------------------------")
# Classe qui s'applique à la premiere fenetre MainWindow

class ClasseAccueil(Ui_fenetreAccueil):
    def __init__(self, fenetre):
        self.setupUi(fenetre)
        # modifications supplémentaires
        self.lineEdit_mdp.setEchoMode(2) 
        """Le mot de passe est masqué ->utiliser self.lineEdit.text()
        pour récupérer le contenu.
        """
        # event
        self.pushButton.setAutoDefault(True)  # Taper sur entrée revient à cliquer
        self.pushButton.clicked.connect(self.check_login)


    def check_login(self):
        # identifiants = [self.lineEdit_id.displayText(), self.lineEdit_mdp.text()]
        identifiants = ["mindpasstest", "Verv00rt"]
        condition = identifiants == ["mindpasstest", "Verv00rt"]

        if condition:
            self.identifiants = identifiants
            self.fenetre_suivante()

    def fenetre_suivante(self):
        pass
        # fonction définissant les modalités du passage à une autre fenêtre
        # qui va être overwrite dans class Accueil()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    fenetreAccueil = QtWidgets.QMainWindow()

    classAccueil = ClasseAccueil(fenetreAccueil)

    fenetreAccueil.show()
    sys.exit(app.exec_())
