#Criptografia clássica : Caesar, vigenere, transposição, substituição.
#Edson Lemes da Silva
#Disciplina de Segurança

import numpy as np
import sys
import random
import math
MODULO = 256



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
	
	#vigenere = np.array([],dtype=int)
	vigenere = []
	j = 0
	for i in data:
		#print(j)
		#j=j+1
		vigenere.append((i+MODULO+keys[flag])%MODULO)
		flag = flag + 1
		if flag >= tam:
			flag =0
			
			
	return vigenere
			
def decryVigenere(data,keys):
	flag = 0
	
	tam  = len(keys)
	dec = []
	for i in data:
		dec.append((i+MODULO-keys[flag])%MODULO)
		flag = flag  +1
		if flag >= tam:
			flag = 0
	return dec
	
#Cifra Substituição

#def genAlphabet():
	#tam = [i for i in range(MODULO)]
	#np.random.seed(3)
	
	#s = sorted(tam,key=lambda k: random.random())
	#return dict(zip(tam,s))

def encrySubs(data,key):
	tam = [i for i in range(MODULO)]
	#keys = genAlphabet()
	#sub = np.array([],dtype=int)
	sub = []
	for i in data:
		sub.append(key[tam.index(i)])
	
	return np.array(sub)
	
def decrySubs(data,key):
	tam = [i for i in range(MODULO)]
	#keys = {v: k for k, v in key.items()}
	#keys = genAlphabet()
	#sub = np.array([],dtype=int)
	sub = []
	for i in data:
		sub.append(tam[key.index(i)])
	return np.array(sub)
		
#Reference:..
#https://inventwithpython.com/hacking/chapter9.html
#Cifra Transposição


def encryTransposition(data,k):
	m = []
	p= 0
	tam = int(len(data))
	for i in range(0,tam,k):
		zero = [0]*k
		t = data[i:i+k]
		zero[0:t.size] = t
		m.append([])
		m[p].append(zero)
		p+=1
	 	
	return(np.asarray(np.array(m).T).reshape(-1))
			
		
def decryTransposition(data,k):
	m = []
	p= 0
	k = int(len(data) / k)
	#k = int(len(data)/k)
	return encryTransposition(data,k)	
	

