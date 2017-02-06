#Edson Lemes
#Reconhecer padrões
import numpy as np

w = ['baboon', 'badger', 'bat','rat', 'bear', 'beaver']
def getWord(wrd):
	prox = 0
	num = {}
	wrds = []
	for l in wrd:
		if l not in num:
			num[l] = str(prox)
			prox = prox + 1
		wrds.append(num[l])
	return wrds	

def patterns(words):
	pp = {}
	for i in words:
		p = getWord(i)
		p = ''.join(p)
		if p not in pp:
			pp[i] = p
		else:
			pp[i].append(p)

	return pp
pp = patterns(w)
print(pp)