#Criptografia clássica : Caesar, vigenere, transposição, substituição.
#Edson Lemes da Silva
#Disciplina de Segurança
#Testes para as cifras

from os import listdir
from cc import *

def indice(x):
	for i,j in enumerate(x):
		if j==32:
			return i
	return None

inputs = listdir('testcases/inputs/')
outputs = listdir('testcases/outputs/')

find = { 'c' : 0, 'v' : 0, 's' : 0, 't': 0}
total = { 'c' : 0, 'v' : 0, 's' : 0, 't': 0}
#print(cipher['c'])
arq = open('dic.txt')
dic = arq.read()
arq.close()
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
							print(i)
							cifr = decryCeasar(data2,i)
							#x = "".join([chr(t) for t in data2])
							y = "".join([chr(t) for t in cifr])
							num = 0
							Xi = cifr
							for k,j in enumerate(cifr):
								
								t = indice(Xi)
								if t!=None:
									sub = cifr[num:t]
									#j = t
									num = t+1
									k=t+1
									Xi = cifr[t+1:]
									st = "".join([chr(p) for p in sub])
									if st in dic:
										find['c']+=1
										print("Chave :" + str(i))
										break
								else:
									break
							


					else:
						continue
						#k = int(k)
						#cifr = encryCeasar(data,k)
						#if np.array(cifr==data2).mean()== 1:
						#find['c']+=1
							#print("Criptografia aceita")
				elif cipher == 'vig':
					continue
				
				elif cipher == 'transp':
					continue
							
				else:
					continue
						
			#print("s")
			arq2.close()
	arq.close()	
#cipher['c']
#v  =total['c']	#
print("\nAcertos Ceasar:" +str(find['c'])+"/"+str(total['c']))
print("Acertos Vigenere:" +str(find['v'])+"/"+str(total['v']))
print("Acertos Transposicao:" +str(find['t'])+"/"+str(total['t']))
print("Acertos Substituicao:" +str(find['s'])+"/"+str(total['s']))
print("Porcentagem de acertos:" + str(round(100*sum(find.values())/ sum(total.values()),2)) + "%")