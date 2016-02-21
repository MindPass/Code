# -*- coding: utf-8 -*-


import imaplib, urllib.parse, re, sqlite3
from email.parser import FeedParser

#user=input('entrez le pseudo: ')+"@outlook.com"
user=input('entrez le pseudo: ')+"@laposte.net"
mdp=input('Entrez le mdp: ') # à garder pendant le développement

# OUVERTURE BDD
fichierDonnees = "maBaseDeDonneesTEST16.sq3"
conn = sqlite3.connect(fichierDonnees)
cur = conn.cursor()
cur.execute ("CREATE TABLE IF NOT EXISTS mails (id TEXT, expediteur TEXT, sujet TEXT, contenu TEXT, date TEXT)")

# RECUPERATION DES ID
cur.execute("SELECT id FROM mails")
tab=cur.fetchall()
liste_id=[]
for element in tab:
    liste_id.append(element[0])

#imap_conn = imaplib.IMAP4_SSL('imap-mail.outlook.com')
imap_conn = imaplib.IMAP4_SSL('imap.laposte.net')
imap_conn.debug = 4
imap_conn.login(user,mdp)
imap_conn.select('INBOX') #renvoie ('OK', b'nombredemaildanslaboite')



result, data = imap_conn.search(None, "ALL") # result vaut 'OK' si la requête a aboutie
ids = data[0] # data est une liste à un élément, contenant les id des mails
listeMailsInbox = ids.split() # ids est une string d'id séparés par un espace
nombreMailsInbox = len(listeMailsInbox)


print("Nombre de mail:%s" % nombreMailsInbox)

k=16 # cas problématique

latest_email_id = listeMailsInbox[k]
id_message=latest_email_id.decode('utf-8')

#Vérification que ce mail n'a pas déjà été enregistré
if(id_message not in liste_id):
    result, data = imap_conn.fetch(latest_email_id, "(RFC822)") 
    # fetch the email body (RFC822) for the given ID
    
    raw_email = data[0][1].decode('utf-8')
    # .decode('utf-8') for python 3.x compatibility (bytes -> str)
    
    #http://stackoverflow.com/questions/4040074/python-email-encoding-problem
    f = FeedParser()
    f.feed(raw_email)
    rootMessage = f.close()
    
    if(rootMessage.is_multipart()):
        corps=rootMessage.get_payload(0).get_payload(decode=True).decode('utf-8')
        # Récupérer le corps du mail en plain/text bien décodé
    else:
        corps=rootMessage.get_payload(decode=True).decode('utf-8')

    #méthode Alex 
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
    #fin méthode Alex
    
    date =rootMessage.get('Date')
    exp=rootMessage.get('From')
    
    cur.execute("INSERT INTO mails (id, expediteur, sujet, contenu, date) VALUES(?,?,?,?,?)",(id_message, exp, subject, corps, date))
    
    print("From:"+exp+" ID:"+id_message)


# ENREGISTREMENT
conn.commit()
# FERMETURE
cur.close()
conn.close()
imap_conn.close()
imap_conn.logout()
