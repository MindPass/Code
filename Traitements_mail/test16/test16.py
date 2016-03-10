# -*- coding: utf-8 -*-


import imaplib
import email
import codecs

format_mail_voulu = "html"  # mettre "plain" si on veut le recupérer en text/plain, html sinon
id_mail_voulu = 18

def print_(arg):
    """
    Args:
        arg: la valeur à afficher

    Returns: la valeur à afficher ainsi qu'une série de '-', afin d'espacer l'affichage

    """
    print(arg)
    print("-------------------------------------")


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

print_("Nombre de mail:%s" % nombreMailsInbox)

byte_id = listeMailsInbox[id_mail_voulu]
result, data = imap_conn.fetch(byte_id, "(RFC822)")
raw_email = data[0][1]  # en bits
str_email = email.message_from_bytes(raw_email)


print_(str_email.get_all("Subject"))
print_(str_email.get_boundary())

if str_email.is_multipart():
    alrdy_saved_in_format = False
    for part in str_email.get_payload():
        if not alrdy_saved_in_format:
            charset = part.get_content_charset()
            try:
                fichier_print = part.get_payload(decode=True).decode(charset, 'replace')
            except AttributeError:
                print_(".decode(charset) n'a pas fonctionné.")

        if part.get_content_type() == ("text/"+format_mail_voulu):
            alrdy_saved_in_format = True
else:
    charset = str_email.get_content_charset()
    try:
        fichier_print = str_email.get_payload(decode=True).decode(charset)
    except AttributeError:
        print_("NON multipart .decode(charset) n'a pas fonctionné")


print_(str(email.iterators._structure(str_email)))  # structure du mail

print(charset)
if charset == "utf-8":
    charset += "-sig"  # ajout du BOM

file = codecs.open("test16.html", "w", charset)
file.write(fichier_print)
file.close()

imap_conn.close()
imap_conn.logout()
