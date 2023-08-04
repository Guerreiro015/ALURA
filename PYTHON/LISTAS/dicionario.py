import os
os.system("cls")

aparicoes = dict(Guilherme = 2, cachorro = 1) # Para criar instaciando com o contrutor dict usa se elemento = valor
print(aparicoes)

# Normalmente se usa como abaixo
# Dicionario é parecido com conjuntos usamos como paremetros as ()
# Nos dicionários usamos dois parametros



aparicoes = {
  "Guilherme" : 1,
  "cachorro" : 2,
  "nome" : 2,
  "vindo" : 1
}

print(type(aparicoes))

print(aparicoes["Guilherme"]) # Mostar o valor relativo ao Guilherme
print(aparicoes["cachorro"]) # Mostar o valor relativo ao cachorro
print(aparicoes["nome"])


#print(aparicoes("xpto")) # dará erros porque não existe
print(aparicoes.get("xpto",0)) # Podemos usar get para retornar zero 0
print(aparicoes.get("nome",0)) # Podemos usar get para retornar zero 0

aparicoes_dicionários= dict(Guilherme = 2, cachorro = 1) # Para criar instaciando com o contrutor dict usa se elemento = valor

print(aparicoes_dicionários)


# Alterando valores de um dicionário

aparicoes["gato"] = 5 # Incluindo valores
print(aparicoes)

aparicoes["gato"] = 100 # alterando valores
print(aparicoes)

del aparicoes["gato"] # Deletando valores
print(aparicoes)

print("carlos" in aparicoes)
print("Guilherme" in aparicoes)

lista = ["Dinossauro",
  "Guilherme",
  "cachorro",
  "nome",
  "vindo",
  "GATO"]

for i in lista:
    if i in aparicoes:
       print(f'O Elemento {i} esta no conjunto aparicoes')
    else:
       print(f'O Elemento {i} não está no conjunto aparicoes') 


aparicoes = {
  "Guilherme" : 1,
  "cachorro" : 2,
  "nome" : 2,
  "vindo" : 1
}
 #Desempacotando

print("="*30)

for x,y in aparicoes.items():
   print(x,"=",y)

[f'item {x}'for a in aparicoes.keys()]

print([f'item {x}'for a in aparicoes.keys()])
   







