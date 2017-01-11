# -*-coding:utf-8 -*

import os
from oauth2 import *

client_id="287712233618-7qua8pervof64n6g740gi8d0o7ifiu28.apps.googleusercontent.com"
#client_secret=raw_input('Rentrer le client secret: ')

client_secret ="iXsCL1-rYN_D9R6RCc6mUmln"
#auth_code=raw_input("Auth code: ")
auth_code="4/G9VdvC6trIxSdF9DmLZuCTq8-sTskXgO9ItzQ2yUx5w"
tokens= open("tokens.txt", "a")
 
resultat=str(AuthorizeTokens(client_id, client_secret,auth_code))
tokens.write(resultat)
#print(resultat)

tokens.close()

os.system("pause")
