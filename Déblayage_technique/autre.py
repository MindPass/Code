# -*- coding: utf-8 -*-
"""
Created on Wed Dec 02 22:46:00 2015

@author: famille
"""

import imaplib

user="mindpasstest@gmail.com"
mdp="vervoort59"

print
imap_conn = imaplib.IMAP4_SSL('imap.gmail.com')
imap_conn.debug = 4
imap_conn.login(user,mdp)
imap_conn.select('INBOX')
