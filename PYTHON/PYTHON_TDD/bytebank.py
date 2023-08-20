
from datetime import date

class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        ano_nascimento = self._data_nascimento.split("/") # separar a data em string onde hover barra /
        ano_nascimento = ano_nascimento[-1] # Vai pegar o último item da lista
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            valor = 0
        return valor

    def __str__(self):
        return f'Funcionario(Nome: {self._nome}, Dt.Nasc: {self._data_nascimento}, Sálario: {self._salario:,.2f})'