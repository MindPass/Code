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
    """docstring for LineEditWithFocusOut
    Ré-implémentation de QLineEdit(), en modifiant son comportement
    lors d'un focusOut event. Ici, on update l'identifiant de la 
    table sites_reconnus.
    """

    def focusOutEvent(self, arg):
        QtWidgets.QLineEdit.focusOutEvent(self, arg)
        # self.id contient l'id de la LigneEdit, ajouté dans afficher_ligne_site()

        requete= "UPDATE sites_reconnus SET identifiant =? WHERE rowid=?"
        bdd_update(requete, (self.text(), self.id +1))

        if self.text() == "":
            self.setPlaceholderText("Ajouter un pseudo")



class LigneSite(object):
	"""docstring for LigneSite"""
	def __init__(self, y, site_web, identifiant, mdp, categorie, objet):
		self.position = y
		self.objet = objet 

		self.ligne = QtWidgets.QHBoxLayout()
		self.site_web =QtWidgets.QLabel()
		self.site_web.setAlignment(QtCore.Qt.AlignCenter)
		self.site_web.setObjectName("site_web")
		self.site_web.setText(site_web)
		self.ligne.addWidget(self.site_web)

		self.identifiant = LineEditWithFocusOut()
		self.identifiant.setAlignment(QtCore.Qt.AlignCenter)
		self.identifiant.setObjectName('identifiant')
		self.identifiant.id = y 

		if identifiant is None or identifiant == "":
		    self.identifiant.setPlaceholderText("Ajouter un pseudo")
		else:
		    self.identifiant.setText(identifiant)

		self.ligne.addWidget(self.identifiant)

		self.mdp = QtWidgets.QComboBox()
		self.mdp.setObjectName("mdp")
		self.afficher_combo_pwd() # affichage des éléments de la combobox en fonction de la bdd
		self.ligne.addWidget(self.mdp)
		self.categorie = QtWidgets.QComboBox()
		self.categorie.setObjectName("categorie")
		self.afficher_combo_cat()  # affichage des éléments de la combobox en fonction de la bdd
		self.ligne.addWidget(self.categorie)
		self.ligne.setStretch(0, 2)
		self.ligne.setStretch(1, 2)
		self.ligne.setStretch(2, 2)
		self.ligne.setStretch(3, 2)

		# Changement de pwd/catégories
		self.categorie.currentIndexChanged.connect(self.changement_cat)
		self.mdp.currentIndexChanged.connect(self.changement_pwd)
	
	def changement_cat(self):
		print("changement")
		requete = "UPDATE sites_reconnus SET categorie=? WHERE rowid=?"
		bdd_update(requete, (self.categorie.currentText(), self.position + 1))
		print("Catégorie changée en"+ str(self.categorie.currentText()))	

	def changement_pwd(self):
		requete = "UPDATE sites_reconnus SET mdp=? WHERE rowid=?"
		bdd_update(requete, (self.mdp.currentText(), self.position + 1))
		print("Pwd changée en"+ str(self.mdp.currentText()))

	def afficher_combo_pwd(self):
		y= self.position
		requete= 'SELECT mdp FROM mdps'
		tab = bdd_select(requete)
		result = []
		for k in range(len(tab)):
		    result.append(tab[k][0])
		requete= 'SELECT mdp FROM sites_reconnus WHERE rowid=?'
		pwd_ligne = bdd_select(requete, (y + 1,))[0][0]

		if pwd_ligne and (pwd_ligne in result):
		    self.mdp.addItem(pwd_ligne)
		    for nom_pwd in result:
		        if nom_pwd != pwd_ligne:
		            self.mdp.addItem(nom_pwd)
		    self.mdp.addItem("")
		else:
		    self.mdp.addItem("")
		    for nom_pwd in result:
		        self.mdp.addItem(nom_pwd)

	def afficher_combo_cat(self):
		y = self.position
		requete = 'SELECT nom_categorie FROM categories'
		tab = bdd_select(requete)
		result = []
		for k in range(len(tab)):
		    result.append(tab[k][0])
		requete='SELECT categorie FROM sites_reconnus WHERE rowid=?'
		cat_ligne = bdd_select(requete, (y + 1,))[0][0]

		if cat_ligne and (cat_ligne in result):
		    self.categorie.addItem(cat_ligne)
		    for nom_categorie in result:
		        if nom_categorie != cat_ligne:
		            self.categorie.addItem(nom_categorie)
		    self.categorie.addItem("")
		else:
		    self.categorie.addItem("")
		    for nom_categorie in result:
		        self.categorie.addItem(nom_categorie)


