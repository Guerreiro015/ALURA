
import os
os.system("cls")

# import sqlite
import sqlite3 as lite
con = lite.connect("dados.bd")

#dados = ['vaso','sala','vaso de planta','PvA','13/03/2023','120',"001002",'c:imagem']
#novos_dados = ['vaso','Banheiro','vaso de planta','PvA','13/03/2023','120',"001002",'c:imagem',5]

#INSERIR DADOS ------------------------------------------------
def inserir_dados(valor):
    cur = con.cursor()
    query = "INSERT INTO inventario(nome, local, descricao, marca, data_compra,valor_compra,serie, imagem) VALUES(?,?,?,?,?,?,?,?)"
    cur.execute(query,valor)


#ATUALIZAR DADOS -----------------------------------------------------
def atualizar(valor):
    with con:
        cur = con.cursor()
        query = "UPDATE inventario SET nome=?, local=?, descricao=?, marca=?, data_compra=?,valor_compra=?,serie=?, imagem=? WHERE id=?"
        cur.execute(query,valor)


#DELETAR DADOS -----------------------------------------------------

def apagar(valor):
    with con:
        cur = con.cursor()
        query = "DELETE FROM inventario WHERE local=?"
        cur.execute(query, valor)


#VER DADOS -----------------------------------------------------
def visualizar():   
    ver_dados = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventario"
        cur.execute(query)

        dad = cur.fetchall()

        for x in dad:
            ver_dados.append(x)

    return ver_dados
   # print(ver_dados)

def ver_item(id):   
    ver_dados_individual = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventario WHERE id?"
        cur.execute(query,id)

        dado = cur.fetchall()
        for x in dado:
            ver_dados_individual.append(x)

    



