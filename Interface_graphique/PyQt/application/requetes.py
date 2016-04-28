import sqlite3
bdd = "../../../Traitement_mails/bdd.sq3"

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

