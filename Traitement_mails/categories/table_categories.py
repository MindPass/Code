
import sqlite3

conn = sqlite3.connect('../bdd.sq3')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS categories (nom_categorie TEXT, PRIMARY KEY (nom_categorie))")

# ENREGISTREMENT
conn.commit()
# FERMETURE
cur.close()
conn.close()
