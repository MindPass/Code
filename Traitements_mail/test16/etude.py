# -*- coding: utf-8 -*-

import imaplib
import re
from email.parser import FeedParser
import quopri

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

print("Nombre de mail:%s" % nombreMailsInbox)

for k in range(nombreMailsInbox):
    email_id = listeMailsInbox[k]
    result, data = imap_conn.fetch(email_id, "(RFC822)")
    raw_email = data[0][1].decode('utf-8')
    raw_email_qpri = quopri.decodestring(data[0][1])
    id_message = email_id.decode('utf-8')
    print(id_message)
    encodages = re.findall(r'Content-Transfer-Encoding:'
                           r'\s[a-zA-Z0-9-]+|charset[=:][a-zA-Z0-9-]+', raw_email)
    print(encodages)




    f = FeedParser()
    f.feed(raw_email)
    rootMessage = f.close()

    fichier_mail = open('Etude/test'+str(k)+'.html', 'w')
    fichier_mail.write(raw_email)
    fichier_mail.close()

    """
    if rootMessage.is_multipart():
        corps = quopri.decodestring(rootMessage.get_payload(0))
    else:
        corps = quopri.decodestring(rootMessage.get_payload())

    fichier_mail = open('Etude/test'+str(k)+'.html', 'a')
    fichier_mail.write(corps)
    fichier_mail.close()
    """


imap_conn.close()
imap_conn.logout()
