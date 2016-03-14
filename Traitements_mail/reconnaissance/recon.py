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

cur.execute("CREATE TABLE IF NOT EXISTS sites_reconnus (id INT, mail_adress TEXT, website TEXT)")

cur.execute("SELECT DISTINCT expediteur FROM mindpasstest_laposte")
tableau = cur.fetchall()

liste_exp = []
for champs in tableau:
    liste_exp.append(champs[0])

print_(liste_exp)

conn.commit()
cur.close()
conn.close()
