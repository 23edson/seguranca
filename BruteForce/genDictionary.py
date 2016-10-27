#Edson Lemes da Silva
#este arquivo gera um dicionário de palavras

import collections
import re

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
	