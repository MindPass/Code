import sqlite3
import re
import listes as li
from requetes import *


def print_(arg):
    """
    Args:
        arg: la valeur à afficher

    Returns: la valeur à afficher ainsi qu'une série de '-', afin d'espacer l'affichage

    """
    print(arg)
    print("-------------------------------------")

def creation_tables(nom_table):
    conn = sqlite3.connect('../../../Traitement_mails/bdd.sq3')
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS sites_reconnus (adresse_mail TEXT , site_web TEXT UNIQUE, identifiant TEXT,"
                " mdp TEXT, categorie TEXT, PRIMARY KEY(site_web))")
    cur.execute("CREATE TABLE IF NOT EXISTS mdps (mdp TEXT PRIMARY KEY)")
    cur.execute("CREATE TABLE IF NOT EXISTS categories (nom_categorie TEXT PRIMARY KEY)")
    
    requete = "SELECT DISTINCT expediteur FROM " + nom_table + " WHERE sujet LIKE "
    for i in range(len(li.liste_mots_cles)-1):
        requete+= "'%" + li.liste_mots_cles[i] + "%' OR sujet LIKE "
    requete+= "'%" + li.liste_mots_cles[len(li.liste_mots_cles)-1] + "%'"
    
    for i in range(len(li.liste_messageries)):
        requete+= " AND expediteur NOT LIKE '%" + li.liste_messageries[i] + "%'"

    rows=bdd_select(requete)
 
    valeurs=[]
    for i in range (len(rows)-1):
        valeurs+= list(rows[i])
   
    valeurs+= list(rows[len(rows)-1])
    print (valeurs)

    sites=[]
    regex_expediteur = "<?([A-Za-z0-9]+\.[A-Za-z]{1,5})>?$"

    for i in range(len(rows)-1):
        sites+= re.findall(regex_expediteur, valeurs[i])
    sites+= re.findall(regex_expediteur, valeurs[len(rows)-1])

    site= set(sites)
    liste_site= list(site)
    print(liste_site)
    request= "INSERT OR IGNORE INTO sites_reconnus (site_web) VALUES "
    for i in range (len(site)-1):
        request+="(?)," 
    request+= "(?)"

    
    cur.execute (request , liste_site)


    conn.commit()
    cur.close()
    conn.close()

creation_tables("mindpasstest_laposte")