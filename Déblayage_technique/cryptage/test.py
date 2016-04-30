import hashlib
import Crypto

# HASH
chaine = "secret"
pwd=bytes(chaine, 'utf-8')
hashed = hashlib.sha224(pwd).hexdigest()
print(hashed)
print(type(hashed))

# Chiffrement asymétrique, clé privé: hashed 

