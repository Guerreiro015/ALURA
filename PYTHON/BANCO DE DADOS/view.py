
import os
os.system("cls")

# import sqlite
import sqlite3 as lite
con = lite.connect("dados.bd")

dados = ['vaso','sala','vaso de planta','PvA','13/03/2023','120',"001002",'c:imagem']

#INSERIR DADOS ------------------------------------------------
def inserir(valor):
    cur = con.cursor()
    query = "INSERT INTO inventario(nome, local, descricao, marca, data_compra,valor_compra,serie, imagem) VALUES(?,?,?,?,?,?,?,?)"
    cur.execute(query,valor)


#ATUALIZAR DADOS -----------------------------------------------------
alterar = ['vaso','quarto','vaso de planta','PvA','13/03/2023','120',"001002",'c:imagem',2]
def atualizar(valor):
    with con:
        cur = con.cursor()
        query = "UPDATE inventario SET nome=?, local=?, descricao=?, marca=?, data_compra=?,valor_compra=?,serie=?, imagem=? WHERE id=?"
        cur.execute(query,valor)


#DELETAR DADOS -----------------------------------------------------
deletar_dados = str(2)
def apagar(valor):
    with con:
        cur = con.cursor()
        query = "DELETE FROM inventario WHERE local = ?"
        cur.execute(query, valor)


#VER DADOS -----------------------------------------------------
ver_dados = []
def visualizar():   
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventario"
        cur.execute(query)

        dad = cur.fetchall()

        for x in dad:
            ver_dados.append(x)

    print(ver_dados)

ver_dados_individual = []
def visualizar_individual():   
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventario"
        cur.execute(query)

        dad = cur.fetchall()

        for x in dad:
            ver_dados.append(x)

    print(ver_dados)

#inserir(dados)
visualizar()
atualizar(alterar)
apagar(deletar_dados)
visualizar()

