# -*- coding: utf-8 -*-


import imaplib
import re
import sqlite3
import html
import urllib.parse
from email.parser import FeedParser

# user=input('entrez le pseudo: ')+"@outlook.com"
# user = input('entrez le pseudo: ') + "@laposte.net"
# mdp = input('Entrez le mdp: ')  # à garder pendant le développement
user = "mindpasstest@laposte.net"
mdp = "Verv00rt"

# OUVERTURE BDD
fichierDonnees = "maBaseDeDonneesTEST16.sq3"
conn = sqlite3.connect(fichierDonnees)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS mails (id TEXT, expediteur TEXT, sujet TEXT, contenu TEXT, date TEXT)")

# RECUPERATION DES ID
cur.execute("SELECT id FROM mails")
tab = cur.fetchall()
liste_id = []
for element in tab:
    liste_id.append(element[0])

# imap_conn = imaplib.IMAP4_SSL('imap-mail.outlook.com')
imap_conn = imaplib.IMAP4_SSL('imap.laposte.net')
imap_conn.debug = 4
imap_conn.login(user, mdp)
imap_conn.select('INBOX')  # renvoie ('OK', b'nombredemaildanslaboite')

result, data = imap_conn.search(None, "ALL")  # result vaut 'OK' si la requête a aboutie
ids = data[0]  # data est une liste à un élément, contenant les id des mails
listeMailsInbox = ids.split()  # ids est une string d'id séparés par un espace
nombreMailsInbox = len(listeMailsInbox)

print("Nombre de mail:%s" % nombreMailsInbox)

k = 13  # cas problématique

latest_email_id = listeMailsInbox[k]
id_message = latest_email_id.decode('utf-8')

# Vérification que ce mail n'a pas déjà été enregistré

result, data = imap_conn.fetch(latest_email_id, "(RFC822)")
# fetch the email body (RFC822) for the given ID


raw_email = data[0][1].decode('utf-8')

# .decode('utf-8') for python 3.x compatibility (bytes -> str)
# http://stackoverflow.com/questions/4040074/python-email-encoding-problem
f = FeedParser()
f.feed(raw_email)
rootMessage = f.close()

if rootMessage.is_multipart():
    try:
        corps = rootMessage.get_payload(0)
    except Exception as e:
        print("Multipart: " + str(e))
        # Récupérer le corps du mail en plain/text bien décodé
else:
    try:
        corps = rootMessage.get_payload()
        if ('text/html' in re.findall(r'text/html', corps)):
            corps = html.unescape(corps)

    except Exception as e:
        print("Non multipart:" + str(e))

fichier_mail = open('test16.html', 'w')
fichier_mail.write(str(corps))
fichier_mail.close()

exp = rootMessage.get('From')
print("From:" + exp + " ID:" + id_message)

enc = rootMessage.get('Content-Transfer-Encoding')

print(enc)

cont = rootMessage.get('Content-Type')
print(cont)

print(id_message)

# ENREGISTREMENT
conn.commit()
# FERMETURE
cur.close()
conn.close()
imap_conn.close()
imap_conn.logout()
