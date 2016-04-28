import sqlite3
import sys

sys.path.append('../fenetres/')
from functools import partial
from PyQt5 import QtWidgets, QtGui, QtCore
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
		self.nom_mdp = mdp
		self.nom_cat = categorie

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

		self.categorie.currentIndexChanged.connect(self.changement_cat)
		self.mdp.currentIndexChanged.connect(self.changement_pwd)

	def changement_cat(self, event):
		requete ="SELECT categorie FROM sites_reconnus WHERE rowid=?"
		ancienne_categorie = toliste(bdd_select(requete, (self.position+1,)))[0]

		# On ajoute le site_web sous la catégorie correspondate
		requete= 'UPDATE sites_reconnus SET categorie=? WHERE rowid=?'
		bdd_update(requete, (self.categorie.currentText(), self.position +1))
		print("Catégorie changée en"+ self.categorie.currentText())

		for k in range(len(self.objet.cats)):
			if(self.objet.cats[k].nom == self.categorie.currentText()):
				liste_label_name =[]
				for element in self.objet.cats[k].labels:
					liste_label_name.append(element.text())
				print(liste_label_name)
				if(self.categorie.currentText() not in liste_label_name):
					label = QtWidgets.QLabel()

					font = QtGui.QFont()
					font.setPointSize(9)
					font.setItalic(True)
					label.setFont(font)
					label.setText(self.site_web.text())

					self.objet.cats[k].labels.append(label)
					self.objet.cats[k].verticalLayout_groupBox.addWidget(label)
				break

		# On met à jour le groupBox de l'ancienne catégorie
		for k in range(len(self.objet.cats)):
			if(self.objet.cats[k].nom == ancienne_categorie):
				print(self.objet.cats[k].nom)

				for label in self.objet.cats[k].labels:
					label.deleteLater()
				self.objet.cats[k].labels = []

				requete ="SELECT site_web FROM sites_reconnus WHERE categorie=?"
				sites_lies= toliste(bdd_select(requete, (ancienne_categorie,)))
				self.objet.cats[k].affichage_sites_lies(sites_lies)


	def changement_pwd(self):
		requete ="SELECT mdp FROM sites_reconnus WHERE rowid=?"
		ancien_mdp = toliste(bdd_select(requete, (self.position+1,)))[0]

		# On ajoute le site_web sous la catégorie correspondate
		requete= 'UPDATE sites_reconnus SET mdp=? WHERE rowid=?'
		bdd_update(requete, (self.mdp.currentText(), self.position +1))
		print("Mdp changée en"+ self.mdp.currentText())

		for k in range(len(self.objet.pwds)):
			if(self.objet.pwds[k].nom == self.mdp.currentText()):
				liste_label_name =[]
				for element in self.objet.pwds[k].labels:
					liste_label_name.append(element.text())
				print(liste_label_name)
				if(self.mdp.currentText() not in liste_label_name):
					label = QtWidgets.QLabel()

					font = QtGui.QFont()
					font.setPointSize(9)
					font.setItalic(True)
					label.setFont(font)
					label.setText(self.site_web.text())

					self.objet.pwds[k].labels.append(label)
					self.objet.pwds[k].verticalLayout_groupBox.addWidget(label)
				break

		# On met à jour le groupBox de l'ancienne catégorie
		for k in range(len(self.objet.pwds)):
			if(self.objet.pwds[k].nom == ancien_mdp):
				print(self.objet.pwds[k].nom)

				for label in self.objet.pwds[k].labels:
					label.deleteLater()
				self.objet.pwds[k].labels = []

				requete ="SELECT site_web FROM sites_reconnus WHERE mdp=?"
				sites_lies= toliste(bdd_select(requete, (ancien_mdp,)))
				self.objet.pwds[k].affichage_sites_lies(sites_lies)

	def afficher_combo_pwd(self):
		requete= 'SELECT mdp FROM mdps'
		tab = bdd_select(requete)
		result = []
		for k in range(len(tab)):
		    result.append(tab[k][0])

		self.mdp.addItem(self.nom_mdp)
		for pwd in result:
		    if pwd != self.nom_mdp:
		        self.mdp.addItem(pwd)

	def afficher_combo_cat(self):
		requete= 'SELECT nom_categorie FROM categories'
		tab = bdd_select(requete)
		result = []
		for k in range(len(tab)):
		    result.append(tab[k][0])

		self.categorie.addItem(self.nom_cat)
		for cat in result:
		    if cat != self.nom_cat:
		        self.categorie.addItem(cat)

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
		self.pushButton = QtWidgets.QPushButton()
		self.groupBox = QtWidgets.QGroupBox()
		self.labels = [] # contiendra la liste des labels (noms des sites liés)
		self.groupBox.setGeometry(QtCore.QRect(20, 50, 91, 50))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.groupBox.setFont(font)
		self.groupBox.setObjectName("groupBox")
		self.verticalLayout_groupBox = QtWidgets.QVBoxLayout(self.groupBox)
		self.verticalLayout_groupBox.setObjectName("verticalLayout_groupBox")

		self.ligne.addWidget(self.groupBox)
		self.ligne.addWidget(self.pushButton)
		self.ligne.setStretch(0, 3)
		self.ligne.setStretch(1, 1)


		self.affichage_sites_lies(sites_lies)

		# Evènement
		self.pushButton.clicked.connect(self.suppression)


	def suppression(self):
		self.suppression_bdd()
		self.suppression_affichage()

	def affichage_sites_lies(self, site_lies):
		pass

