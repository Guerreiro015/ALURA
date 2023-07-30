import os
os.system("cls")



usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

todos = usuarios_data_science
all = usuarios_data_science.copy()
print (todos)
print (all)

todos.extend(usuarios_machine_learning)
all.extend(usuarios_machine_learning)

print (todos)
print (all)

# Uma das formas seria usar um for e IF:
res = []
for i in todos:
    if i not in res:
      res.append(i)
print(res)  

# Maneira mais fácil de retirar as duplicidades é usando o (set) = conjunto
# O set forma um cojunnto e desconsidera todos os dados duplicados
# O conjuto pose ser iteravel mas não possui indexação

conjunto = set(todos)
conjunto2 = set(usuarios_data_science+usuarios_machine_learning)
conjunto3 = sorted(set(todos))


print("\n",conjunto)
print(conjunto2)
print(conjunto3)

print(type(conjunto))

# Colocando os dados já como {} conjunto podemos usar o sinal | = or, para juntar
usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}
conjunto4 = usuarios_data_science | usuarios_machine_learning
print(conjunto4)