import sqlite3

fichierDonnees = "maBaseDeDonnees.sq3"

conn = sqlite3.connect(fichierDonnees)
cur = conn.cursor()

# SUPPRIMER ET RECREEER LA BDD
"""
cur.execute ("DROP TABLE mails")
cur.execute ("CREATE TABLE mails (expéditeur TEXT, destinataire TEXT, objet TEXT, contenu TEXT, date TEXT)")
"""

# INSERER UNE NOUVELLE LIGNE

cur.execute ("INSERT INTO mails (expéditeur,destinataire,objet, contenu, date) VALUES('machintttt@lequipe.fr','FranckLopez@lol.fr', 'blabla', 'loret ipsum', '01/01/2016') ")


# COMMIT
conn.commit()

# TRANSFORMATION EN TABLEAU
"""
cur.execute("SELECT * FROM mails")
print(cur.fetchall())
"""

cur.close()
conn.close()

# POUR SE RECONNECTER PLUS TARD A LA BDD EXISTANTE
"""
import sqlite3
conn = sqlite3.connect("maBaseDeDonnees.sq3") 
cur = conn.cursor()
"""
