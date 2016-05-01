
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
