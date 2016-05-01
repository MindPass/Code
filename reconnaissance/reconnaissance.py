# -*- coding: utf-8 -*-

import sqlite3 as sq3
import listes as li
from requetes import *
import re

output = "output.sq3"
conn = sq3.connect(output)
curr = conn.cursor()
curr.execute ("CREATE TABLE IF NOT EXISTS expediteurs (expediteur TEXT UNIQUE, PRIMARY KEY ('expediteur'))")


requete = "SELECT DISTINCT expediteur FROM mindpasstest_laposte WHERE sujet LIKE "
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
request= "INSERT OR IGNORE INTO expediteurs (expediteur) VALUES "
for i in range (len(site)-1):
    request+="(?)," 
request+= "(?)"

    
curr.execute (request , liste_site)

# 
conn.commit()
curr.close()
conn.close()