class Ligne(object):
	"""docstring for ligneCategorie

	(objet) est l'objet contenant tous les éléments de la fenetre.
	Permet d'accéder à ces éléments et de les modifier.
	"""

	def __init__(self, position, nom, sites_lies, objet): 
		self.position = position
		self.nom = nom
		self.sites_lies = sites_lies
		self.objet = objet

		self.ligne = QtWidgets.QHBoxLayout()
		self.label = QtWidgets.QLabel()
		self.pushButton = QtWidgets.QPushButton()
		self.pushButton.clicked.connect(self.suppression)

		self.ligne.addWidget(self.label)
		self.ligne.addWidget(self.pushButton)

	def suppression(self):
		pass

class Categorie(Ligne):
	"""docstring for Categorie"""

	def __init__(self, position, nom, sites_lies, objet):
		super().__init__(position, nom, sites_lies, objet)
		self.label.setObjectName("label_cat")
		self.label.setText(nom)
		self.pushButton.setObjectName("pushButton_cat")
		self.pushButton.setText('X_cat')

	def suppression(self):
		requete = "DELETE FROM categories WHERE nom_categorie=?"
		bdd_delete(requete, (self.nom,))
		print("Categorie supprimée: "+ self.nom)

		# destruction des layouts dans la scroll_area
		self.objet.scrollAreaWidgetContents_cat.deleteLater()
		# on vide les attributs
		self.objet.cats = []
		# On en recrée un vide
		self.objet.scrollAreaWidgetContents_cat = QtWidgets.QWidget()
		self.objet.scrollAreaWidgetContents_cat.setGeometry(QtCore.QRect(0, 0, 177, 767))
		self.objet.scrollAreaWidgetContents_cat.setObjectName("scrollAreaWidgetContents_cat")
		self.objet.verticalLayout_3 = QtWidgets.QVBoxLayout(self.objet.scrollAreaWidgetContents_cat)
		self.objet.verticalLayout_3.setObjectName("verticalLayout_3")
		self.objet.scrollArea_cat.setWidget(self.objet.scrollAreaWidgetContents_cat)
		# on relance la méthode d'affichage des catégories
		self.objet.afficher_categories()


class Password(Ligne):
	"""docstring for Password"""

	def __init__(self, position, nom, sites_lies, objet):
		super().__init__(position, nom, sites_lies, objet)
		self.label.setObjectName("label_pwd")
		self.label.setText(nom)
		self.pushButton.setObjectName("pushButton_pwd")
		self.pushButton.setText('X_pwd')
		

