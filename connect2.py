# -*-coding:utf-8 -*

import os
from oauth2 import *

client_id="287712233618-7qua8pervof64n6g740gi8d0o7ifiu28.apps.googleusercontent.com"
client_secret=raw_input('Rentrer le client secret: ')

<<<<<<< HEAD
auth_code=raw_input("Auth code: ")
=======
auth_code="4/W1_AnPo2m1LygjzOao1faUFDJUYgemMmslfaMvftavI" #modifie par w précaution
>>>>>>> 597466c7ae5b0cec1d4a3653dff1eaef6b0cf2b8

tokens= open("tokens.txt", "a")
 
resultat=str(AuthorizeTokens(client_id, client_secret,auth_code))
tokens.write(resultat)
print(resultat)

tokens.close()

os.system("pause")
