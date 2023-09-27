from asyncio import DefaultEventLoopPolicy
from flask import Flask,render_template
from flask import request,redirect,flash



# criar a 1 pagina no site
# route -> caminho a seguir
# função -> O que vai ser exibido no site
# vamos usar servirdor heroko gratis

app = Flask(__name__)

@app.route("/") #Decorate logo acima da função
def homepage():
    return render_template('index.html')


@app.route("/contatos")
def contatos():
   return render_template('contatos.html')


@app.route('/cliente', defaults={"nome_cliente": "USUÁRIO"} )
@app.route('/cliente/<nome_cliente>')
def cliente(nome_cliente):
   return render_template('cliente.html',nome_cliente=nome_cliente)
   # para executarmos um variavel python no html colocamos ela entre duas chaves{{variavel}}


@app.route('/usuario2')
def usuario2():
   nome="FAISCA"
   dados={
      'nome': 'Antonio',
      'filho': 'Lucas',
      'filha': 'Luana',
      'esposa': 'Francisca'
   }
   return render_template('usuario2.html', nome=nome,dados=dados)


@app.route('/login')
def login():
   return render_template('login.html')

# usando methodo get
@app.route('/autenticar', methods=['GET','POST'])
def autenticar():
   usuario = request.args.get('usuario')
   senha = request.args.get('senha')
   return f'USUÁRIO: {usuario} e SENHA: {senha}'

@app.route('/login2')
def login2():
   return render_template('login2.html')

# usando methodo post
@app.route('/autenticar2', methods=['POST'])
def autenticar2():
   usuario = request.form.get('usuario') # troca o args(argumentos) por form(formulario)
   senha = request.form.get('senha')
   if usuario=='antonio' and senha=='123':
      return f'USUÁRIO: {usuario} e SENHA: {senha}'
   else:
      flash('dados invalidos')
      return redirect('/login2')
      #IMPORTANTE para uso do flash
      #temos que definir uma palavra secerta no arquivo

   




if __name__ == __name__:  
  app.run(debug=True) # Colocando o true o site atusliza as informaões automoaticamnte
  