class ClasseGestion(Ui_fenetreGestion):
	def __init__(self, fenetre):
		self.setupUi(fenetre)
		self.ajouter_cat.setPlaceholderText("Ajouter une catégorie")
		self.ajouter_pwd.setPlaceholderText("Ajouter un mot de passe")
		self.ajouter_cat.returnPressed.connect(self.check_if_exist_cat)
		self.ajouter_pwd.returnPressed.connect(self.check_if_exist_pwd)

		self.sites = []
		self.cats = []
		self.pwds = []

		#lancement(self):
		self.afficher_sites()
		self.afficher_categories()
		self.afficher_pwds()

	def check_if_exist_cat(self):
		"""
		Vérifier que la catégorie en question n'est pas déjà dans la base de donnée
		"""
		if self.ajouter_cat.displayText() != "":

		    requete = "SELECT nom_categorie FROM categories WHERE nom_categorie=?"
		    categories_table = bdd_select(requete, (self.ajouter_cat.displayText(),))

		    conditions = not categories_table or categories_table[0][0] != self.ajouter_cat.displayText()
		    if conditions:
		        self.ajouter_categorie()

	def afficher_categories(self):
		requete= 'SELECT nom_categorie FROM categories'
		tab = bdd_select(requete)

		if tab:
		    for k in range(len(tab)):
		        self.ajouter_ligne_categorie(k, tab[k][0])

	def ajouter_categorie(self):
		requete ="INSERT INTO categories (nom_categorie) VALUES(?)"
		bdd_insert(requete, (self.ajouter_cat.displayText(),))

		# ajout de la catégorie dans la scrollArea Categories        
		self.ajouter_ligne_categorie(len(self.cats), self.ajouter_cat.displayText())
		print("Catégorie ajoutée : "+ str(self.ajouter_cat.displayText()))

		"""
		# ajout de la catégorie dans les comboBox
		for y in range(len(self.sites)):
		    self.sites[y]['categorie'].addItem(self.ajouter_cat.displayText())
		"""

		self.ajouter_cat.setText("")

	def ajouter_ligne_categorie(self, y, nom_categorie):
		self.cats.append(Categorie(y, nom_categorie,[], self))
		self.verticalLayout_3.addLayout(self.cats[y].ligne)
		# On garde l'alignement haut
		self.verticalLayout_3.setAlignment(QtCore.Qt.AlignTop) 


	def check_if_exist_pwd(self):
		"""
		Vérifier que le pwd en question n'est pas déjà dans la base de donnée
		"""
		if self.ajouter_pwd.displayText() != "":
		    requete = "SELECT mdp FROM mdps WHERE mdp=?"
		    pwds_table = bdd_select(requete, (self.ajouter_pwd.displayText(),))


		    conditions = not pwds_table or pwds_table[0][0] != self.ajouter_pwd.displayText()
		    if conditions:
		        self.ajouter_password()

	def afficher_pwds(self):
		requete= 'SELECT mdp FROM mdps'
		tab = bdd_select(requete)

		if tab:
		    for k in range(len(tab)):
		        self.ajouter_ligne_pwd(k, tab[k][0])

	def ajouter_password(self):
		requete = "INSERT INTO mdps (mdp) VALUES(?)"
		bdd_insert(requete, (self.ajouter_pwd.displayText(),))

		# ajout dans la ScrollArea Passwords
		self.ajouter_ligne_pwd(len(self.pwds), self.ajouter_pwd.displayText())
		print("Password ajoutée : " + self.ajouter_pwd.displayText())

		"""
		# ajout du mdp dans les comboBox
		for y in range(len(self.sites)):
		    self.sites[y]['mdp'].addItem(self.ajouter_pwd.displayText())
		"""
		self.ajouter_pwd.setText("")

	def ajouter_ligne_pwd(self, y, nom_pwd):
		self.pwds.append(Password(y, nom_pwd, [], self))
		self.verticalLayout_2.addLayout(self.pwds[y].ligne)

		# On garde l'alignement haut
		self.verticalLayout_2.setAlignment(QtCore.Qt.AlignTop)

	def afficher_sites(self):
		requete= 'SELECT site_web, identifiant, mdp, categorie FROM sites_reconnus'
		tab = bdd_select(requete)

		for k in range(len(tab)):
		    self.verticalLayout.addLayout(LigneSite(k,tab[k][0], tab[k][1], tab[k][2], tab[k][3], self).ligne)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    fenetreGestion = QtWidgets.QMainWindow()

    classGestion = ClasseGestion(fenetreGestion)

    fenetreGestion.show()
    sys.exit(app.exec_())
