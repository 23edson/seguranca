#AES256 com hash sha256
#Edson Lemes da Silva
#Disciplina de Segurança

import base64
from Crypto.Cipher import AES
from Crypto import Random
import sys
import binascii
import hashlib
import os

SIZE = 32
text = 'Banklist:Nome:Fulano,Idade:25,Sexo:M,conta:1-200345,passwd:fog4063;Nome:Fulana,Idade:30,Sexo:F,conta:1-34456,passwd:joi5573;'

key = b"0x53BF277B" #1405036411
hashl = hashlib.sha256(key).digest()
iv = Random.new().read(AES.block_size)
encKey = AES.new(hashl, mode=AES.MODE_CFB, IV=iv)


#def pad(text):
#	text = str(text)
#	return text + str(((16 - len(text)%16))* '{')

def pad(text):
	return text + ((32-len(text)%32)*'{')

def encryptData(text):
	#key = os.urandom(SIZE)
	global encKey
	#global encD = AES.new(hashlib.sha256(key).digest(), mode=AES.MODE_CFB, IV=Random.new().read(AES.block_size))
	return iv + encKey.encrypt(pad(text))
	
	
def decryptData(text):
	
	global encKey
	dec = encKey.decrypt(text)
	string1 = str(dec[AES.block_size:]) 
	lnum = string1.count('{')
	return string1[2:len(string1)-(lnum+1)]
	
	
print("\nOriginal:", str(text))	
datac =encryptData(text)
print("\nEncrypted:" + str(binascii.hexlify(datac)))

datac = decryptData(datac)
print("--------------------")
print("\nDecrypted:" + datac)