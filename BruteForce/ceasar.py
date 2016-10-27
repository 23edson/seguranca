#Edson Lemes
#Algoritmos de força bruta
import sys
sys.path.insert(1, '../CC')
from cc import *


def ceasarBreaker(data,dictionary):
	#count = 0
	#limiar = 0
	for k in range(1,256):
		count = 0
		wrd = decryCeasar(data,k)
		wrd = bytes([t for t in wrd])
		wrd = wrd.split()
		
		
		for i in wrd:
			if i in dictionary:
				count = count + 1
				
		if ((count*100)/len(wrd)) > 50:
			print("chave encontrada : " + str(k))
			break 
	print("Chave nao encontrada")	


def TranspositionBreaker(data,dictionary):
	#count = 0
	#limiar = 0
	for k in range(1,256):
		count = 0
		
		wrd = decryTransposition(data,k)
		wrd = bytes([t for t in wrd])
		wrd = wrd.split()
		out = []
		for i in wrd:
			if i in dictionary:
				count = count + 1
		print(len(wrd))
		if ((count*100)/len(wrd)) > 60:
			print("Chave encontrada: " + str(k))
			break
	print("Chave nao encontrada")

def VigenereBreaker(data,dictionary):
	word = "0123456789abcdefghijklmnopqrstuvxzwy"
	for tam in range(1,10):
		permut = itertools.product(word, repeat=tam)
		for i in permut:
			count = 0
			k = np.array([ord(t) for t in i])
			k = list(k)
			wrd = decryVigenere(data,k)
			wrd = bytes([t for t in wrd])
			wrd = wrd.split()
			for j in wrd:
				if j in dictionary:
					count = count + 1
			if((count*100)/len(wrd)) > 60:
				print("Chave encontrada: " + str(k))
				return
	print("Chave nao encontrada")

#data = open('test/6.input.ceasar.X','rb').read()
data = open('test/6.input.vig.1234','rb').read()
data = np.array([t for t in data])
dic = open('dic.txt','rb').read()
dic = dic.split()
VigenereBreaker(data,dic)
