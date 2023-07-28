
import os
os.system("cls")

# import sqlite
import sys
import sqlite3 as lite
con = lite.connect("dados.bd")

#dados = ['vaso','sala','vaso de planta','PvA','13/03/2023','120',"001002",'c:imagem']
#novos_dados = ['vaso','Banheiro','vaso de planta','PvA','13/03/2023','120',"001002",'c:imagem',5]

#INSERIR DADOS ------------------------------------------------
def inserir_dados(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO inventario(nome, local, descricao, marca, data_compra,valor_compra,serie, imagem) VALUES(?,?,?,?,?,?,?,?)"
        cur.execute(query,i)


#ATUALIZAR DADOS -----------------------------------------------------
def atualizar(i):
    with con:
        cur = con.cursor()
        query = "UPDATE inventario SET nome=?, local=?, descricao=?, marca=?, data_compra=?,valor_compra=?,serie=?, imagem=? WHERE id=?"
        cur.execute(query,i)


#DELETAR DADOS -----------------------------------------------------

def apagar(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM inventario WHERE id=?"
        cur.execute(query, i)


#VER inventário -----------------------------------------------------
def visualizar():   
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Inventario")
        rows = cur.fetchall()
        for row in rows:
             lista_itens.append(row)
        return lista_itens
            
    
#VER ítem no inventário -----------------------------------------------------

def ver_item(id):   
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Inventario WHERE id=?",(id))

        query = "SELECT * FROM inventario WHERE id?"

        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
        return lista_itens


    



