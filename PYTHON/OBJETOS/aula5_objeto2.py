#REMOVENTO DUPLICATAS
#VAMOS CRIAR UM CLASSE PARA cONTER OS dADOS QUE TEM NAS OUTRAS DUAS CLASSES

# 
## melhorando para mão precisar usar usar o IF e nem o print usaremos o __str__ e return

import os
os.system("cls")
class programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    
    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
    
    def __str__(self):
        return (f'Nome: {programa.nome}  - Likes: {programa.likes}')
    


class Filme(programa):
    def __init__(self,nome,ano,duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    def __str__(self):
        return(f'Nome: {programa.nome} - Duração: {self.duracao} Minutos - Likes: {programa.likes}')
        

    

class Serie(programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas

    def __str__(self):
        return(f'Nome: {programa.nome} - Temporadas: {self.temporadas} - Likes: {programa.likes}')

class Playlist():
    def __init__(self, nome, programa):
        self.nome = nome
        self.programa = programa

    def tamanho(self):
        return len(self.programa)
    


vingadores = Filme('vingadores - guerra infinita', 2018, 168)

print(f"Nome: {vingadores.nome}, Likes: {vingadores.likes}")
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
print(f"Nome: {vingadores.nome}- Likes: {vingadores.likes}\n")

atlanta = Serie('atlanta', 2018, 2)

print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} likes: {atlanta.likes}')
atlanta.dar_likes()
atlanta.dar_likes()
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} likes: {atlanta.likes}\n')

tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

filmes_series = [vingadores,atlanta,demolidor,tmep]

playlist_fim_de_semana = Playlist('fim de semana', filmes_series)


## melhorando para não precisar usar usar o IF
for programa in filmes_series:
    print(programa)




    
    # if hasattr(programa, 'duracao'):
    #     detalhes = "Duração: ",programa.duracao

    # elif hasattr(programa, 'temporadas'): 
    #     detalhes = ("Quant. de Temporadas: ",programa.temporadas)
    # else:
    #     detalhes = ""
    
    # print(f'Nome: {programa.nome} - {detalhes} - Likes: {programa.likes}')

