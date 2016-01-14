# coding: utf8
import imaplib, urllib.parse, re
from email.parser import Parser
from email.parser import FeedParser

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

imap_conn.close()
imap_conn.logout()

#http://stackoverflow.com/questions/4040074/python-email-encoding-problem
f = FeedParser()
f.feed(raw_email)
rootMessage = f.close()

corps=rootMessage.get_payload(0).get_payload(decode=True).decode('utf-8')
# Récupérer le corps du mail en plain/text bien décodé

open("laposte.txt","w").close()
email = open("laposte.txt", "w")
email.write(raw_email)
email.close()

print(mail['From'])

""" méthode Alex """
subject=mail['Subject']
for i in range(len(subject)):
    if subject[i] == "=":
        subject = subject[:i] + "%" + subject[i+1:]
    elif subject[i] == "_":
        subject = subject[:i] + " " + subject[i+1:]
# suppression des entêtes de merde avec une regexp
subject = re.sub('(\n)*\%\?(UTF|utf)\-8\?(Q|B|q|b)\? *', '', subject)
subject = re.sub('\?\%(\r\n)*', '', subject)
subject=urllib.parse.unquote(subject) 
print(subject) # <<<mail['Subject']>>> modifié avec le bon décodage et sans superflu
""" fin méthode Alex """

print(corps)
print(mail['Date'])

#print( "Le nombre de messages est : " + str(nombreMailsInbox) )