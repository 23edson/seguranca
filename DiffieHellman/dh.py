#Diffie Hellman
#Edson Lemes da Silva
#Disciplina de Segurança
import sys


#Exponenciação modular
def expMod(base,key,mod):
	exp = base%mod
	resp = 1
	while key > 0:
		if(key%2==1):
			resp = int((resp*exp)%mod)
		exp = int((exp*exp)%mod)
		key = int(key/2)
		
	return resp
		 

base  = 5
prime = "E53DF5FC3F650D066875837012A4E7BEA863C65CB592D9C36942CF69CBC6DD4FD804E19CCF2696C9BEBCF18742FA5FB091CBDE1782E8291009464913ECE19"
prime = prime + "7457800EA6E43B0E2A64615D182B6DE150479C58D1C7C702D47EA3031B379CA13A2048C964E1D1E8D4CD3815D0895BF31E53271D4607E16461B77FB2"
prime = prime + "6100915D6799060203EDEBFEA9495A5A8E7CED68FC9DB2D47CE7992461BA78174608AD0BBE3F5E63EC6C960564430CBD2E6E587D08EE12F94B5B99DFF"
prime = prime + "B12C6727A25E800DAC6CD8DE77A5BBC93B36E444B070888CB5ADD991870466968A6E9A23C2EE0A1D671C9B601081A44AA6A58D4DC76686EF15FCE1C9AE"
prime = prime + "B4033395A9B24BE1AA1929BB"
mod = (int(prime,16))

key = int(sys.argv[1])

a = expMod(base,key,mod)
print(a)

b = int(input('Qual a chave compartilhada?\n'))

secretKey = expMod(b,key,mod)
print('---------------')
print('Chave calculada:' + str(secretKey))