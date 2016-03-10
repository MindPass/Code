# -*- coding: utf-8 -*-


import imaplib
import quopri
from email.parser import Parser
import email
import html

# user=input('entrez le pseudo: ')+"@outlook.com"
# user = input('entrez le pseudo: ') + "@laposte.net"
# mdp = input('Entrez le mdp: ')  # à garder pendant le développement
user = "mindpasstest@laposte.net"
mdp = "Verv00rt"

# imap_conn = imaplib.IMAP4_SSL('imap-mail.outlook.com')
imap_conn = imaplib.IMAP4_SSL('imap.laposte.net')
imap_conn.debug = 4
imap_conn.login(user, mdp)
imap_conn.select('INBOX')  # renvoie ('OK', b'nombredemaildanslaboite')

result, data = imap_conn.search(None, "ALL")  # result vaut 'OK' si la requête a aboutie
ids = data[0]  # data est une liste à un élément, contenant les id des mails
listeMailsInbox = ids.split()  # ids est une string d'id séparés par un espace
nombreMailsInbox = len(listeMailsInbox)

#print("Nombre de mail:%s" % nombreMailsInbox)

k = 16  # cas problématique

latest_email_id = listeMailsInbox[k]
id_message = latest_email_id.decode('utf-8')

# Vérification que ce mail n'a pas déjà été enregistré

result, data = imap_conn.fetch(latest_email_id, "(RFC822)")
# fetch the email body (RFC822) for the given ID

raw_email = data[0][1]
str_email = email.message_from_bytes(raw_email)


if (str_email.is_multipart()):
	for part in str_email.get_payload():
		charset = part.get_content_charset()
		fichier_print=part.get_payload(decode=True).decode(charset)
else:
	charset = str_email.get_content_charset()
	fichier_print=str_email.get_payload(decode=True).decode(charset)

"""
raw_email_qpri = quopri.decodestring(raw_email)
chaine =  raw_email_qpri.decode('utf-8','replace')
"""
print(charset)


# .decode('utf-8') for python 3.x compatibility (bytes -> str)
# http://stackoverflow.com/questions/4040074/python-email-encoding-problem

fichier_mail = open('test16.html', 'w')
fichier_mail.write(fichier_print)
fichier_mail.close()


imap_conn.close()
imap_conn.logout()
