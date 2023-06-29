# utilizando métodos de varias classes

import os
os.system("cls")
class Funcionario:
    def __init__(self,nome):
        self.nome = nome

    def registra_horas(self, horas):
        print(f'Horas registradas...: {horas}\n')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

class hispter():
    def __str__(self):
        return f'Meu {self.nome}'
    

class junior(Alura):
    pass

class pleno(Alura,Caelum):
    pass

class senior(Alura,Caelum,hispter):
    pass

jose = junior("Carlos")
jose.busca_perguntas_sem_resposta()
jose.mostrar_tarefas()
jose.registra_horas("12:00")

luan = pleno("tesouro")
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes("Python")
luan.registra_horas("13:00")

pedro= senior("garoto")
print(pedro)
