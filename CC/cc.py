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
		
#Reference:..
#https://inventwithpython.com/hacking/chapter9.html
#Cifra Transposição

def copyArray(data,k):
	flag = 0
	for i in range(k):
		if flag==0:
			out = np.asarray(data[i])
			flag = 1
		else:
			out = np.insert(out,len(out),data[i],axis=0)
	return out
	
def encryTransposition(data,k):
	m = []
	#out = np.array([],dtype=int)
	for i in range(k):
		m.append([])
		p = i
		while p < len(data):
			m[i].append(data[p])
			p = p + k
	return(copyArray(m,k))
			
		
def decryTransposition(data,k):
	flag = 0
	flag1 = 0
	m = []
	cols = math.ceil(len(data) / k)
	junk = (cols*k) - len(data)
	for i in range(cols):
		m.append([])
	for i in data:
		m[flag].append(i)
		flag = flag+1
		if (flag == cols) or  (flag == cols-1 and flag1 >= k - junk):
			flag = 0 
			flag1= flag1+1
	return(copyArray(m,cols))		
	