class Categorie(Ligne):
	"""docstring for Categorie"""

	def __init__(self, position, nom, sites_lies, objet):
		super().__init__(position, nom, sites_lies, objet)
		self.groupBox.setObjectName("groupBox_cat")
		self.groupBox.setTitle(nom)
		self.pushButton.setObjectName("pushButton_cat")
		self.pushButton.setText('X')

	def affichage_sites_lies(self, sites_lies):
		for site in sites_lies:
			label = QtWidgets.QLabel()
				
			font = QtGui.QFont()
			font.setPointSize(9)
			font.setItalic(True)
			label.setFont(font)
			label.setText(site)

			self.labels.append(label)
			self.verticalLayout_groupBox.addWidget(label)


	def suppression_bdd(self):
		requete = "DELETE FROM categories WHERE nom_categorie=?"
		bdd_delete(requete, (self.nom,))
		print("Categorie supprimée: "+ self.nom)

	def suppression_affichage(self):
		# suppression combobox
		for k in range(len(self.objet.sites)):
		    if self.objet.sites[k].categorie.currentText() == self.nom:
		        # si la catégorie supprimée était celle du site, alors on change la catégorie de celui-ci en le choix vide:""
		        if self.objet.sites[k].categorie.findText("") == -1:
		            # si il n'y a pas le choix vide "", on l'ajoute
		            self.objet.sites[k].categorie.addItem("")
		        self.objet.sites[k].categorie.setCurrentIndex(self.objet.sites[k].categorie.findText(""))
		    index = self.objet.sites[k].categorie.findText(self.nom)
		    self.objet.sites[k].categorie.removeItem(index)


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

	def ajout_combobox(self):
		for k in range(len(self.objet.sites)):
		    self.objet.sites[k].categorie.addItem(self.nom)


