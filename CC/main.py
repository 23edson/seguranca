#Criptografia clássica : Caesar, vigenere, transposição, substituição.
#Edson Lemes da Silva
#Disciplina de Segurança
#TEST :. Leitura do arquivo 'data.in', encontrado no mesmo diretório


import numpy as np
from cc import *

k = 3
k2 = 6
result = ""

try:
	arq = open(sys.argv[1],"rb")
except IOError:
	print("Problema ao abrir o arquivo")
	exit(0)

	
	
b = arq.read()
data = np.array([t for t in b ])
#print(data)
#le chave Ceasar
numb = ''
for i in arq.name[::-1]:
	if i == '.':
		break
	numb+=str(i)
k = int(numb)
#print(arq.name[0])
if len(numb)>1:
	for i in range(len(numb)-1, -1, -1):
		result += numb[i]
		k = int(result)

arqout = 'testcases/inputs/'
arqout+=str(arq.name[18])
arqout+='.input.verif.txt'
#print(k)
arq.close()

	

print("\nCeasar")
#encryptedCeasar = encryCeasar(data,k)
decryptedCeasar = decryCeasar(data,k)


#list1=[chr(i) for i in encryptedCeasar]
#print(''.join(list1))
list1=[chr(i) for i in decryptedCeasar]
output = ''.join(list1)



out = open(arqout,"w+")
out.write(output)
out.close()

#print("\nVigenere")
#encryptedVigenere = encryVigenere(data,[k,k2])
#decryptedVigenere= decryVigenere(encryptedVigenere,[k,k2])

#list1=[chr(i) for i in encryptedVigenere]
#print(''.join(list1))
#list1=[chr(i) for i in decryptedVigenere]
#print(''.join(list1))

#print("\nSubstituicao")
#encryptedSub,keySub = encrySubs(data)
#decryptedSub = decrySubs(encryptedSub,keySub)

#list1=[chr(i) for i in encryptedSub]
#print(''.join(list1))
#list1=[chr(i) for i in decryptedSub]
#print(''.join(list1))

#print("\nTransposicao")
#encryptedTransposition = encryTransposition(data,k)
#decryptedTransposition = decryTransposition(encryptedTransposition,k)

#list1=[chr(i) for i in encryptedTransposition]
#print(''.join(list1))
#list1=[chr(i) for i in decryptedTransposition]
#print(''.join(list1))

