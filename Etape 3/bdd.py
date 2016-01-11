import sqlite3

fichierDonnees = "mabasededonnées.sq3"

conn = sqlite3.connect(fichierDonnees)

cur = conn.cursor()

cur.execute ("DROP TABLE mails")
cur.execute ("CREATE TABLE mails (expéditeur TEXT, destinataire TEXT, objet TEXT, contenu TEXT, date TEXT)")

# INSERER UNE NOUVELLE LIGNE
cur.execute ("INSERT INTO mails (expéditeur,destinataire,objet, contenu, date) VALUES('machintttt@lequipe.fr','FranckLopez@lol.fr', 'blabla', 'loret ipsum', '01/01/2016') ")

conn.commit()


cur.execute("SELECT * FROM mails")
print(cur.fetchall()[3])

cur.close()
conn.close()

# Pour se reconnecter à la base ensuite
"""
import sqlite3
conn = sqlite3.connect("E:/python3/essais/bd_test.sq3") 
cur = conn.cursor()
"""