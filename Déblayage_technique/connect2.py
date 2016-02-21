# -*-coding:utf-8 -*

import os
from oauth2 import *

client_id="287712233618-7qua8pervof64n6g740gi8d0o7ifiu28.apps.googleusercontent.com"
client_secret=raw_input('Rentrer le client secret: ')

auth_code=raw_input("Auth code: ")

tokens= open("tokens.txt", "a")
 
resultat=str(AuthorizeTokens(client_id, client_secret,auth_code))
tokens.write(resultat)
print(resultat)

tokens.close()

os.system("pause")
