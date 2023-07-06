
import os
os.system("cls")
#VAMOS TRABALHAR COM FATIAMENTO

texto="abcde"
print(f"{texto}\n")
print(texto[0])
print(texto[0:1])
print(texto[0:2])
print(texto[0:5])
print(texto[0:7],"\n")

url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'
moeda = 'bytebank.com/cambio?moedaOrigem=real'
fatia = moeda[0:19] #url base
fatia1 = moeda[20:36] #url parametros
def imprime(a=None,b=None,c=None):
    print(a,f"{c} execução")
    print(b,f"{c} execução\n")

print(url)
print(moeda)
# print("\n",fatia,"\n")
# print(fatia1,"\n")
imprime(fatia,fatia1,"1ª")

# usamos o find para encontrar o indice da string
fim = len(moeda)
ind = moeda.find("?")

fatia = moeda[0:ind]
fatia1 = moeda[ind+1:fim+1]
# print("\n",fatia,"\n")
# print(fatia1,"\n")
imprime(fatia,fatia1,"2ª usando o find e o len")

# Podemos omitir o inicio ou o fim para fatiar e o python vai entender

fatia = moeda[:ind]
fatia1 = moeda[ind+1:]
# print(fatia,"( omitindo inicio)\n")
# print(fatia1,"(omitindo fim)\n")

imprime(fatia,fatia1,"3ª Omitindo o inicio e o fim")

#O find também procura por uma string e retorna o inicio dela

ind = url.find("moedaDestino")

fatia2 =url[ind:]

imprime(fatia,fatia2,"4ª\n")


