import re

chaine ='''
fdmfld
dflkdlfkd
dfldkf
charset=UTF-8
charset=Latin-1
charset=iso-8859-15
'''

encodages = re.findall(r'charset=[a-zA-Z0-9-]+', chaine)
print(encodages)

for element in encodages:
    encodage = element.split('=')[1]
    print(encodage)
