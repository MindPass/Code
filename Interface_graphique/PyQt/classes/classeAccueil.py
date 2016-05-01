import sys

sys.path.append('../fenetres/')

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
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
        self.setupMenu()
        self.lineEdit_mdp.setEchoMode(2) 
        """Le mot de passe est masqué ->utiliser self.lineEdit.text()
        pour récupérer le contenu.
        """
        # event
        self.lineEdit_mdp.returnPressed.connect(self.check_login)  # Taper sur entrée revient à cliquer
        self.pushButton.clicked.connect(self.check_login)

    def setupMenu(self):
        self.aide_url = "https://github.com/MindPass/Code/wiki/Aide"
        self.apropos_url  ="https://github.com/MindPass/Code"
        self.actionObtenir_de_l_aide.triggered.connect(self.ouvrirAide)
        self.actionA_propos_de_MindPass.triggered.connect(self.ouvrirApropos)

        # Affichage
        self.actionMode_deux_lettres.triggered.connect(self.deuxLettres)

    def deuxLettres(self):
        pass

    def touteLettres(self):
        pass

    def ouvrirAide(self):
        self.openURL(self.aide_url)

    def ouvrirApropos(self):
        self.openURL(self.apropos_url)

    def openURL(self, given_url):
        url = QtCore.QUrl(given_url)
        if not QtGui.QDesktopServices.openUrl(url):
            QtGui.QMessageBox.warning(self, 'Open Url', 'Could not open url')


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
