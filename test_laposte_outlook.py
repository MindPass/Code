# -*- coding: utf-8 -*-
"""
Created on Thu Dec 03 23:00:10 2015

@author: famille
"""

# -*-coding:utf-8 -*

user=input('entrez le pseudo: ')+"@outlook.com"
mdp=input('Entrez le mdp: ')

imap_conn = imaplib.IMAP4_SSL('imap-mail.outlook.com')
imap_conn.debug = 4
imap_conn.login(user,mdp)
imap_conn.select('INBOX')

result, data = imap_conn.search(None, "ALL")
ids = data[0] # data is a list.
id_list = ids.split() # ids is a space separated string
latest_email_id = id_list[-1] # get the latest
result, data = imap_conn.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID

raw_email = data[0][1] # here's the body, which is raw text of the whole email
# including headers and alternate payloads

laposte= open("laposte.txt", "a")
laposte.write(raw_email)
laposte.close()


print raw_email
