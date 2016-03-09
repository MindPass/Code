# -*- coding: utf-8 -*-

import sqlite3 as sq3

output = "output.sq3"
conn = sq3.connect(output)
curr = conn.cursor()
curr.execute ("CREATE TABLE IF NOT EXISTS mails (id TEXT, login TEXT, pass TEXT, category TEXT)")

mailist_cache=[]
con = sq3.connect('test.sq3')

with con:    
    
    cur = con.cursor()    
    cur.execute("SELECT id, contenu FROM mindpasstest_laposte WHERE contenu LIKE '%login%' OR contenu LIKE '%password%';")

    rows = cur.fetchall()

    i=0
    for row in rows:
        mailist_cache.append(row)
        curr.execute("SELECT id FROM mails")
        tab=curr.fetchall()
        liste_id=[]
        for element in tab:
            liste_id.append(element[0])
        if(mailist_cache[i][0] not in liste_id):
            curr.execute("INSERT INTO mails (id, login, pass, category) VALUES(?,?,?,?)",(mailist_cache[i][0], mailist_cache[i][1], mailist_cache[i][0], mailist_cache[i][0]))
        i+=1



# ENREGISTREMENT
conn.commit()
# FERMETURE
cur.close()
conn.close()
