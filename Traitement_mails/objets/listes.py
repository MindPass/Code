# pour les test uniquement
import re

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


liste_mots_cles = []
liste_mots_cles += ['Bienvenue', 'Confirm', 'Registration', 'Welcome', 'Identifiant', 'Activat', 'Verif', 'scrip', 'mot de passe', 'login', 'password', 'Valid']


liste_messageries = []
liste_messageries += ['outlook', 'laposte', 'hotmail', 'gmail', 'yahoo', 'msn', 'zoho', 'aol', 'gmx', 'caramail', 'voila', 'orange.fr', 'mailoo', 'wanadoo']


regex_expediteur = "<?([A-Za-z0-9]+\.[A-Za-z]{1,5})>?$"
exp= "Laposte.net <noreply@laposte.net"

if(re.findall(regex_expediteur, exp)):
    print("salut")