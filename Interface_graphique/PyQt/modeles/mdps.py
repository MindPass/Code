import sqlite3
import sys
sys.path.append("../cryptage/")
sys.path.append("../classes/")

from cryptage_symetrique import AESCipher
from requetes import *

# comment gérer l'accessibilité des classes/attributs/méthode
class password(object):

	"""docstring for mdp"""
	def __init__(self, nomTable, key, password):
		self.nomTable = nomTable
		self.key = key
		self.password = self.crypt(password)

	def crypt(self, password):
		cipher = AESCipher(key=self.key)
		return cipher.encrypt(password)

	def decrypt(self):
		cipher = AESCipher(key=self.key)
		return cipher.decrypt(self.password)

	def save(self):
		requete = "INSERT INTO mdps_"+self.nomTable+" password VALUES(?)"
		bdd_exec(requete, (self.password,))

# Example
b = password("matable", "skjd", "secretsdslké@/")
print(b.password)
print(b.decrypt())