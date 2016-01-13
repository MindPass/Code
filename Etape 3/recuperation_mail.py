# -*- coding: utf-8 -*-
import imaplib, base64
from email.parser import Parser

#user=input('entrez le pseudo: ')+"@outlook.com"
user=input('entrez le pseudo: ')+"@laposte.net"
mdp=input('Entrez le mdp: ') # à garder pendant le développement


#imap_conn = imaplib.IMAP4_SSL('imap-mail.outlook.com')
imap_conn = imaplib.IMAP4_SSL('imap.laposte.net')
imap_conn.debug = 4
imap_conn.login(user,mdp)
dansInbox=imap_conn.select('INBOX')

result, data = imap_conn.search(None, "ALL")
ids = data[0] # data is a list.
listeMailsInbox = ids.split() # ids is a space separated string
latest_email_id = listeMailsInbox[-1] # get the latest
result, data = imap_conn.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID

nombreMailsInbox = len(listeMailsInbox)

raw_email = data[0][1].decode('utf-8')
# .decode('utf-8') for python 3.x compatibility (bytes -> str)
mail = Parser().parsestr(raw_email)

imap_conn.close()
imap_conn.logout()


open("laposte.txt","w").close()
email = open("laposte.txt", "w")
email.write(raw_email)
email.close()

#print(mail['To'])
#print(mail['From'])

print(base64.decode(mail['Subject']))

print(mail['Content-Type'])

#print(mail['Date'])


"""
print(mail['From'])
print(mail['Subject'])
"""


#print( "Le nombre de messages est : " + str(nombreMailsInbox) )