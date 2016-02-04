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
	-conn et cur, sont des variables permettant de se conecter à une bdd en sqlite (.sq3).
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
			" (id TEXT, expéditeur TEXT, sujet TEXT, contenu TEXT, date TEXT)")
		#se prémunir d'une injection SQL reste à faire

	def addMail(self, id_message, expediteur, sujet, contenu, date):
		self.cur.execute("INSERT INTO "+self.name+" (id, expéditeur, sujet, contenu, date) VALUES(?,?,?,?,?)",\
			(id_message, expediteur, sujet, contenu, date))
		#se prémunir d'une injection SQL reste à faire

	def saveAndClose(self):
		self.conn.commit()
		self.cur.close()
		self.conn.close()


