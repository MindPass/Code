# -*- coding: utf-8 -*-

import sqlite3 as sq3
import listes as li

output = "output.sq3"
conn = sq3.connect(output)
curr = conn.cursor()
curr.execute ("CREATE TABLE IF NOT EXISTS mails (exp TEXT ,login TEXT, pass TEXT, category TEXT)")

mailist_cache=[]
con = sq3.connect('../Traitement_mails/bdd.sq3')

with con:    
    
    cur = con.cursor()   
    cur.execute("SELECT rowid, expediteur, sujet, contenu FROM mindpasstest_laposte  WHERE sujet  LIKE '%Bienvenue%' OR sujet LIKE '%Confirm%' OR sujet LIKE '%Welcome%' OR sujet LIKE '%Identifiant%' OR sujet LIKE '%Activ%' OR sujet LIKE '%Verif%' OR sujet LIKE '%scrip%' OR sujet LIKE '%mot de passe%' OR sujet LIKE '%login%' OR sujet LIKE '%password%';")

    rows = cur.fetchall()

    i=0
    for row in rows:
        mailist_cache.append(row)
        curr.execute("SELECT exp FROM mails")
        tab=curr.fetchall()
        liste_id=[]
        for element in tab:
            liste_id.append(element[0])
        if(mailist_cache[i][0] not in liste_id):
            curr.execute("INSERT INTO mails (exp, login, pass, category) VALUES(?,?,?,?)",(mailist_cache[i][1], mailist_cache[i][1], mailist_cache[i][0], mailist_cache[i][0]))
        i+=1



# ENREGISTREMENT
conn.commit()
# FERMETURE
cur.close()
conn.close()
