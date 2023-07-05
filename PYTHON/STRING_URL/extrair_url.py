
import os
os.system("cls")
#VAMOS TRABALHAR COM FATIAMENTO

texto="abcde"
print(texto)
print(texto[0])
print(texto[0:1])
print(texto[0:2])
print(texto[0:5])
print(texto[0:7])

url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'
moeda = 'bytebank.com/cambio?moedaOrigem=real'
fatia = moeda[0:19] #url base
fatia1 = moeda[20:36] #url parametros

print(url)
print(moeda)
print(fatia)
print(fatia1)


