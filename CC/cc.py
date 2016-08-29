#Criptografia clássica : Caesar, vigenere, transposição, substituição.
#Edson Lemes da Silva
#Disciplina de Segurança

import numpy as np
import sys
import random
MODULO = 256
k = 3
k2 = 4

#Cifra Ceasar
def encryCeasar(data,k):
	ceasar = np.vectorize(lambda x,k : (x+MODULO+k)%MODULO)
	return ceasar(data,k)
def decryCeasar(data,k):
	dec = np.vectorize(lambda x,k : (x+MODULO-k)%MODULO)
	return dec(data,k)
	
#Cifra Vigenere
def encryVigenere(data,keys):
	
	flag = 0
	tam  = len(keys)
	#print("tam1"+str(len(data)))
	
	vigenere = np.array([],dtype=int)
	
	for i in data:
		vigenere = np.insert(vigenere, len(vigenere),(i+MODULO+keys[flag])%MODULO,axis=0)
		flag = flag + 1
		if flag >= tam:
			flag =0
			
			
	return vigenere
			
def decryVigenere(data,keys):
	flag = 0
	
	tam  = len(keys)
	dec = np.array([],dtype=int)
	for i in data:
		dec = np.insert(dec, len(dec),(i+MODULO-keys[flag])%MODULO,axis=0)
		flag = flag  +1
		if flag >= tam:
			flag = 0
	return dec
	
#Cifra Substituição

def genAlphabet():
	tam = [i for i in range(MODULO)]
	#np.random.seed(3)
	
	s = sorted(tam,key=lambda k: random.random())
	return dict(zip(tam,s))

def encrySubs(data):
	
	keys = genAlphabet()
	sub = np.array([],dtype=int)
	for l in data:
		sub = np.insert(sub,len(sub),keys[l],axis=0)
	return sub,keys
	
def decrySubs(data,key):
	#keys = {v: k for k, v in key.items()}
	#keys = genAlphabet()
	sub = np.array([],dtype=int)
	for i in data:
		for k,j in key.items():
			if i==j:
				sub = np.insert(sub,len(sub),k,axis=0)
	return sub
		

try:
	arq = open("data.in","rb")
except IOError:
	print("Problema ao abrir o arquivo")
	exit(0)

	
	

	

b = arq.read()
data = np.array([t for t in b ])

#encryptedCeasar = encryCeasar(data,k)
#list1=[chr(i) for i in encryptedCeasar]
#decryptedCeasar = decryCeasar(encryptedCeasar,k)
#print(''.join(list1))

#print(decryptedCeasar)	
#print(data)
#print("tam"+ str(len(data)))

#encryptedVigenere = encryVigenere(data,[k,k2])
#decr= decryVigenere(encryptedVigenere,[k,k2])
#list1=[chr(i) for i in decr]
#print(''. join(list1))
encryptedSub,keySub = encrySubs(data)
#print(keySub)
list1=[chr(i) for i in encryptedSub]
print(''. join(list1))
dec = decrySubs(encryptedSub,keySub)
list1=[chr(i) for i in dec]
print(''. join(list1))
#print(encryptedVigenere)


arq.close()	
	
