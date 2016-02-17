

class Personne(object):

    def __init__(self, nom, prenom):
        """

        Returns:
            object:
        """
        self.nom = nom
        self.prenom = prenom

    def destruct(self):
        l = [item for item in self.__dict__]
        for attribut in l:
            self.__delattr__(attribut)

l = []
p = Personne("df", "dkjs")
l.append(p)
print(l)
