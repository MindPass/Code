# coding: utf8
import imaplib, urllib.parse, re
from email.parser import Parser, FeedParser

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

latest_email_id = listeMailsInbox[-2] # get the latest
result, data = imap_conn.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID

nombreMailsInbox = len(listeMailsInbox)


raw_email = data[0][1].decode('utf-8')
# .decode('utf-8') for python 3.x compatibility (bytes -> str)
mail = Parser().parsestr(raw_email)

imap_conn.close()
imap_conn.logout()

#http://stackoverflow.com/questions/4040074/python-email-encoding-problem
f = FeedParser()
f.feed(raw_email)
rootMessage = f.close()

corps=rootMessage.get_payload(0).get_payload(decode=True).decode('utf-8')
# Récupérer le corps du mail en plain/text bien décodé

""" si on veut tester dans un txt
open("laposte.txt","w").close()
email = open("laposte.txt", "w")
email.write(raw_email)
email.close()
"""

""" méthode Alex """
# suppression des entêtes de merde avec une regexp
subject=rootMessage.get('Subject')
for i in range(len(subject)):
    if subject[i] == "=":
        subject = subject[:i] + "%" + subject[i+1:]
    elif subject[i] == "_":
         subject = subject[:i] + " " + subject[i+1:]
subject = re.sub('(\n)*\%\?(UTF|utf)\-8\?(Q|B|q|b)\? *', '', subject)
subject = re.sub('\?\%(\r\n)*', '', subject)
subject=urllib.parse.unquote(subject) 
"""fin méthode Alex """

print (subject)
print (rootMessage.get('From'))
print (rootMessage.get('Date'))
print (corps)


#print( "Le nombre de messages est : " + str(nombreMailsInbox) )