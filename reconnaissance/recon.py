import sqlite3
import re


def print_(arg):
    """
    Args:
        arg: la valeur à afficher

    Returns: la valeur à afficher ainsi qu'une série de '-', afin d'espacer l'affichage

    """
    print(arg)
    print("-------------------------------------")


conn = sqlite3.connect('../bdd.sq3')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS sites_reconnus (adresse_mail TEXT PRIMARY KEY, site_web TEXT, identifiant TEXT,"
            " mdp TEXT, categorie TEXT)")

cur.execute("SELECT DISTINCT expediteur FROM mindpasstest_laposte WHERE expediteur NOT LIKE '%outlook%' AND expediteur NOT LIKE '%gmail%' AND expediteur NOT LIKE '%laposte%' AND expediteur NOT LIKE '%yahoo%' AND expediteur NOT LIKE '%hotmail%' AND expediteur NOT LIKE '%zoho%' AND expediteur NOT LIKE '%msn%' AND expediteur NOT LIKE '%aol%' AND expediteur NOT LIKE '%gmx%' AND expediteur NOT LIKE '%caramail%' AND expediteur NOT LIKE '%voila%' AND expediteur NOT LIKE '%orange.fr%' AND expediteur NOT LIKE '%mailoo%' AND expediteur NOT LIKE '%wanadoo%'")
tableau = cur.fetchall()

liste_mail = []
liste_domaines = []
regex_expediteur = "<?([A-Za-z0-9]+@(?:(?:[A-Za-z0-9])*\.)*([A-Za-z0-9]+\.[A-Za-z]{1,5}))>?"

for champs in tableau:
    expediteur = re.findall(regex_expediteur, champs[0])

    mail_temp = expediteur[0][0]
    domaine_temp = "www." + expediteur[0][1]

    if domaine_temp not in liste_domaines:
        cur.execute("INSERT INTO sites_reconnus (adresse_mail, site_web) VALUES(?, ?)", (mail_temp, domaine_temp))
        liste_mail.append(mail_temp)
        liste_domaines.append(domaine_temp)

print_(liste_mail)
print_(liste_domaines)

conn.commit()
cur.close()
conn.close()
