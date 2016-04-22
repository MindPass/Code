import sqlite3
bdd = "../../../Traitement_mails/bdd.sq3"

def bdd_update(table, champs, where, valeurs): 
	""" champs est un tuple, table et where des strings, valeurs un tuple 
	valeurs contiendra les valeurs à modifier ainsi que la condition du where
	en dernier élément. Ex:
	UPDATE sites_reconnus SET identifiant=allo, categorie=crunch WHERE rowid=3
	--> bdd_update("sites_reconnus",("identifiant","categorie"), "rowid", ('allo', 'crunch', 3))
	"""

	conn = sqlite3.connect(bdd)
	cur = conn.cursor()
	requete = "UPDATE "+table+" SET "

	for champ in champs:
		requete = requete + champ +"=? "

	requete = requete + "WHERE " + where + "=? "
	cur.execute(requete , valeurs)
	conn.commit()
	cur.close()
	conn.close()
