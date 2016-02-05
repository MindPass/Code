
class Voiture(object):
	"""docstring for Voiture"""
	def __init__(self, roue, marque):
		self.roue = roue
		self.marque=marque

	def rouler(self):
		print("Je roule !")

class Siege(object):
	"""docstring for Siege"""
	def __init__(self, object, matiere):
		self.matiere=matiere
		self.marque = object.marque

	def rouler(self):
		object.rouler()
		
		
		