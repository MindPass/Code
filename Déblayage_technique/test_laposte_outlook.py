# -*- coding: utf-8 -*-
import imaplib, getpass

#user=input('entrez le pseudo: ')+"@outlook.com"
user=input('entrez le pseudo: ')+"@laposte.net"
mdp=input('Entrez le mdp: ') # à garder pendant le développement
#mdp=getpass.getpass('Entrez le mdp: ') # pour cacher le mdp lors de la saisie

#imap_conn = imaplib.IMAP4_SSL('imap-mail.outlook.com')
imap_conn = imaplib.IMAP4_SSL('imap.laposte.net')
imap_conn.debug = 4
imap_conn.login(user,mdp)
dansInbox=imap_conn.select('INBOX')

result, data = imap_conn.search(None, "ALL")
ids = data[0] # data is a list.
listeMailsInbox = ids.split() # ids is a space separated string
latest_email_id = listeMailsInbox[16] # get the 17th
result, data = imap_conn.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID

nombreMailsInbox = len(listeMailsInbox)

raw_email = data[0][1].decode('utf-8') # .decode('utf-8') for python 3.x compatibility (bytes -> str)

imap_conn.close()
imap_conn.logout()

#email = open("outlook.txt", "w")
email = open("laposte.txt", "w")
email.write(raw_email)
email.close()

print( "Le nombre de messages est : " + str(nombreMailsInbox) )
