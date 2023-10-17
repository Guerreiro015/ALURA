

import mysql.connector

conn = mysql.connector.connect(user='root', password='lucas0108', host='localhost')

cursor = conn.cursor()
comando=('CREATE DATABASE IF NOT EXISTS notas')
cursor.execute(comando)

comando='''CREATE TABLE IF NOT EXISTS 'alunos'(
         "id" int(11) NOT NULL AUTO_INCREMENT,
      "nome" varchar(50) NOT NULL,
      "categoria" varchar(40) NOT NULL,
      "console" varchar(20) NOT NULL)'''

cursor.close()

