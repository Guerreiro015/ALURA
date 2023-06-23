#REMOVENTO DUPLICATAS
#VAMOS CRIAR UM CLASSE PARA cONTER OS dADOS QUE TEM NAS OUTRAS DUAS CLASSES
class programa:
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



class Filme(programa):
    def __init__(self, nome, ano, duracao):
        self._nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self._likes = 0

    

class Serie(programa):
    def __init__(self, nome, ano, temporadas):
        self._nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self._likes = 0

    

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(vingadores.nome)


atlanta = Serie('atlanta', 2018, 2)
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} likes: {atlanta.likes}')
atlanta.dar_likes()
atlanta.dar_likes()

print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} likes: {atlanta.likes}')