<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
<link rel="stylesheet" href="../static/bootstrap.css" >
<body background="/images/fundo.jpg" bgproperties="fixed">
(corpo do documento em HTML)
</body>

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Lucas@0108',
    database='jogoteca'

)

from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://user:password@localhost:3306/mydatabase')