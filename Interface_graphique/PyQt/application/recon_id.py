import sqlite3
import re
import listes as li
from requetes import *
bdd = "../../../Traitement_mails/bdd.sq3"


def print_(arg):
    """
    Args:
        arg: la valeur à afficher

    Returns: la valeur à afficher ainsi qu'une série de '-', afin d'espacer l'affichage

    """
    print(arg)
    print("-------------------------------------")

def creation_tables(nom_table, identifiant):
    conn = sqlite3.connect(bdd)
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS sites_reconnus_"+nom_table+" (adresse_mail TEXT , site_web TEXT UNIQUE, identifiant TEXT,"
                " mdp TEXT, categorie TEXT, PRIMARY KEY(site_web))")
    cur.execute("CREATE TABLE IF NOT EXISTS mdps_"+nom_table+" (mdp TEXT PRIMARY KEY)")
    cur.execute("CREATE TABLE IF NOT EXISTS categories_"+nom_table+" (nom_categorie TEXT PRIMARY KEY)")
    
    requete = "SELECT DISTINCT expediteur, contenu, rowid FROM " + nom_table + " WHERE sujet LIKE "
    for i in range(len(li.liste_mots_cles)-1):
        requete+= "'%" + li.liste_mots_cles[i] + "%' OR sujet LIKE "
    requete+= "'%" + li.liste_mots_cles[len(li.liste_mots_cles)-1] + "%'"
    
    for i in range(len(li.liste_messageries)):
        requete+= " AND expediteur NOT LIKE '%" + li.liste_messageries[i] + "%'"

    rows=bdd_select(requete)
    regex_mail= identifiant
    
    rowid_mails= []
    for i in range(len(rows)):
        if re.findall(regex_mail, rows[i][1]):
            rowid_mails.append(rows[i][0])
    print(rowid_mails)
    

    valeurs=toliste(rows)
   

    sites=[]
    regex_expediteur = "<?([A-Za-z0-9]+\.[A-Za-z]{1,5})>?$"

    for i in range(len(valeurs)):
        sites+= re.findall(regex_expediteur, valeurs[i])
    
    site= set(sites)
    liste_site= list(site)
    print(liste_site)


    request= "INSERT OR IGNORE INTO sites_reconnus_"+nom_table+" (site_web, identifiant) VALUES "
    for i in range (len(liste_site)-1):
        request+="(?,?)," 
    request+= "(?,?)"
    
    valeurs2=[]
    for i in range(len(liste_site)):
        valeurs2+= [""]

    for i in range(len(rowid_mails)):
        site=re.findall(regex_expediteur, rowid_mails[i])
        for j in range(len(liste_site)):
            if site[0]==liste_site[j]:
                valeurs2[j]= identifiant
    print(valeurs2)
    
    val=[]
    for i in range(len(liste_site)):
        val+=[liste_site[i], valeurs2[i]]
    print(val)

    
    cur.execute (request , val)


    conn.commit()
    cur.close()
    conn.close()
