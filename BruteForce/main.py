#Criptografia clássica : Caesar, vigenere, transposição, substituição.
#Edson Lemes da Silva
#Disciplina de Segurança
#Testes para as cifras

from os import listdir
from breaker import *


outputs = listdir('test/output/')


#print(cipher['c'	
dic = open('dic.txt','rb').read()
dic = dic.split()
for out in outputs:
		try:
			arq2 = open('test/output/' + str(out), "rb")
		except IOError:
			print("Problema ao abrir o arquivo:" + str(out))
		name = arq2.name
		n2,inp2,cipher,k = name.split('.')
		n2 = n2[len(n2)-1]
		
			#print(inputname)
		
			#arquivo cifrado
		cif = arq2.read()
		data = np.array([t for t in cif])
		if cipher == 'ceasar':
			k = ceasarBreaker(data,dic)
			
		elif cipher == 'vig':
			continue
			k = vigenereBreaker(data,dic)
		elif cipher == 'transp':
			k = transpositionBreaker(data,dic)
		print("Arquivo:" + str(name) + " Chave:" + str(k))
