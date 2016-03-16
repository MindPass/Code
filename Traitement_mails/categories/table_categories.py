
import sqlite3

conn = sqlite3.connect('../bdd.sq3')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS categories (categorie_id INT, nom TEXT, PRIMARY KEY (categorie_id))")



# ENREGISTREMENT
conn.commit()
# FERMETURE
cur.close()
conn.close()
