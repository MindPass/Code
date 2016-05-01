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

output = "output.sq3"
conn = sq3.connect(output)
curr = conn.cursor()
curr.execute ("CREATE TABLE IF NOT EXISTS mails (id TEXT,exp TEXT ,login TEXT, pass TEXT, category TEXT)")

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
            curr.execute("INSERT INTO mails (id, exp, login, pass, category) VALUES(?,?,?,?,?)",(mailist_cache[i][0], "wasabi", mailist_cache[i][1], mailist_cache[i][0], mailist_cache[i][0]))
        i+=1



# ENREGISTREMENT
conn.commit()
# FERMETURE
cur.close()
conn.close()
