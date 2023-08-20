import os
os.system('cls')

from bytebank import *

def cliente(a,b,x):
    cliente = Funcionario(a,b,x)

    print(cliente) 
    print(f'{cliente.idade()} Anos')
    print(f'R$: {cliente.calcular_bonus():,.2f} de Bônus \n')


cliente('Antonio','10/03/1981',2400)
cliente('Luana','28/09/1998',2400)


