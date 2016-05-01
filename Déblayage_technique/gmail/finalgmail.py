# -*-coding:utf-8 -*

import os
import imaplib
from oauth2 import *



client_id="287712233618-7qua8pervof64n6g740gi8d0o7ifiu28.apps.googleusercontent.com"
client_secret="iXsCL1-rYN_D9R6RCc6mUmln"

url=GeneratePermissionUrl(client_id, scope='https://mail.google.com/')

print(url)

print("Autoriser la recherche dans vos mails.") #Récupérer l'authcode
auth_code="4/G9VdvC6trIxSdF9DmLZuCTq8-sTskXgO9ItzQ2yUx5w"
resultat=str(AuthorizeTokens(client_id, client_secret,auth_code))
""" resultat vaut: {u'access_token': u'ya29.CjHPAvnOH17P3g7UPuacy3vVmaV_spffEzVlEAUWBf6_7ZAAUacdJex3xC7n-Z4qShJ7',
u'token_type': u'Bearer', u'expires_in': 3599,
u'refresh_token': u'1/RHsZXi3nH5o4_CRrVZYvjbXH8f0bQH5XLJ4WGPjJgDg'}"""

#L'access_token n'est valable qu'une heure, il faudra donc utiliser un refresh_token
new_access_token = RefreshToken(client_id, client_secret, refresh_token)
print(new_access_token)
""" new_access_token vaut: {u'access_token': u'ya29.CjHPAsJXZ_uUAYdSiK4t9RXnsZ6LV-G6y0eWDSvwGrzCEVmQEAmtgsYveV5432mXczsd',
u'token_type': u'Bearer', u'expires_in': 3600}"""


client_id="287712233618-7qua8pervof64n6g740gi8d0o7ifiu28.apps.googleusercontent.com"
#access_token=raw_input("Access token: ")
access_token = "ya29.CjHPAvnOH17P3g7UPuacy3vVmaV_spffEzVlEAUWBf6_7ZAAUacdJex3xC7n-Z4qShJ7"

auth_string=oauth2.GenerateOAuth2String(user, access_token, False)
#print(auth_string)
#print(TestImapAuthentication(user, auth_string))

imap_conn = imaplib.IMAP4_SSL('imap.gmail.com')
imap_conn.debug = 4
imap_conn.authenticate('XOAUTH2', lambda x: auth_string)
imap_conn.select('INBOX')


os.system("pause")
