import sqlite3
import sys

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



sys.path.append('../fenetres/')
from functools import partial
from PyQt5 import QtWidgets, QtGui, QtCore
from fenetreGestion import Ui_fenetreGestion
from requetes import *
import numpy as np
import colorsys

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
    table sites_reconnus_"+self.nom_table+".
    """
    def __init__(self, nom_table):
    	super().__init__()
    	self.nom_table = nom_table

    def focusOutEvent(self, arg):
        QtWidgets.QLineEdit.focusOutEvent(self, arg)
        # self.id contient l'id de la LigneEdit, ajouté dans afficher_ligne_site()

        requete= "UPDATE sites_reconnus_"+self.nom_table+" SET identifiant =? WHERE rowid=?"
        bdd_update(requete, (self.text(), self.id +1))

        if self.text() == "":
            self.setPlaceholderText("Ajouter un pseudo")



class LigneSite(object):
	"""docstring for LigneSite"""
	def __init__(self, y, site_web, identifiant, mdp, categorie, objet, nom_table):
		self.position = y
		self.objet = objet
		self.nom_site = site_web
		self.nom_mdp = mdp
		self.nom_cat = categorie
		self.nom_table = nom_table

		self.ligne = QtWidgets.QHBoxLayout()
		self.site_web =QtWidgets.QLabel()
		self.site_web.setAlignment(QtCore.Qt.AlignCenter)
		self.site_web.setObjectName("site_web")
		self.site_web.setText(site_web)
		self.ligne.addWidget(self.site_web)

		self.identifiant = LineEditWithFocusOut(self.nom_table)
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
		requete ="SELECT categorie FROM sites_reconnus_"+self.nom_table+" WHERE rowid=?"
		ancienne_categorie = toliste(bdd_select(requete, (self.position+1,)))[0]

		# On ajoute le site_web sous la catégorie correspondante
		requete= "UPDATE sites_reconnus_"+self.nom_table+" SET categorie=? WHERE rowid=?"
		bdd_update(requete, (self.categorie.currentText(), self.position +1))
		print("Catégorie changée en"+ self.categorie.currentText())

		for k in range(len(self.objet.cats)):
			if(self.objet.cats[k].nom == self.categorie.currentText()):
				liste_label_name =[]
				for element in self.objet.cats[k].labels:
					liste_label_name.append(element.text())
				if(self.categorie.currentText() not in liste_label_name):
					label = QtWidgets.QLabel()

					font = QtGui.QFont()
					font.setPointSize(9)
					font.setItalic(True)
					label.setFont(font)
					label.setObjectName("sites_lies_cat")
					label.setText(self.site_web.text())

					self.objet.cats[k].labels.append(label)
					self.objet.cats[k].verticalLayout_groupBox.addWidget(label)
				break

		# On met à jour le groupBox de l'ancienne catégorie
		for k in range(len(self.objet.cats)):
			if(self.objet.cats[k].nom == ancienne_categorie):
				for label in self.objet.cats[k].labels:
					label.deleteLater()
				self.objet.cats[k].labels = []

				requete ="SELECT site_web FROM sites_reconnus_"+self.nom_table+" WHERE categorie=?"
				sites_lies= toliste(bdd_select(requete, (ancienne_categorie,)))
				self.objet.cats[k].affichage_sites_lies(sites_lies)

		# On update le label dont la catégorie a été changée
		for pwd in self.objet.pwds:
			for label in pwd.labels:
				if(label.texte == self.nom_site):
					pwd.update(label, self.categorie.currentText())
					# On update la couleur du groupBox_pwd contenant le label associé
					pwd.update_color_groupBox()

	def changement_pwd(self):
		requete ="SELECT mdp FROM sites_reconnus_"+self.nom_table+" WHERE rowid=?"
		ancien_mdp = toliste(bdd_select(requete, (self.position+1,)))[0]

		# On ajoute le site_web sous le mdp correspondant
		requete= "UPDATE sites_reconnus_"+self.nom_table+" SET mdp=? WHERE rowid=?"
		nouveau_mdp = self.mdp.currentText()
		bdd_update(requete, (nouveau_mdp , self.position +1))
		print("Mdp changée en"+ nouveau_mdp)

		for k in range(len(self.objet.pwds)):
			if(self.objet.pwds[k].nom == nouveau_mdp):
				liste_label_name =[]
				for element in self.objet.pwds[k].labels:
					liste_label_name.append(element.text())
				if(nouveau_mdp not in liste_label_name):
					self.objet.pwds[k].label(self.site_web.text())
				break

		# On met à jour le groupBox de l'ancienn mdp
		for k in range(len(self.objet.pwds)):
			if(self.objet.pwds[k].nom == ancien_mdp):
				for label in self.objet.pwds[k].labels:
					label.deleteLater()
				self.objet.pwds[k].labels = []

				requete ="SELECT site_web FROM sites_reconnus_"+self.nom_table+" WHERE mdp=?"
				sites_lies= toliste(bdd_select(requete, (ancien_mdp,)))
				self.objet.pwds[k].affichage_sites_lies(sites_lies)

		for pwd in self.objet.pwds:
			if(pwd.nom == ancien_mdp):
				pwd.update_color_groupBox()
			elif(pwd.nom == nouveau_mdp):
				pwd.update_color_groupBox()

	def update_pwd_combobox(self, complet):
		print(self.mdp.maxCount())



	def afficher_combo_pwd(self):
		requete= "SELECT mdp FROM mdps_"+self.nom_table+""
		tab = bdd_select(requete)
		result = []
		for k in range(len(tab)):
		    result.append(tab[k][0])

		self.mdp.addItem(self.nom_mdp)
		for pwd in result:
		    if pwd and pwd != self.nom_mdp:
		        self.mdp.addItem(pwd)
		if(self.nom_mdp and self.nom_mdp != ""):
			self.mdp.addItem("")

	def afficher_combo_cat(self):
		requete= "SELECT nom_categorie FROM categories_"+self.nom_table 
		tab = bdd_select(requete)
		result = []
		for k in range(len(tab)):
		    result.append(tab[k][0])

		self.categorie.addItem(self.nom_cat)
		for cat in result:
		    if cat and cat != self.nom_cat:
		        self.categorie.addItem(cat)
		if(self.nom_cat and self.nom_cat != ""):
			self.categorie.addItem("")

class Ligne(object):
	"""docstring for ligneCategorie

	(objet) est l'objet contenant tous les éléments de la fenetre.
	Permet d'accéder à ces éléments et de les modifier.
	"""

	def __init__(self, position, nom, sites_lies, objet, nom_table): 
		self.position = position
		self.nom = nom
		self.sites_lies = sites_lies
		self.objet = objet
		self.nom_table =nom_table

		self.ligne = QtWidgets.QHBoxLayout()
		self.pushButton = QtWidgets.QPushButton()

		self.pushButton.setMinimumSize(QtCore.QSize(24, 24))

		self.groupBox = QtWidgets.QGroupBox()
		self.colorHEX = "#757575"
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
		self.ligne.setStretch(0, 20)
		self.ligne.setStretch(1, 1)


		self.affichage_sites_lies(sites_lies)

		# Evènement
		self.pushButton.clicked.connect(self.msgbox)

	def msgbox(self):
		msg = QtWidgets.QMessageBox()
		msg.setIcon(QtWidgets.QMessageBox.Information)

		msg.setText("Voulez-vous vraiment supprimer \""+ str(self.nom) + "\" ?")
		msg.setIcon(2)
		msg.setInformativeText("Les liens établis avec les sites seront perdus.")
		msg.setWindowTitle("Confirmer suppression")
		msg.addButton(QtWidgets.QPushButton('Oui'), QtWidgets.QMessageBox.YesRole)
		msg.addButton(QtWidgets.QPushButton('Non'), QtWidgets.QMessageBox.NoRole)

		msg.buttonClicked.connect(self.msgbtn)
		ret = msg.exec_();

	def msgbtn(self, buttonClicked):
		if(buttonClicked.text() == "Oui"):
			self.suppression()

	def suppression(self):
		self.suppression_bdd()
		self.suppression_affichage()

	def affichage_sites_lies(self, site_lies):
		pass

class Categorie(Ligne):
	"""docstring for Categorie"""

	def __init__(self, position, nom, sites_lies, objet, nom_table):
		# On exécute Ligne.__init__()
		super().__init__(position, nom, sites_lies, objet, nom_table)
		# On ajoute d'autres attributs/propriétés
		self.ligne.setObjectName("ligne_categorie")
		self.groupBox.setObjectName("groupBox_cat")
		self.groupBox.setTitle(nom)
		self.pushButton.setObjectName("pushButton_cat")

	def setColor(self, k, nb_cat):
		
		num_colors=nb_cat
		colors=[]
		for i in np.arange(0., 360., 360. / num_colors):
			hue = i/360.
			lightness = (50 + np.random.rand() * 10)/100.
			saturation = (55 + np.random.rand() * 10)/100.
			colors.append(colorsys.hls_to_rgb(hue, lightness, saturation))
		t= colors
		
		self.colorRGB = (int(t[k][0]*255),int(t[k][1]*255),int(t[k][2]*255))
		self.colorHEX ='#%02x%02x%02x' % self.colorRGB

		self.groupBox.setStyleSheet("QGroupBox {\n"
			"border: 2px solid rgb(" + str(self.colorRGB[0]) + "," + str(self.colorRGB[1]) + "," + str(self.colorRGB[2]) + ");\n"
			"}\n"
			"QGroupBox:title {\n"
			"color: rgb(" + str(self.colorRGB[0]) + "," + str(self.colorRGB[1]) + "," + str(self.colorRGB[2]) + ");\n"
			"}\n"
			)

	def affichage_sites_lies(self, sites_lies):
		for site in sites_lies:
			label = QtWidgets.QLabel()
				
			font = QtGui.QFont()
			font.setPointSize(9)
			font.setItalic(True)
			label.setFont(font)
			label.setObjectName("sites_lies_cat")
			label.setText(site)

			self.labels.append(label)
			self.verticalLayout_groupBox.addWidget(label)


	def suppression_bdd(self):
		requete = "DELETE FROM categories_"+self.nom_table +" WHERE nom_categorie=?"
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
		self.objet.actualiser_couleur_pwd()


	def ajout_combobox(self):
		for k in range(len(self.objet.sites)):
		    self.objet.sites[k].categorie.addItem(self.nom)


class Password(Ligne):
	"""docstring for Password"""

	def __init__(self, position, nom, sites_lies, objet, nom_table):
		super().__init__(position, nom, sites_lies, objet, nom_table)
		self.ligne.setObjectName("ligne_pwd")
		self.groupBox.setObjectName("groupBox_pwd")
		self.groupBox.setTitle(nom)
		self.pushButton.setObjectName("pushButton_pwd")

		# On modifie la couleur de la groupBox_pwd
		self.update_color_groupBox()

	def update_title(self, titre):
		self.groupBox.setTitle(titre)

	def affichage_sites_lies(self, sites_lies):
		for site in sites_lies:
			self.label(site)

	def label(self, site):
		label = QtWidgets.QLabel()
		label.texte = site
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setItalic(True)
		label.setFont(font)
		label.setObjectName("sites_lies_pwd")
		label.colorRGB = self.getColor_label(site)[0]
		label.colorHEX = self.getColor_label(site)[1]

		texte = self.create_text_label(label.colorHEX, site)
		label.setText(texte)

		self.labels.append(label)
		self.verticalLayout_groupBox.addWidget(label)

	def create_text_label(self, couleur, site):
		texte = "<font size='5' font-style='' color="+couleur+">•</font> "
		for lettre in site:
			texte += lettre
		return(texte)


	def update(self, label, categorie):
		couleur ="#fff"
		for k in range(len(self.objet.cats)):
			if(self.objet.cats[k].nom == categorie):
				couleur = self.objet.cats[k].colorHEX

		label.colorHEX = couleur
		texte= self.create_text_label(couleur, label.texte)
		label.setText(texte)


	def update_color_groupBox(self):

		colorGroupBox = self.colorHEX
		if(self.labels != []):
			if(self.labels[0].colorHEX != "#fff"):
				colorGroupBox = self.labels[0].colorHEX
			b = 1
			for label in self.labels:
				if(label.colorHEX != colorGroupBox):
					b=0
			if(not b):
				colorGroupBox = "#757575"
		else:
			colorGroupBox = "#757575"
		
		self.groupBox.setStyleSheet("QGroupBox {"
			"border-color:"+colorGroupBox+";"
			"}")


	def getColor_label(self, site):
		"""En paramètre le site, retourne un tableau de couleur [RGB, HEX] (associée à la categorie
		éventuellement assignées
		"""
		requete = "SELECT categorie FROM sites_reconnus_"+self.nom_table+" WHERE site_web=?"
		categorie = toliste(bdd_select(requete, (site,)))[0]

		tab = ["rgb(255,255,255)","#fff"]

		for k in range(len(self.objet.cats)):
			if(self.objet.cats[k].nom == categorie):
				tab[0] = self.objet.cats[k].colorRGB
				tab[1] = self.objet.cats[k].colorHEX
		return(tab)



	def suppression_bdd(self):
		requete = "DELETE FROM mdps_"+self.nom_table+" WHERE mdp=?"
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
		# on relance la méthode d'affichage des mdps_"+self.nom_table+"
		self.objet.afficher_pwds()
		

class ClasseGestion(Ui_fenetreGestion):
	def __init__(self, fenetre):
		self.setupUi(fenetre)
		self.ajouter_cat.setPlaceholderText("Ajouter une catégorie")
		self.ajouter_pwd.setPlaceholderText("Ajouter un mot de passe")
		self.lineEdit_ajout_site.setPlaceholderText("Ajouter un site web")


		# Evènements
		self.ajouter_cat.returnPressed.connect(self.check_if_exist_cat)
		self.ajouter_pwd.returnPressed.connect(self.check_if_exist_pwd)
		self.lineEdit_ajout_site.returnPressed.connect(self.check_new_site)
		self.pushButton_ajout_site.clicked.connect(self.check_new_site)



		self.sites = []
		self.cats = []
		self.pwds = []

	def lancement(self, user_email, nom_table):
		self.user_email = user_email
		self.nom_table = nom_table
		self.afficher_sites()
		self.afficher_categories()
		self.afficher_pwds()
		self.setupMenu()

		
	def setupMenu(self):
		self.aide_url = "https://github.com/MindPass/Code/wiki/Aide"
		self.apropos_url  ="https://github.com/MindPass/Code"
		self.actionObtenir_de_l_aide.triggered.connect(self.ouvrirAide)
		self.actionA_propos_de_MindPass.triggered.connect(self.ouvrirApropos)

		"""
		self.actionMode_deux_lettres.triggered.connect(self.check_deux_lettres)
		self.actionMode_complet.triggered.connect(self.check_complet)
		self.menuAffichage()
		"""
	"""
	def check_deux_lettres(self):
		self.actionMode_deux_lettres.setChecked(True)
		self.actionMode_complet.setChecked(False)
		self.menuAffichage()

	def check_complet(self):
		self.actionMode_deux_lettres.setChecked(False)
		self.actionMode_complet.setChecked(True)
		self.menuAffichage()


	def menuAffichage(self):
		if(self.actionMode_deux_lettres.isChecked()):
			self.affichage_deux_lettres()
		else:
			self.affichage_complet()

    
	def affichage_complet(self):
		for pwd in self.pwds:
			pwd.update_title(pwd.nom)
		for site in self.sites:
			site.update_pwd_combobox(1)


	def affichage_deux_lettres(self):
		pass
	"""		

	def ouvrirAide(self):
		self.openURL(self.aide_url)

	def ouvrirApropos(self):
		self.openURL(self.apropos_url)

	def openURL(self, given_url):
		url = QtCore.QUrl(given_url)
		if not QtGui.QDesktopServices.openUrl(url):
		    QtGui.QMessageBox.warning(self, "Open Url", "Could not open url")


	def check_if_exist_cat(self):
		"""
		Vérifier que la catégorie en question n'est pas déjà dans la base de donnée
		"""
		if self.ajouter_cat.displayText() != "":

			requete = "SELECT nom_categorie FROM categories_"+self.nom_table +" WHERE nom_categorie=?"
			categories_table = bdd_select(requete, (self.ajouter_cat.displayText(),))

			conditions = not categories_table or categories_table[0][0] != self.ajouter_cat.displayText()
			if conditions:

				self.ajouter_categorie()
				# On actualise les couleurs des catégories
				self.actualiser_couleur()
				# On actualise les couleurs des labels dans la colonne Mots de Passe
				self.actualiser_couleur_pwd()

	def actualiser_couleur(self):
		nb_cat = len(self.cats)
		for i in range(nb_cat):
			self.cats[i].setColor(i, nb_cat)


	def afficher_categories(self):
		requete= "SELECT nom_categorie FROM categories_"+self.nom_table 
		tab = bdd_select(requete)

		if tab:
		    for k in range(len(tab)):
		        self.ajouter_ligne_categorie(k, tab[k][0])

		self.actualiser_couleur()


	def ajouter_categorie(self):
		requete ="INSERT INTO categories_"+self.nom_table +" (nom_categorie) VALUES(?)"
		bdd_insert(requete, (self.ajouter_cat.displayText(),))

		#ajout dans les combobox
		for k in range(len(self.sites)):
			self.sites[k].categorie.addItem(self.ajouter_cat.displayText())

		# ajout de la catégorie dans la scrollArea Categories        
		self.ajouter_ligne_categorie(len(self.cats), self.ajouter_cat.displayText())
		print("Catégorie ajoutée : "+ str(self.ajouter_cat.displayText()))

		self.ajouter_cat.setText("")


	def ajouter_ligne_categorie(self, y, nom_categorie):
		requete = "SELECT site_web FROM sites_reconnus_"+self.nom_table+" WHERE categorie=?"
		sites_lies= toliste(bdd_select(requete, (nom_categorie,)))
		self.cats.append(Categorie(y, nom_categorie, sites_lies, self , self.nom_table))
		self.verticalLayout_3.addLayout(self.cats[y].ligne)
		# On garde l'alignement haut
		self.verticalLayout_3.setAlignment(QtCore.Qt.AlignTop) 


	def check_if_exist_pwd(self):
		"""
		Vérifier que le pwd en question n'est pas déjà dans la base de donnée
		"""
		if self.ajouter_pwd.displayText() != "":
		    requete = "SELECT mdp FROM mdps_"+self.nom_table+" WHERE mdp=?"
		    pwds_table = bdd_select(requete, (self.ajouter_pwd.displayText(),))
		    conditions = not pwds_table or pwds_table[0][0] != self.ajouter_pwd.displayText()
		    if conditions:
		        self.ajouter_password()


	def afficher_pwds(self):
		requete= "SELECT mdp FROM mdps_"+self.nom_table+""
		tab = bdd_select(requete)

		if tab:
		    for k in range(len(tab)):
		        self.ajouter_ligne_pwd(k, tab[k][0])


	def ajouter_password(self):
		requete = "INSERT INTO mdps_"+self.nom_table+" (mdp) VALUES(?)"
		bdd_insert(requete, (self.ajouter_pwd.displayText(),))

		#ajout dans les combobox
		for k in range(len(self.sites)):
			self.sites[k].mdp.addItem(self.ajouter_pwd.displayText())

		# ajout dans la ScrollArea Passwords
		self.ajouter_ligne_pwd(len(self.pwds), self.ajouter_pwd.displayText())
		print("Password ajoutée : " + self.ajouter_pwd.displayText())

		self.ajouter_pwd.setText("")

	def ajouter_ligne_pwd(self, y, nom_pwd):
		requete = "SELECT site_web FROM sites_reconnus_"+self.nom_table+" WHERE mdp=?"
		sites_lies= toliste(bdd_select(requete, (nom_pwd,)))
		self.pwds.append(Password(y, nom_pwd, sites_lies, self, self.nom_table))
		self.verticalLayout_2.addLayout(self.pwds[y].ligne)

		# On garde l'alignement haut
		self.verticalLayout_2.setAlignment(QtCore.Qt.AlignTop)


	def actualiser_couleur_pwd(self):
		# destruction des layouts dans la scroll_area
		self.scrollAreaWidgetContents_pwd.deleteLater()
		# on vide les attributs
		self.pwds = []
		# On en recrée un vide
		self.scrollAreaWidgetContents_pwd = QtWidgets.QWidget()
		self.scrollAreaWidgetContents_pwd.setGeometry(QtCore.QRect(0, 0, 177, 767))
		self.scrollAreaWidgetContents_pwd.setObjectName("scrollAreaWidgetContents_cat")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_pwd)
		self.verticalLayout_2.setObjectName("verticalLayout_3")
		self.scrollArea_pwd.setWidget(self.scrollAreaWidgetContents_pwd)
		# on relance la méthode d'affichage des mdps_"+self.nom_table+"
		self.afficher_pwds()


	def afficher_sites(self):
		requete= "SELECT site_web, identifiant, mdp, categorie FROM sites_reconnus_"+self.nom_table+""
		tab = bdd_select(requete)

		for k in range(len(tab)):
			self.sites.append(LigneSite(k,tab[k][0], tab[k][1], tab[k][2], tab[k][3], self, self.nom_table))
			self.verticalLayout.addLayout(self.sites[k].ligne)

	def check_new_site(self):
		requete =  "SELECT site_web FROM sites_reconnus_"+self.nom_table+""
		sites_web = toliste(bdd_select(requete))

		if(self.lineEdit_ajout_site.text() not in sites_web and self.lineEdit_ajout_site.text() != ""):
			requete = "INSERT INTO sites_reconnus_"+self.nom_table+" VALUES(?,?,?,?,?)"
			valeurs =("",self.lineEdit_ajout_site.text(),"", "", "")
			bdd_insert(requete, valeurs)
			self.sites.append(LigneSite(len(self.sites), self.lineEdit_ajout_site.text(), "", "", "", self, self.nom_table))
			self.verticalLayout.addLayout(self.sites[len(self.sites)-1].ligne)
			self.lineEdit_ajout_site.setText("")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    fenetreGestion = QtWidgets.QMainWindow()

    classGestion = ClasseGestion(fenetreGestion)

    fenetreGestion.show()
    sys.exit(app.exec_())