class Password(Ligne):
	"""docstring for Password"""

	def __init__(self, position, nom, sites_lies, objet):
		super().__init__(position, nom, sites_lies, objet)
		self.groupBox.setObjectName("groupBox_pwd")
		self.groupBox.setTitle(nom)
		self.pushButton.setObjectName("pushButton_pwd")
		self.pushButton.setText('X')

	def affichage_sites_lies(self, sites_lies):
		for site in sites_lies:
			label = QtWidgets.QLabel()
				
			font = QtGui.QFont()
			font.setPointSize(9)
			font.setItalic(True)
			label.setFont(font)
			label.setText(site)

			self.labels.append(label)
			self.verticalLayout_groupBox.addWidget(label)

	def suppression_bdd(self):
		requete = "DELETE FROM mdps WHERE mdp=?"
		bdd_delete(requete, (self.nom,))
		print("Pwd supprimée: "+ self.nom)

	def suppression_affichage(self):
		# suppression combobox
		for k in range(len(self.objet.sites)):
		    if self.objet.sites[k].mdp.currentText() == self.nom:
		        # si le mdp supprimée était celui du site, alors on change le change en le choix vide:""
		        if self.objet.sites[k].mdp.findText("") == -1:
		            # si il n'y a pas le choix vide "", on l'ajoute
		            self.objet.sites[k].mdp.addItem("")
		        self.objet.sites[k].mdp.setCurrentIndex(self.objet.sites[k].mdp.findText(""))
		    index = self.objet.sites[k].mdp.findText(self.nom)
		    self.objet.sites[k].mdp.removeItem(index)

		# destruction des layouts dans la scroll_area
		self.objet.scrollAreaWidgetContents_pwd.deleteLater()
		# on vide les attributs
		self.objet.pwds = []
		# On en recrée un vide
		self.objet.scrollAreaWidgetContents_pwd = QtWidgets.QWidget()
		self.objet.scrollAreaWidgetContents_pwd.setGeometry(QtCore.QRect(0, 0, 177, 767))
		self.objet.scrollAreaWidgetContents_pwd.setObjectName("scrollAreaWidgetContents_cat")
		self.objet.verticalLayout_2 = QtWidgets.QVBoxLayout(self.objet.scrollAreaWidgetContents_pwd)
		self.objet.verticalLayout_2.setObjectName("verticalLayout_3")
		self.objet.scrollArea_pwd.setWidget(self.objet.scrollAreaWidgetContents_pwd)
		# on relance la méthode d'affichage des mdps
		self.objet.afficher_pwds()
		

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

		#ajout dans les combobox
		for k in range(len(self.sites)):
			self.sites[k].categorie.addItem(self.ajouter_cat.displayText())

		# ajout de la catégorie dans la scrollArea Categories        
		self.ajouter_ligne_categorie(len(self.cats), self.ajouter_cat.displayText())
		print("Catégorie ajoutée : "+ str(self.ajouter_cat.displayText()))

		self.ajouter_cat.setText("")


	def ajouter_ligne_categorie(self, y, nom_categorie):
		requete = "SELECT site_web FROM sites_reconnus WHERE categorie=?"
		sites_lies= toliste(bdd_select(requete, (nom_categorie,)))
		self.cats.append(Categorie(y, nom_categorie, sites_lies, self))
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

		#ajout dans les combobox
		for k in range(len(self.sites)):
			self.sites[k].mdp.addItem(self.ajouter_pwd.displayText())

		# ajout dans la ScrollArea Passwords
		self.ajouter_ligne_pwd(len(self.pwds), self.ajouter_pwd.displayText())
		print("Password ajoutée : " + self.ajouter_pwd.displayText())

		self.ajouter_pwd.setText("")

	def ajouter_ligne_pwd(self, y, nom_pwd):
		requete = "SELECT site_web FROM sites_reconnus WHERE mdp=?"
		sites_lies= toliste(bdd_select(requete, (nom_pwd,)))
		self.pwds.append(Password(y, nom_pwd, sites_lies, self))
		self.verticalLayout_2.addLayout(self.pwds[y].ligne)

		# On garde l'alignement haut
		self.verticalLayout_2.setAlignment(QtCore.Qt.AlignTop)

	def afficher_sites(self):
		requete= 'SELECT site_web, identifiant, mdp, categorie FROM sites_reconnus'
		tab = bdd_select(requete)

		for k in range(len(tab)):
			self.sites.append(LigneSite(k,tab[k][0], tab[k][1], tab[k][2], tab[k][3], self))
			self.verticalLayout.addLayout(self.sites[k].ligne)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    fenetreGestion = QtWidgets.QMainWindow()

    classGestion = ClasseGestion(fenetreGestion)

    fenetreGestion.show()
    sys.exit(app.exec_())
