# -*- coding: utf-8 -*-
import imaplib, urllib.parse, re, sqlite3
from email.parser import FeedParser

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
		cmd="CREATE TABLE IF NOT EXISTS %s (id TEXT, expediteur TEXT, sujet TEXT, contenu TEXT, date TEXT)" % name
		self.cur.execute (cmd)
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

	def liste_id(self):
		self.cur.execute("SELECT id FROM "+self.name)
		tab=self.cur.fetchall()
		liste_id=[]
		for element in tab:
			liste_id.append(element[0])
		return(liste_id)

	def save(self):
		self.conn.commit()
	
	def close(self):
		self.cur.close()
		self.conn.close()


class TableExterne(object):
	"""docstring for TableExterne


	"""
	def __init__(self, connexion, user, mdp):
		self.connexion = connexion
		self.user= user
		self.mdp= mdp

		self.imap_conn = imaplib.IMAP4_SSL(connexion)
		self.imap_conn.debug = 4
		self.imap_conn.login(user,mdp)
		self.imap_conn.select('INBOX') #renvoie ('OK', b'nombredemaildanslaboite')

	def liste_id(self):
		result, data = self.imap_conn.search(None, "ALL") # result vaut 'OK' si la requête a aboutie
		ids = data[0] # data est une liste à un élément, contenant les id des mails
		liste_mails_inbox = ids.split() # ids est une string d'id séparés par un espace
		return(liste_mails_inbox)

	def raw_email(self, email_id):
		result, data = self.imap_conn.fetch(email_id, "(RFC822)") 
		# fetch the email body (RFC822) for the given ID
		raw_email = data[0][1].decode('utf-8')
		return(raw_email)

	def email_as_list(self, email_id):
		raw_email=self.raw_email(email_id)
		f = FeedParser()
		f.feed(raw_email)
		rootMessage = f.close()
		
		if(rootMessage.is_multipart()):
			corps=rootMessage.get_payload(0).get_payload(decode=True).decode('utf-8')
			# Récupérer le corps du mail en plain/text bien décodé
		else:
			corps=rootMessage.get_payload(decode=True).decode('utf-8')

		subject=rootMessage.get('Subject') 
		#méthode Alex 
		# suppression des entêtes inutiles avec une regexp
		subject=rootMessage.get('Subject')
		for i in range(len(subject)):
			if subject[i] == "=":
				subject = subject[:i] + "%" + subject[i+1:]
			elif subject[i] == "_":
				subject = subject[:i] + " " + subject[i+1:]
		subject = re.sub('(\n)*\%\?(UTF|utf)\-8\?(Q|B|q|b)\? *', '', subject)
		subject = re.sub('\?\%(\r\n)*', '', subject)
		subject=urllib.parse.unquote(subject) 
		#fin méthode Alex

		date =rootMessage.get('Date')
		exp=rootMessage.get('From')

		email_liste=[]
		email_liste.extend((email_id,exp, corps, date))

		return(email_liste)


	def close(self):
		self.imap_conn.close()
		self.imap_conn.logout()









		

















