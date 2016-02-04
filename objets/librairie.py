# -*- coding: utf-8 -*-
import sqlite3

class Table(object):
	"""docstring for Table
	Définit une table dans la bdd, destinée à contenir les mails d'une adresse données.

	Attributs:
	-name, est en fait l'adresse mail de l'utilisateur (str), utile dans le cas où
	il nous fournit plusieurs adresses.
	-bdd, fichier .sq3 qui contient les données.
	Méthodes:
	-la connexion se fait lors du constructeur.
	"""
	bdd="MaBaseDeDonnes.sq3"
	def __init__(self, name):
		self.name = name
		self.conn=sqlite3.connect(Table.bdd)
		self.cur=self.conn.cursor()
		self.cur.execute ("CREATE TABLE IF NOT EXISTS "+self.name+\
			" (id TEXT, expéditeur TEXT, sujet TEXT, contenu TEXT, date TEXT)")

	def addMail(self, id_message, expediteur, sujet, contenu, date):
		self.cur.execute("INSERT INTO "+self.name+" (id, expéditeur, sujet, contenu, date) VALUES(?,?,?,?,?)",\
			(id_message, expediteur, sujet, contenu, date))

	def saveAndClose(self):
		self.conn.commit()
		self.cur.close()
		self.conn.close()


