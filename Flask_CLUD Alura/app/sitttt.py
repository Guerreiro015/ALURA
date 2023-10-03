from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (create_engine,String,Integer,column,Table,table,MetaData)

engine=create_engine('sqlite:///banco.db', echo=True)

metadata = MetaData(bind=engine)

cliente= Table('cliente',metadata,
               column('id',Integer, primary_key=True),
               column('nome',String(40)),
               column('email',String(40)),
               column('telefone',String(40))
                             
               
               )
metadata.create_all()

