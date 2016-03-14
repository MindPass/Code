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


conn = sqlite3.connect('../objets/bdd.sq3')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS sites_reconnus (mail_adress TEXT, website TEXT, PRIMARY KEY (mail_adress))")

cur.execute("SELECT DISTINCT expediteur FROM mindpasstest_laposte")
tableau = cur.fetchall()

liste_exp = []
liste_domaines = []
regex_expediteur = "<?([A-Za-z0-9]+@(?:(?:[A-Za-z0-9])*\.)*([A-Za-z0-9]+\.[A-Za-z]{1,5}))>?"

for champs in tableau:
    expediteur = re.findall(regex_expediteur, champs[0])
    liste_exp.append(expediteur[0][0])
    liste_domaines.append("www." + expediteur[0][1])

print_(liste_exp)
print_(liste_domaines)

conn.commit()
cur.close()
conn.close()
