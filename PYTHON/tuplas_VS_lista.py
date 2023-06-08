dias = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
semana = ("Domingo", "Segunda", "Terça", "Terça", "Quinta", "Sexta", "Sábado")
num = range(0,10)
# lista e formada usando colchetes
# tuplas é formada com parenteses
# A lista pode ser moficicada 
# A tupla NÃO pode ser modificada
# o RANGE também é um tipo de lista
dias.append('outro domimgo')
print(dias)

dias.pop()
print(dias)

print(semana)
print(num[5])

print(semana.index("Quinta"))
print(semana.count("Terça"))

# Não podemos usar del, remove(), pop() ou clear() com uma tupla
# podemos usar com lista

del dias[0] # deleta pelo indice do lista
print(dias)

dias.remove("Segunda") # Remove o item selecionado
print(dias)

dias.pop() # Remove o último item
print(dias)
dias.pop(3) # remove pelo indice
print(dias)

dias.clear() # limpa tudo
print(dias)



