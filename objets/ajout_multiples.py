#-*- coding: utf-8 -*-

from librairie import *


user_email=input('entrez le pseudo: ')+"@laposte.net"
mdp=input('Entrez le mdp: ') # à garder pendant le développement

l=user_email.split('@')
l[1]=l[1].split('.')[0]
nom_table=l[0]+'_'+l[1] # vaut 'pseudo_laposte'

table=Table(nom_table)
tableExterne=TableExterne('imap.laposte.net', user_email, mdp)
fichier_erreurs=open('fichier_erreurs.txt', 'a')


for id_email in tableExterne.liste_id():
	if(id_email not in table.liste_id()):
		try:
			table.add_mail(tableExterne.email_as_list(id_email))
		except Exception as e:
			fichier_erreurs.write(str(id_email)+"-Erreur : %s \n" % e)


fichier_erreurs.close()
table.save()
table.close()
tableExterne.close()
