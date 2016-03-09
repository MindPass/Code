import re

chaine ='''
fdmfld
dflkdlfkd
dfldkf
charset=UTF-8
charset=Latin-1
charset=iso-889-1
ch
'''

encodage = re.findall(r'charset=[a-zA-Z0-9-]+', chaine)
print(encodage)