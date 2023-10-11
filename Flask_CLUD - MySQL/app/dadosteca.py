
#pip install mysql-connector-python
#pip install mysql.connector  
import os
os.system('cls')

import mysql.connector

import os
os.system('cls')

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Lucas@0108',
    database='jogoteca'
)

cursor=conexao.cursor()
conexao.commit() # Quando edita/grava/deleta - banco de dados

#--------------------<>_______________________________________#

nom=('Roma')
nick=('gato')
sen=('12345')
dados=[nom,nick,sen]
print(dados)

def inserir_usuarios(i):
        comando =f'INSERT INTO usuarios(nome,nickname,senha) VALUES("{i[0]}", "{i[1]}", "{i[2]}")'
        cursor.execute(comando)
        conexao.commit() # Quando edita/grava/deleta - banco de dados
#inserir_usuarios(dados)

nom="Gran Turismo 6"
cat="Corrida"
con="PS5"
an="2026"
dados=[nom,cat,con,an]

def inserir_jogos(i):
        comando =f'INSERT INTO jogos(nome,categoria,console,ano) VALUES("{i[0]}", "{i[1]}", "{i[2]}", "{i[3]}")'        
        cursor.execute(comando)
        conexao.commit() # Quando edita/grava/deleta - banco de dados
#inserir_jogos(dados)


def atualizar_usuarios(i):
    comando = f'UPDATE usuarios SET nome = "{i[0]}", nickname="{i[1]}", senha="{i[2]}" WHERE id = "{i[3]}" '
    cursor.execute(comando)
    conexao.commit() # Quando edita/grava/deleta - banco de dados
    
#atualizar_usuarios(dados,'Romeu')



def atualizar_jogos(i):
    comando = f'UPDATE jogos SET nome = "{i[0]}", categoria="{i[1]}", console="{i[2]}", ano="{i[3]}" WHERE id = "{i[4]}" '
    cursor.execute(comando)
    conexao.commit() # Quando edita/grava/deleta - banco de dados
    
#atualizar_jogos(dados,'ps5')
    
#     #DELETAR DADOS -----------------------------------------------------
busca='i[0]'
def excluir_usuario(i):    
    comando = f'DELETE FROM usuarios WHERE nome = "{i}"'
    cursor.execute(comando)
    conexao.commit() # edita o banco de dados
#excluir_usuario(busca)

busca='Clash bandicoot'
def excluir_jogos(i):    
    comando = f'DELETE FROM jogos WHERE nome = "{i}"'
    cursor.execute(comando)
    conexao.commit() # edita o banco de dados
#excluir_jogos(busca)



    #VER inventário -----------------------------------------------------
def visualizar_usuarios():   
    comando=f'SELECT * FROM usuarios'
    cursor.execute(comando)
    resultado = cursor.fetchall() # ler banco de dados    
    return resultado
    
#visualizar_usuarios()       
                
   

def visualizar_jogos():   
    comando=f'SELECT * FROM jogos'
    cursor.execute(comando)
    resultado = cursor.fetchall() # ler banco de dados
   
    return resultado
#visualizar_jogos()        
            
        
                
# def ver_usuario(i):   
#         lista_itens = []
#         with con:
#             usuario='none'
#             cur = con.cursor()
#             cur.execute("SELECT * FROM usuario")
#             rows = cur.fetchall()
#             for row in rows:
#                 if i in row:
#                     usuario=row[1]
#                     senha=row[3]
#                     log=(usuario,senha)
#                     break
#                 else:
#                     log='none'
            
#             return log
        
# def ver_jogos(i):   
#         lista = []
#         with con:           
#             cur = con.cursor()
#             cur.execute("SELECT * FROM jogos")
#             rows = cur.fetchall()
#             for row in rows:
#                 if i in row:
#                    id=row[0]
#                    nome=row[1]
#                    categoria=row[2]
#                    console=row[3]
#                    ano=row[4]
#                    lista=(id,nome,categoria,console,ano)
#                    lista=[lista]
#                    break
                                 
#             return lista



cursor.close()
conexao.close()

            #excluir_jogos(('11',))


