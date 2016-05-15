
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



import sqlite3
bdd = "../bdd.sq3"

# REQUETES permettant d'éviter les répétitions d'ouvertures et fermetures de la bdd
def bdd_open():
	conn = sqlite3.connect(bdd)
	cur = conn.cursor()

def bdd_save():
	conn.commit()

def bdd_close():
	cur.close()
	conn.close()

def bdd_exec(requete, valeurs=None): 
	if valeurs:
		cur.execute(requete, valeurs)
	else:
		cur.execute(requete)
## REQUETES permettant d'éviter les répétitions d'ouvertures et fermetures de la bdd



# REQUETES intuitives
def bdd_update(requete, valeurs): 
	conn = sqlite3.connect(bdd)
	cur = conn.cursor()
	cur.execute(requete, valeurs)
	conn.commit()
	cur.close()
	conn.close()

def bdd_select(requete, valeurs=None):
	conn = sqlite3.connect(bdd)
	cur = conn.cursor()

	if valeurs:
		cur.execute(requete, valeurs)
	else:
		cur.execute(requete)

	tab = cur.fetchall()
	conn.commit()
	cur.close()
	conn.close()

	return(tab)


def bdd_insert(requete, valeurs):
	conn = sqlite3.connect(bdd)
	cur = conn.cursor()
	cur.execute(requete, valeurs)
	conn.commit()
	cur.close()
	conn.close()


def bdd_delete(requete, valeurs):
	conn = sqlite3.connect(bdd)
	cur = conn.cursor()
	cur.execute(requete, valeurs)
	conn.commit()
	cur.close()
	conn.close()


# function permettant de transformer le résultat en une liste
def toliste(tab):
	l=[]
	for k in range(len(tab)):
		l.append(tab[k][0])
	return(l)
