# -*- coding: utf-8 -*-

import re
from librairie import *
from requetes import *
import listes
# pour le cryptage
import hashlib
import Crypto


def isMailInscription(exp, sujet):
	# email_liste = [id_email, expediteur, sujet, corps, date]
	l= listes.liste_mots_cles
	l2=listes.liste_messageries
	b = False
	for mot_cle in l:
		if(re.findall(mot_cle, sujet)):
			b = True
	for messagerie in l2:
		if(re.findall(messagerie, exp)):
			b= False

	return b


bdd="../bdd.sq3"
conn = sqlite3.connect(bdd)
cur = conn.cursor()

user_email =  "mindpasstest@laposte.net"
mdp = "Verv00rt"
# à garder pendant le développement

mdpb=bytes(mdp, 'utf-8')
mdp_hash = hashlib.sha224(mdpb).hexdigest()

l = user_email.split('@') 

l2 = l[1].split(".")

nom_table = l[0]
for element in l2:
    nom_table += "_"+element


# Creation de la table CONNEXIONS
requete = "CREATE TABLE IF NOT EXISTS CONNEXIONS (adresse_mail TEXT UNIQUE, mdp_hash TEXT, last_id INT, PRIMARY KEY(adresse_mail))"
cur.execute(requete)
conn.commit()

# creation de sites_reconnus_nom_table
requete ="CREATE TABLE IF NOT EXISTS sites_reconnus_"+nom_table+""" (site_web TEXT UNIQUE, identifiant TEXT, 
			mdp TEXT, categorie TEXT, PRIMARY KEY(site_web))"""

cur.execute(requete)
conn.commit()


tableExterne = TableExterne('imap.laposte.net', user_email, mdp)
tableExterne.connexionMail()

liste_id = tableExterne.liste_id()
last_id=0
new_last_id= len(liste_id)

try:
	requete ="INSERT INTO CONNEXIONS VALUES(?, ?, ?)"
	cur.execute(requete, (user_email, mdp_hash, new_last_id))
	conn.commit()
except:
	# Si l'insertion échoue, alors adresse est déjà enregistré et on enregistre le last_id
	requete="SELECT last_id FROM CONNEXIONS WHERE adresse_mail=?"
	cur.execute(requete, (user_email,))
	last_id = toliste(cur.fetchall())[0]

	requete = "UPDATE CONNEXIONS SET last_id=? WHERE adresse_mail=?"
	cur.execute(requete,(new_last_id, user_email))
	conn.commit()

nouveaux_mails = new_last_id-last_id
print("Nouveaux mails: "+str(nouveaux_mails))


requete = "SELECT site_web FROM sites_reconnus_"+nom_table
cur.execute(requete)
# liste des sites déjà enregistrés
site_enregistres = toliste(cur.fetchall())

regex_expediteur = "<?([A-Za-z0-9]+\.[A-Za-z]{1,5})>?$"


if(nouveaux_mails):
	# exp et sujet des derniers mails
	liste_exp_sujet= tableExterne.get_exp_sujet(liste_id[last_id:])

	for element in liste_exp_sujet:
		exp, sujet = element
		recherche = re.findall(regex_expediteur, exp)
		if(recherche):
			site= recherche[0]

		if(recherche and site not in site_enregistres):
			if(isMailInscription(exp, sujet)):
				try:
					requete = "INSERT INTO sites_reconnus_"+nom_table+" (site_web) VALUES(?)"
					cur.execute(requete, (site,) )
					site_enregistres.append(site)
					print(site_enregistres)
				except Exception as e:
					print(e)
					print("Probleme d'insertion, last_id:"+str(last_id)+" new_last_id:"+str(new_last_id))



conn.commit()
tableExterne.close()
cur.close()
conn.close()



