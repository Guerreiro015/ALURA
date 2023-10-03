from flask import Flask, render_template, request, redirect, session,flash
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key='alura'

app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'Lucas@0108',
        servidor = '127.0.0.1',
        database = 'jogoteca'
    )

db=SQLAlchemy(app)

class Jogos(db.Model): 
   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   nome = db.Column(db.String(50), nullable=False)
   categoria = db.Column(db.String(40), nullable=False)
   console = db.Column(db.String(20), nullable=False)


def __repr__(self): 
   return '<Name %r>' % self.name

class Usuarios(db.Model):
   nickname = db.Column(db.String(8), primary_key=True)
   nome = db.Column(db.String(20), nullable=False)
   senha = db.Column(db.String(100), nullable=False)
                        




@app.route('/')
def login():
   return render_template('login.html',titulo='LOGIN')

@app.route('/index')
def index():
   lista_jogos = Jogos.query.order_by(Jogos.id)
   if 'usuario_logado' not in session or session['usuario_logado'] == None:
        flash('Nenhum Usuário Logado')
        return redirect(url_for('login'))
   else:
        tit="jogos de 2023"
        return render_template('index.html',titulo=tit,jogos=lista_jogos)

@app.route('/novo_jogo')
def novo_jogo():
  if 'usuario_logado' not in session or session['usuario_logado'] == None:      
        flash('Nenhum Usuário Logado')
        return redirect(url_for('login'))
  else:
        return render_template('novo_jogo.html', titulo="novo jogo")


@app.route('/criar', methods=['POST'])
def criar():
  nome=request.form['nome']
  categoria=request.form['categoria']
  console=request.form['console']
  ano=request.form['ano']
  jogar=Jogos(nome,categoria,console,ano)
  lista_jogos.append(jogar)
  return redirect(url_for('index'))

# @app.route('/autenticar', methods=['POST'])
# def autenticar():
  # usuario=request.form['usuario']
  # senha=request.form['senha']
  # if usuario == 'antonio' and senha == '123':
  #   session['usuario_logado']=request.form['usuario']
  #   flash(request.form['usuario']+' Logado com Sucesso')
  #   return redirect(url_for('index'))
  # else:
  #   flash(request.form['usuario']+' Não Conseguiu Logar')
  #   return redirect(url_for('login'))
@app.route('/autenticar', methods=['POST'])
def autenticar():  
  usuario=Usuarios.query.filter_by(nickname=request.form['usuario']).first()
  if usuario:
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash('Usuário '+ usuario.nickname + ' logado com sucesso!')
            return redirect(url_for('index'))
        else:
            flash('Usuário não logado.')
            return redirect(url_for('login'))
  else:
    flash('Digite o nome de um usuário.')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
  flash('Usuário Desconectado')
  session['usuario_logado'] = None
  return redirect(url_for('login'))





if __name__ == __name__:  
  app.run(debug=True)

  # trecho da app
#app.run(host='0.0.0.0', port=8080)
