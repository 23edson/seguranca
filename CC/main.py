#Criptografia clássica : Caesar, vigenere, transposição, substituição.
#Edson Lemes da Silva
#Disciplina de Segurança
#TEST :. Leitura do arquivo 'data.in', encontrado no mesmo diretório


import numpy as np
from cc import *

k = 3
k2 = 6

print("\nCeasar")
encryptedCeasar = encryCeasar(data,k)
decryptedCeasar = decryCeasar(encryptedCeasar,k)

list1=[chr(i) for i in encryptedCeasar]
print(''.join(list1))
list1=[chr(i) for i in decryptedCeasar]
print(''.join(list1))

print("\nVigenere")
encryptedVigenere = encryVigenere(data,[k,k2])
decryptedVigenere= decryVigenere(encryptedVigenere,[k,k2])

list1=[chr(i) for i in encryptedVigenere]
print(''.join(list1))
list1=[chr(i) for i in decryptedVigenere]
print(''.join(list1))

print("\nSubstituicao")
encryptedSub,keySub = encrySubs(data)
decryptedSub = decrySubs(encryptedSub,keySub)

list1=[chr(i) for i in encryptedSub]
print(''.join(list1))
list1=[chr(i) for i in decryptedSub]
print(''.join(list1))

print("\nTransposicao")
encryptedTransposition = encryTransposition(data,k)
decryptedTransposition = decryTransposition(encryptedTransposition,k)

list1=[chr(i) for i in encryptedTransposition]
print(''.join(list1))
list1=[chr(i) for i in decryptedTransposition]
print(''.join(list1))

