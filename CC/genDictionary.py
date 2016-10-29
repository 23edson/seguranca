#Edson Lemes da Silva
#este arquivo gera um dicionário de palavras

import collections
import re

def dicAlphabet():
	with open('texto.txt') as arq:
		c = collections.Counter(
			word.lower()
	 		for line in arq
	 		for word in re.findall(r'\b[^\W\d_]+\b', line)) #desconsidera acentuações
	
	arq.close()
	arq = open('dic.txt','w')
	for i in sorted(list(c)):
		arq.write(i+"\n")
	arq.close()
	
def dicCustom():
	arq = open('texto.txt')
	arq1 = open('dic.txt','w')
	string = arq.read()
	r = list(string)
	for i,j in enumerate(r):
		if j=="\n" or j=="\t":
			r[i] = " "
		
	string = ''.join(r)
	string = string.split(" ")
		
	myset = (set(list(string)))
	
	listum = list(myset)
	print(listum)
	for i in sorted(listum):
		arq1.write(i + "\n")
	arq1.close()
	arq.close()
	
	
	
dicCustom()
		