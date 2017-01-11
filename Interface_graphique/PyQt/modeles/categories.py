import sqlite3
import sys
sys.path.append("../technique/cryptage/")
sys.path.append("../classes/")

from cryptage_symetrique import AESCipher
from requetes import *

# comment gérer l'accessibilité des classes/attributs/méthode
class categorie(object):
	self.nomTable
	self.key = None

	"""docstring for categorie"""
	def __init__(self, nomTable, key, categorie):
		self.nomTable = nomTable
		self.key = key
		self.categorie = self.crypter(categorie)
		
	def crypter(self, categorie):
		cipher = AESCipher(key=self.key)
		return cipher.encrypt(categorie)

	def decrypter(self):
		cipher = AESCipher(key=self.key)
		return cipher.decrypt(self.categorie)

	def save(self):
		requete = "INSERT INTO categories_"+self.nomTable+" categorie VALUES(?)"
		bdd_exec(requete, (self.categorie,))