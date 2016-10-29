import numpy as np
import math
from btree import *
from collections import Counter
MODULO = 256

def buildHuffmann(data,tree):
	new = bitarray()
	for i in data:
		new = new + tree[i]
	return new.tobytes()

def initTree(frequence):
	lista = []
	for i in frequence:
		lista.append(N(i,frequence[i]))
	return lista
	
def entropy(data):
	freq = Counter(data)
	accum = 0
	for i in freq:
		calc = float(freq[i]) / float(len(data))
		accum = accum + (calc*math.log(calc,MODULO))
	return -accum,freq

r = open("7.input.subs.X",'rb').read()
data = np.array([t for t in r])
entropia,freq = entropy(data)	

lista = initTree(freq)
lista.sort() 
tree = huffmann(lista)


data2 = buildHuffmann(data,tree)

entropia2,freq2 = entropy(data2)

print("Entropia Original: " + str(entropia))
print("Entropia Nova: " + str(entropia2))	