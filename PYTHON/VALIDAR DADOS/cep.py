import os
os.system('cls')
from validar_cep import cep
import requests

codigo = 12312340
codigo1 = 123123409999900
codigo2 = str('04760060')

print(cep(codigo))
#print(cep(codigo1))
print(cep(codigo2))
# cep(codigo)
# cep(codigo2)

r = requests.get('https://viacep.com.br/ws/64670000/json/')
print(r.text)

lista =dict( r.text)

for i in lista:
    print(i)

