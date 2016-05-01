# -*- coding: utf-8 -*-

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



from Traitement_mails.objets.librairie import *

user_email = input('entrez le pseudo: ') + "@laposte.net"
mdp = input('Entrez le mdp: ')
# à garder pendant le développement

l = user_email.split('@')
l[1] = l[1].split('.')[0]
nom_table = l[0] + '_' + l[1]  # vaut 'pseudo_laposte'


bdd="../bdd.sq3"
table = Table(bdd, nom_table)
tableExterne = TableExterne('imap.laposte.net', user_email, mdp)
fichier_erreurs = open('fichier_erreurs.txt', 'a')

for id_email in tableExterne.liste_id():
    print(id_email)
    if id_email not in table.liste_id():
        try:
            table.add_mail(tableExterne.email_as_list(id_email))
            print(id_email)
        except Exception as e:
            print("ERREUR POUR l'ID " + str(id_email)+" : "+str(e))
            fichier_erreurs.write("ERREUR POUR l'ID " + str(id_email)+" : "+str(e))

table.save()
fichier_erreurs.close()
table.close()
tableExterne.close()
