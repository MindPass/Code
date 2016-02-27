class Polyedre(object):
    """docstring for Equaedre"""

    def __init__(self, nombre):
        self.nombre = nombre


class Rectangle(object):
    """docstring for Rectangle"""

    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur


class Carre(Rectangle, Polyedre):
    """docstring for Carrer"""

    def __init__(self, longueur, largeur, nombre):
        super(Carre, self).__init__(longueur, largeur, nombre)


c = Carre(1,2,3)
print(c.largeur)