#Criptografia clássica : Caesar, vigenere, transposição, substituição.
#Edson Lemes da Silva
#Disciplina de Segurança

import numpy as np
import sys

MODULO = 256
k = 3


#Cifra Ceasar
def encryCeasar(data,k):
	ceasar = np.vectorize(lambda x,k : (x+MODULO+k)%MODULO)
	return ceasar(data,k)
def decryCeasar(data,k):
	dec = np.vectorize(lambda x,k : (x+MODULO-k)%MODULO)
	return dec(data,k)
	



try:
	arq = open("data.in","rb")
except IOError:
		print("Problema ao abrir o arquivo")
		exit(0)

	
	

	encryptedCeasar = encryCeasar(data,k)

b = arq.read()
data = np.array([t for t in b ])

encryptedCeasar = encryCeasar(data,k)
list1=[chr(i) for i in encryptedCeasar]
decryptedCeasar = decryCeasar(encryptedCeasar,k)
print(''.join(list1))

print(decryptedCeasar)	



arq.close()	
	