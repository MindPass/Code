
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
import re


def print_(arg):
    """
    Args:
        arg: la valeur à afficher

    Returns: la valeur à afficher ainsi qu'une série de '-', afin d'espacer l'affichage

    """
    print(arg)
    print("-------------------------------------")

def creation_tables():
    conn = sqlite3.connect('../bdd.sq3')
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS sites_reconnus (adresse_mail TEXT , site_web TEXT, identifiant TEXT,"
                " mdp TEXT, categorie TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS mdps (mdp TEXT PRIMARY KEY)")
    cur.execute("CREATE TABLE IF NOT EXISTS categories (nom_categorie TEXT PRIMARY KEY)")


    cur.execute("SELECT DISTINCT expediteur FROM mindpasstest_laposte")
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

creation_tables()
