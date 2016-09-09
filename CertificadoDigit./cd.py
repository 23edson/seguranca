#Gerador de certificado digital
#Edson Lemes da Silva
#Disciplina de Segurança

import hashlib
import Crypto
import Crypto.Hash.SHA256 as sha256
from Crypto.PublicKey import RSA
from Crypto import Random
import os


#codificando
text = "Este trabalho consiste em gerar um certificado digital válido"

hashf = hashlib.sha256()
hashf.update(text.encode('utf-8'))
hashf.digest()

rnumber = Random.new().read
cryptKey = RSA.generate(2048, rnumber)
publicKey = cryptKey.publickey()
encrypted = publicKey.encrypt(hashf,32)

key = publicKey.exportKey().decode(encoding = 'utf-8')
header = len(text)

text = text + header+ "\n...h\n" str(encrypted.decode(encoding = 'latin')) + "\nh...\n" + str(key)


#decodificando

hash1 = ''
head = "\n...h\n"
foot = "\nh...\n"

for i in text:
	





