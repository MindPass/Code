# -*- coding: utf-8 -*-

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