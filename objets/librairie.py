# -*- coding: utf-8 -*-
import sqlite3

class Table(object):
	"""docstring for Table
	Définit une table dans la bdd, destinée à contenir les mails d'une adresse donnée; classe
	utile si l'utilisateur nous en fournit plusieurs.

	Attributs,
	De classe:
	-bdd est le fichier .sq3 contenant les données.
	D'instance:
	-name, qui peut être l'adresse donnée.
	-conn et cur, sont des variables permettant de se conecter à la bdd en sqlite (.sq3).
	"""

	bdd="MaBaseDeDonnes.sq3"
	def __init__(self, name):
		"""Constructeur
		On créé la table name si elle n'existe pas
		"""
		self.name = name
		self.conn=sqlite3.connect(Table.bdd)
		self.cur=self.conn.cursor()
		self.cur.execute ("CREATE TABLE IF NOT EXISTS "+self.name+\
			" (id TEXT, expediteur TEXT, sujet TEXT, contenu TEXT, date TEXT)")
		#se prémunir d'une injection SQL reste à faire

	def add_mail(self, arg):
		"""
		Prend une liste, tuple ou dictionnaire en paramètre.
		"""
		if(isinstance(arg, list) or isinstance(arg, tuple)):
			self.cur.execute("INSERT INTO "+self.name+" (id, expediteur, sujet, contenu, date) VALUES(?,?,?,?,?)",\
				(arg[0], arg[1], arg[2], arg[3], arg[4]))
		elif(isinstance(arg, dict)):
			self.cur.execute("INSERT INTO "+self.name+" (id, expediteur, sujet, contenu, date) VALUES(?,?,?,?,?)",\
				(arg["id"], arg["expediteur"], arg["sujet"], arg["contenu"], arg["date"]))
		else:
			print("L'argument passé à addMail n'est pas du bon type")

	def get_id(self):
		self.cur.execute("SELECT id FROM "+self.name)
		self.tab=self.cur.fetchall()
		self.liste_id=[]
		for element in self.tab:
		    self.liste_id.append(element[0])
		return(self.liste_id)

	def save(self):
		self.conn.commit()
	
	def close(self):
		self.cur.close()
		self.conn.close()

def Table_Externe(object):

