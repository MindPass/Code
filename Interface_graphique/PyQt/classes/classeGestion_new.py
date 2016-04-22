import sqlite3
import sys

sys.path.append('../fenetres/')
from functools import partial
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from fenetreGestion import Ui_fenetreGestion
from requetes import *

bdd = "../../../Traitement_mails/bdd.sq3"

def print_(arg):
    """
    Args:
        arg: la valeur à afficher

    Returns: la valeur à afficher ainsi qu'une série de '-', afin d'espacer l'affichage

    """
    print(arg)
    print("-------------------------------------")

class LineEditWithFocusOut(QtWidgets.QLineEdit):
    """docstring for LineEditWithFocusOut"""

    def focusOutEvent(self, arg):
        QtWidgets.QLineEdit.focusOutEvent(self, arg)
        # self.id contient l'id de la LigneEdit, ajouté dans afficher_ligne_site()

        bdd_update("sites_reconnus", ("identifiant",), "rowid", (self.text(), self.id +1))
        
        if self.text() == "":
            self.setPlaceholderText("Ajouter un pseudo")


class Ligne(object):
	"""docstring for ligneCategorie"""

	def __init__(self, position, nom, sites): 
		self.position = position
		self.nom = nom
		self.sites = sites

		self.ligne = QtWidgets.QHBoxLayout()
		self.label = QtWidgets.QLabel()
		self.pushButton = QtWidgets.QPushButton()

		self.ligne.addWidget(self.label)
		self.ligne.addWidget(self.pushButton)


class Categorie(Ligne):
	"""docstring for Categorie"""

	def __init__(self, position, nom, sites):
		super().__init__(position, nom, sites)
		self.label.setObjectName("label_cat")
		self.label.setText(nom)
		self.pushButton.setObjectName("pushButton_cat")
		self.pushButton.setText('X_cat')

class Password(Ligne):
	"""docstring for Password"""

	def __init__(self, position, nom, sites):
		super().__init__(position, nom, sites)
		self.label.setObjectName("label_pwd")
		self.label.setText(nom)
		self.pushButton.setObjectName("pushButton_pwd")
		self.pushButton.setText('X_pwd')
		

class ClasseGestion(Ui_fenetreGestion):
	def __init__(self, fenetre):
		self.setupUi(fenetre)
		self.ajouter_cat.setPlaceholderText("Ajouter une catégorie")
		self.ajouter_pwd.setPlaceholderText("Ajouter un mot de passe")

		self.cats = []
		self.pwds = []

		#lancement(self):
		self.afficher_categories()
		self.afficher_pwds()

	def afficher_categories(self):
		conn = sqlite3.connect(bdd)
		cur = conn.cursor()
		cur.execute('SELECT nom_categorie FROM categories')
		tab = cur.fetchall()

		if tab:
		    for k in range(len(tab)):
		        self.ajouter_ligne_categorie(k, tab[k][0])

		conn.commit()
		cur.close() 
		conn.close()

	def ajouter_ligne_categorie(self, y, nom_categorie):
		self.cats.append(Categorie(y, nom_categorie,[]))
		self.verticalLayout_3.addLayout(self.cats[y].ligne)
		# On garde l'alignement haut
		self.verticalLayout_3.setAlignment(QtCore.Qt.AlignTop) 


	def afficher_pwds(self):
		conn = sqlite3.connect(bdd)
		cur = conn.cursor()
		cur.execute('SELECT mdp FROM mdps')
		tab = cur.fetchall()

		if tab:
		    for k in range(len(tab)):
		        self.ajouter_ligne_pwd(k, tab[k][0])

		conn.commit()
		cur.close()
		conn.close()

	def ajouter_ligne_pwd(self, y, nom_pwd):
		self.pwds.append(Password(y, nom_pwd, []))
		self.verticalLayout_2.addLayout(self.pwds[y].ligne)

		# On garde l'alignement haut
		self.verticalLayout_2.setAlignment(QtCore.Qt.AlignTop)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    fenetreGestion = QtWidgets.QMainWindow()

    classGestion = ClasseGestion(fenetreGestion)

    fenetreGestion.show()
    sys.exit(app.exec_())
