# -*-coding:utf-8 -*

import os
from oauth2 import *

client_id="287712233618-7qua8pervof64n6g740gi8d0o7ifiu28.apps.googleusercontent.com"


fichier = open("fichier.txt", "a") # Argh j'ai tout écrasé !

url=GeneratePermissionUrl(client_id, scope='https://mail.google.com/')
fichier.write(url)
print(url)

fichier.close()

os.system("pause")
