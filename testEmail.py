# -*-coding:utf-8 -*

import os
import imaplib
import oauth2

user=raw_input("prefixe gmail: ")
user= user +"@gmail.com"

client_id="287712233618-7qua8pervof64n6g740gi8d0o7ifiu28.apps.googleusercontent.co
client_secret=raw_input('Client secret: ')
access_token=raw_input("Access token: ")

auth_string=oauth2.GenerateOAuth2String(user, access_token, False)
#print(auth_string)
#print(TestImapAuthentication(user, auth_string))

imap_conn = imaplib.IMAP4_SSL('imap.gmail.com')
imap_conn.debug = 4
imap_conn.authenticate('XOAUTH2', lambda x: auth_string)
imap_conn.select('INBOX')

result, data = imap_conn.search(None, "ALL")

ids = data[0] # data is a list.
id_list = ids.split() # ids is a space separated string
latest_email_id = id_list[-1] # get the latest
 
result, data = imap_conn.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
 
raw_email = data[0][1] # here's the body, which is raw text of the whole email
# including headers and alternate payloads

print(raw_email)
