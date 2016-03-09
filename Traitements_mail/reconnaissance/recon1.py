# -*- coding: utf-8 -*-

import sqlite3 as sq3



mailist_cache=[]
con = sq3.connect('test.sq3')

with con:    
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM mindpasstest_laposte")

    rows = cur.fetchall()

    for row in rows:
        mailist_cache.append(row)

