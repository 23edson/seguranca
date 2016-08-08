#Troca de mensagem com RSA
#Edson Lemes da Silva
#Disciplina de Segurança

import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import hashlib
import binascii as bhex

msg = "Mensagem criptografada"

def alphaDecoder(num):
	
	return bhex.unhexlify(format(num,"x").encode('utf-8')).decode('utf-8')
	
def alphaEncoder():
	global msg
	#numb = base64.b64decode(msg)
	#return int(binascii.hexlify(numb, 16))
	return int(bhex.hexlify(msg.encode('utf-8')),16)

rnumber = Random.new().read

#hashl = hashlib.sha256(rnumber).digest()

cryptKey = RSA.generate(2048, rnumber)

publicKey = cryptKey.publickey()
conv = alphaEncoder()

encryptData = cryptKey.encrypt(conv,32)

decryptData = cryptKey.decrypt(encryptData)
decryptData = alphaDecoder(decryptData)

print("\nEncrypted: ", encryptData)
print("-------------------------\n")
print("\nDecrypted: ", decryptData)
