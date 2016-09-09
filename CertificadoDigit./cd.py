#Gerador de certificado digital
#Edson Lemes da Silva
#Disciplina de Segurança

import hashlib
import Crypto
import Crypto.Hash.SHA256 as sha256
from Crypto.PublicKey import RSA
from Crypto import Random
import os

HEADER = 32 #32bytes iniciais pertence ao cabeçalho do arquivo
#codificando
text = "Este trabalho consiste em gerar um certificado digital válido"

#codificando

hashf = hashlib.sha256()
hashf.update(text.encode(encoding = 'latin'))
hashf = hashf.digest()

rnumber = Random.new().read
cryptKey = RSA.generate(2048, rnumber)
publicKey = cryptKey.publickey()
encrypted = publicKey.encrypt(hashf.decode(encoding = 'latin').encode(),32)

key = publicKey.exportKey('PEM').decode(encoding = 'latin')
header = str(len(text))+ "." + str(len(encrypted[0].decode(encoding = 'latin'))) + "." +str(len(key))+"."
if len(header) < HEADER:
	for i in range(len(header),HEADER):
		header+=str('#')

text = header + text + str(encrypted[0].decode(encoding = 'latin')) + str(key)


#decodificando

ReadHeader = ''
for i in range(0,HEADER):
	ReadHeader+=text[i]

tSize,hashSize,pubkeySize,junk = ReadHeader.split('.')

#get original text
Readtext = ''
#get Hash
ReadHash = ''
#get publickey
ReadpubKey = ''
for i,j in enumerate(text):
	if i>HEADER-1 and i<int(tSize)+HEADER:
		Readtext+=j
	elif i>=int(tSize)+HEADER and i< int(tSize)+int(hashSize)+HEADER:
		ReadHash+=j
	elif i>=int(tSize)+int(hashSize)+HEADER:
		ReadpubKey+=j
		

hashf1 = hashlib.sha256()
hashf1.update(Readtext.encode(encoding = 'latin'))
hashf1 = hashf1.digest()
getKey = RSA.importKey(ReadpubKey)
encrypted1 = getKey.encrypt(hashf1.decode(encoding = 'latin').encode(),32)
print("Arquivo íntegro") if encrypted1[0]==ReadHash.encode('latin') else print("Arquivo com problema")







