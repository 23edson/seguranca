#Gerador de certificado digital
#Edson Lemes da Silva
#Disciplina de Segurança

import Crypto
import Crypto.Hash.SHA256 as sha256
from Crypto.PublicKey import RSA
from Crypto import Random
import os

text = "Este trabalho consiste em gerar um certificado digital válido"

hashf = sha256.new()
hashf.update(text.encode('utf-8'))


