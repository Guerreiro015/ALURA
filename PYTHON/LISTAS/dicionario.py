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
   

# Vamos usar o defaultdict para sempre usar o padrao int()
meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()

# sem o defaultdict teriamos que usar o .get para retornrar 0 quando náo existisse
# neste exemo iremos contar a quant. de cada items.

for palavra in meu_texto.split():
  ate_agora = aparicoes.get(palavra, 0)
  aparicoes[palavra] = ate_agora + 1

print(aparicoes,"\n")



from collections import defaultdict

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
  ate_agora = aparicoes[palavra]
  aparicoes[palavra] = ate_agora + 1

print(aparicoes)

