# -*- coding: utf-8 -*-
"""
Created on Wed Dec 02 23:34:39 2015

@author: famille
"""


import os
from oauth2 import *

client_id="287712233618-7qua8pervof64n6g740gi8d0o7ifiu28.apps.googleusercontent.com"
client_secret=input('Rentrer le client secret: ')
refresh_token=input('Rentrer le refresh token: ')

print(RefreshToken(client_id, client_secret, refresh_token))
