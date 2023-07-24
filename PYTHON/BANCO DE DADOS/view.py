
import os
os.system("cls")

# import sqlite
import sqlite3 as lite
con = lite.connect("dados.bd")

dados = ['vaso','sala','vaso de planta','PvA','13/03/2023','120',"001002",'c:imagem']

#INSERIR DADOS ------------------------------------------------
cur = con.cursor()
query = "INSERT INTO inventario(nome, local, descricao, marca, data_compra,valor_compra,serie, imagem) VALUES(?,?,?,?,?,?,?,?)"
cur.execute(query,dados)


#ATUALIZAR DADOS -----------------------------------------------------
atualizar_dados = ['vaso','Cozinha','vaso de planta','PvA','13/03/2023','120',"001002",'c:imagem',1]
with con:
    cur = con.cursor()
    query = "UPDATE inventario SET nome=?, local=?, descricao=?, marca=?, data_compra=?,valor_compra=?,serie=?, imagem=? WHERE id=?"
    cur.execute(query,atualizar_dados)


#DELETAR DADOS -----------------------------------------------------
deletar_dados = [1]
with con:
    cur = con.cursor()
    query = "DELETE FROM inventario WHERE id = ?"
    cur.execute(query, deletar_dados[0])


#VER DADOS -----------------------------------------------------
ver_dados = []
with con:
    cur = con.cursor()
    query = "SELECT * FROM inventario"
    cur.execute(query)

    dad = cur.fetchall()

    for x in dad:
        ver_dados.append(x)

print(ver_dados)



