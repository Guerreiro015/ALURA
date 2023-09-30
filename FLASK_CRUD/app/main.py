from flask import Flask
from database import db
from flask import render_template
from flask_migrate import Migrate
from usuarios import bp_usuarios

app = Flask(__name__)
db.init_app(app)
conexao = 'sqlite:///meubanco.sqlite'

app.config['SECRET_KEY'] = 'base-chave-nova'
app.config['SQLALCHEMY_DATABASE_URL'] = conexao
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False
app.register_blueprint(bp_usuarios, url_prefix='/usuarios')


Migrate = Migrate(app,db)





@app.route("/") 
def index():
    return ('Ola testado o minfol')




if __name__ == __name__:  
  app.run(debug=True) # Colocando o true o site atusliza as informaões automoaticamnte
  
