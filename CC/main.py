#Criptografia clássica : Caesar, vigenere, transposição, substituição.
#Edson Lemes da Silva
#Disciplina de Segurança
#Testes para as cifras

from os import listdir
import numpy as np
from cc import *

inputs = listdir('testcases/inputs/')
outputs = listdir('testcases/outputs/')

find = { 'c' : 0, 'v' : 0, 's' : 0, 't': 0}
total = { 'c' : 0, 'v' : 0, 's' : 0, 't': 0}
#print(cipher['c'])
for inp in inputs:
	try:
		arq = open('testcases/inputs/'+ str(inp),"rb")
	except IOError:
		print("Problema ao abrir o arquivo:" + str(inp))
		
	inputname = arq.name
	n,inpr = inputname.split('.')
	n = n[len(n)-1]
	
	#arquivo original	
	b = arq.read()
	data = np.array([t for t in b ])
	
	for out in outputs:
		if n==out[0]:
			try:
				arq2 = open('testcases/outputs/' + str(out), "rb")
			except IOError:
				print("Problema ao abrir o arquivo:" + str(out))
			name = arq2.name
			n2,inp2,cipher,k = name.split('.')
			n2 = n2[len(n2)-1]
		
			#print(inputname)
		
			#arquivo cifrado
			cif = arq2.read()
			data2 = np.array([t for t in cif])
		
		
			if n==n2:
				#print(total['c'])
				print("Comparing..." + inputname + " " + name)
				if cipher == 'ceasar':
				
					total['c']+=1
					if k == 'X':
						for i in range(MODULO):
							cifr = encryCeasar(data,i)
							#print(cifr)
							if np.array(cifr==data2).mean()== 1:
								find['c']+=1
								#print("Chave encontrada, " + "k:"+str(i))
								break


					else:
						k = int(k)
						cifr = encryCeasar(data,k)
						if np.array(cifr==data2).mean()== 1:
							find['c']+=1
							#print("Criptografia aceita")
				elif cipher == 'vig':
					total['v']+=1
					if k=='X' or k=='Y':
						#implementar como descobrir uma chave
						diff = data2 - data
						for i in range(1,30):
							enc = encryVigenere(data,diff[0:i])
							if (data2==enc).mean() == 1:
								find['v']+=1
								break
					else:
						keys  = np.array(list(k.encode()), dtype=int)
						cifr = encryVigenere(data,keys)
						if np.array(cifr==data2).mean()==1:
							find['v']+=1
				
				elif cipher == 'transp':
					total['t']+=1
					if k == 'X' or k == 'Y':
						for i in range(1,MODULO):
							cifr = encryTransposition(data,i)
							if np.array(cifr==data2).mean()==1:
								find['t']+=1
								break
					else:
						k = int(k)
						cifr = encryTransposition(data,k)
						if np.array(cifr==data2).mean()==1:
							find['t']+=1
							
				else:
					total['s']+=1
					if k == 'X' or k == 'Y':
						#implementar como descobrir uma chave
						continue
					else:
						q = open('testcases/' + k,"rb")
						q = q.read()
						q = np.array([t for t in q])
						cifr = encrySubs(data,q)
						if np.array(cifr==data2).mean()==1:
							find['s']+=1
			#print("s")
			arq2.close()
	arq.close()	
#cipher['c']
#v  =total['c']	#
print("\nAcertos Ceasar:" +str(find['c'])+"/"+str(total['c']))
print("Acertos Vigenere:" +str(find['v'])+"/"+str(total['v']))
print("Acertos Transposicao:" +str(find['t'])+"/"+str(total['t']))
print("Acertos Substituicao:" +str(find['s'])+"/"+str(total['s']))
print("Porcentagem de acertos:" + str(round(100*sum(find.values())/ sum(total.values()),2)))