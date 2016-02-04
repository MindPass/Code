import sqlite3

fichierDonnees = "maBaseDeDonnees.sq3"

conn = sqlite3.connect(fichierDonnees)
cur = conn.cursor()

# SUPPRIMER ET RECREEER LA BDD
cur.execute ("CREATE TABLE IF NOT EXISTS test (id TEXT, expéditeur TEXT, sujet TEXT, contenu TEXT, date TEXT)")

# INSERER UNE NOUVELLE LIGNE

values=[
        ('1','Fraisebook',' Une nouvelle fraise', 'voila', '15 janvier'),
        ('2','Fraisebook',' Une nouvelle fraise', 'voila', '15 janvier'),
        ('3','Fraisebook',' Une nouvelle fraise', 'voila', '15 janvier'),
        ('4','Fraisebook',' Une nouvelle fraise', 'voila', '15 janvier'),
        ('5','Fraisebook',' Une nouvelle fraise', 'voila', '15 janvier'),
        ]
cur.executemany("INSERT INTO mails (id, expéditeur, sujet, contenu, date) VALUES(?,?,?,?,?)", values)


# COMMIT
conn.commit()

# TRANSFORMATION EN TABLEAU

cur.execute("SELECT * FROM mails")
tab=cur.fetchall()



# RECUPERATION DES ID
"""
cur.execute("SELECT id FROM mails")
tab=cur.fetchall()
liste_id=[]
for element in tab:
    liste_id.append(element[0])
print(liste_id)
"""


cur.close()
conn.close()

# POUR SE RECONNECTER PLUS TARD A LA BDD EXISTANTE
"""
import sqlite3
conn = sqlite3.connect("maBaseDeDonnees.sq3") 
cur = conn.cursor()
"""
