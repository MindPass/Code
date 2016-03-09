import re

chaine ='''
fdmfld
dflkdlfkd
dfldkf
charset=UTF-8
charset=Latin-1
<<<<<<< HEAD
charset=iso-8859-15
ch
'''

encodages = re.findall(r'charset=[a-zA-Z0-9-]+', chaine)
print(encodages)

for element in encodages:
    encodage = element.split('=')[1]
    print(encodage)
=======
charset=iso-889-1
ch
'''

encodage = re.findall(r'charset=[a-zA-Z0-9-]+', chaine)
print(encodage)
>>>>>>> ec21bc254813273dc9307d0880332d9ded329c25
