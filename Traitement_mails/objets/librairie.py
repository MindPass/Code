# -*- coding: utf-8 -*-

"""<Mindpass is a intelligent password manager written in Python3
    that checks your mailbox for logins and passwords that you do not remember.>
    Copyright (C) <2016>  <Cantaluppi Thibaut, Garchery Martial, Domain Alexandre, Boulmane Yassine>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>."""



import imaplib
import sqlite3
import email


def print_(arg):
    """
    Args:
        arg: la valeur à afficher

    Returns: la valeur à afficher ainsi qu'une série de '-', afin d'espacer l'affichage

    """
    print(arg)
    print("-------------------------------------")


class Table(object):
    """docstring for Table
    Définit une table dans la bdd, destinée à contenir les mails d'une adresse donnée; classe
    utile si l'utilisateur nous en fournit plusieurs.
    Attributs,

    D'instance:
    -bdd est le fichier .sq3 contenant les données.
    -name, qui peut être l'adresse donnée.
    -conn et cur, sont des variables permettant de se conecter à la bdd en sqlite (.sq3).
    """

    def __init__(self, bdd, name):
        """Constructeur
        On créé la table name si elle n'existe pas
        """

        self.name = name
        self.conn = sqlite3.connect(bdd)
        self.cur = self.conn.cursor()
        cmd = "CREATE TABLE IF NOT EXISTS %s (id INT, expediteur TEXT, sujet TEXT, contenu TEXT, date TEXT)" % name
        self.cur.execute(cmd)

    # se prémunir d'une injection SQL reste à faire

    def add_mail(self, arg):
        """Prend une liste, tuple ou dictionnaire en paramètre.

        """
        if isinstance(arg, list) or isinstance(arg, tuple):
            self.cur.execute("INSERT INTO " + self.name + " (id, expediteur, sujet, contenu, date) VALUES(?,?,?,?,?)",
                             (arg[0], arg[1], arg[2], arg[3], arg[4]))
        elif isinstance(arg, dict):
            self.cur.execute("INSERT INTO " + self.name + " (id, expediteur, sujet, contenu, date) VALUES(?,?,?,?,?)",
                             (arg["id"], arg["expediteur"], arg["sujet"], arg["contenu"], arg["date"]))
        else:
            print("L'argument passé à add_mail n'est pas du bon type")

    def liste_id(self):
        self.cur.execute("SELECT id FROM " + self.name)
        tab = self.cur.fetchall()
        liste_id = []
        for element in tab:
            liste_id.append(element[0])
        return liste_id

    def save(self):
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()


class TableExterne(object):
    """docstring for TableExterne


    """

    def __init__(self, connexion, user, mdp):
        self.connexion = connexion
        self.user = user
        self.mdp = mdp

        """
        self.imap_conn = imaplib.IMAP4_SSL(connexion)
        self.imap_conn.debug = 4
        self.imap_conn.login(user, mdp)
        self.imap_conn.select('INBOX')  # renvoie ('OK', b'nombredemaildanslaboite')
        """

    def test_connexion(self, connexion, user, mdp):
        imap_conn = imaplib.IMAP4_SSL(connexion)
        imap_conn.debug = 4
        try:
            imap_conn.login(user, mdp)
            return True
        except Exception:
            return False

    def connexionMail(self):
        self.imap_conn = imaplib.IMAP4_SSL(self.connexion)
        self.imap_conn.debug = 4
        self.imap_conn.login(self.user, self.mdp)
        self.imap_conn.select('INBOX')  # renvoie ('OK', b'nombredemaildanslaboite')

    def liste_id(self):
        result, data = self.imap_conn.search(None, "ALL")  # result vaut 'OK' si la requête a aboutie
        ids = data[0]  # data est une liste à un élément, contenant les id des mails
        liste_mails_inbox = ids.split()

        for k in range(len(liste_mails_inbox)):
            if type(liste_mails_inbox[k]) == "bytes":
                liste_mails_inbox[k] = liste_mails_inbox[k].decode('utf-8')
                # ids est une string d'id séparés par un espace
        return liste_mails_inbox

    def raw_email(self, email_id):
        result, data = self.imap_conn.fetch(email_id, "(RFC822)")
        # fetch the email body (RFC822) for the given ID
        raw_email = data[0][1]
        return raw_email

    def email_as_list(self, email_id):
        raw_email = self.raw_email(email_id)
        str_email = email.message_from_bytes(raw_email)  # str_email est  de type message

        format_mail_voulu = "html"  # mettre "plain" si on veut le recupérer en text/plain, html sinon

        if str_email.is_multipart():
            alrdy_saved_in_format = False
            for part in str_email.get_payload():
                if not alrdy_saved_in_format:
                    charset = part.get_content_charset()
                    try:
                        corps = part.get_payload(decode=True).decode(charset, 'replace')
                    except AttributeError as e:
                        # si decode n'a pas marché, alors part est multipart: on recommence
                        for sub_part in part.get_payload():
                            if sub_part.get_content_type() == 'text/plain':
                                charset = sub_part.get_content_charset()
                                corps = sub_part.get_payload(decode=True).decode(charset, 'replace')
                                break
                            elif sub_part.get_content_type() == 'text/html':
                                charset = sub_part.get_content_charset()
                                corps = sub_part.get_payload(decode=True).decode(charset, 'replace')

                if part.get_content_type() == ("text/" + format_mail_voulu):
                    alrdy_saved_in_format = True
        else:
            charset = str_email.get_content_charset()
            try:
                corps = str_email.get_payload(decode=True).decode(charset)
            except AttributeError:
                print_("NON multipart .decode(charset) n'a pas fonctionné")

        ### SUJET
        mime_subject = str_email.get('Subject')
        # sujet du mail, possiblement encodé par le protocole MIME
        subject_encoded, encoding = email.header.decode_header(mime_subject)[0]
        # liste contenant un seul tuple  ('sujet', None) si sujet non encodé

        if encoding is None:
            subject = subject_encoded
        else:
            subject = subject_encoded.decode(encoding)
        ##

        ### EXPEDITEUR
        mime_exp = str_email.get('From')

        if len(email.header.decode_header(mime_exp)) != 1:
            exp = ""
            for element in email.header.decode_header(mime_exp):
                exp_encoded, encoding = element
                if encoding is None:
                    exp += exp_encoded.decode('utf-8')
                else:
                    exp += exp_encoded.decode(encoding)

        else:
            exp_encoded, encoding = email.header.decode_header(mime_exp)[0]
            if encoding is None:
                exp = exp_encoded
            else:
                exp = exp_encoded.decode(encoding)
        ##

        date = str_email.get('Date')
        email_liste = []

        if type(email_id) == "<class 'bytes'>":
            email_id = email_id.decode('utf-8')
        email_liste.extend((email_id, exp, subject, corps, date))

        return email_liste

    def close(self):
        self.imap_conn.close()
        self.imap_conn.logout()
