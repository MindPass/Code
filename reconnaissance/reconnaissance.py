# -*- coding: utf-8 -*-

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

import sqlite3 as sq3
import listes as li
from requetes import *
import re

conn = sq3.connect("../Traitement_mails/bdd.sq3")
curr = conn.cursor()


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
request= "INSERT OR IGNORE INTO sites_reconnus (expediteur) VALUES "
for i in range (len(site)-1):
    request+="(?)," 
request+= "(?)"

    
curr.execute (request , liste_site)

# 
conn.commit()
curr.close()
conn.close()






