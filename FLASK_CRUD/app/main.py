from asyncio import DefaultEventLoopPolicy
from flask import Flask,render_template
from flask import request,redirect,flash



# criar a 1 pagina no site
# route -> caminho a seguir
# função -> O que vai ser exibido no site
# vamos usar servirdor heroko gratis

app = Flask(__name__)
app.config['SECRET_KEY'] = 'base-chave-nova'

@app.route("/") #Decorate logo acima da função
def homepage():
    return render_template('index.html')




if __name__ == __name__:  
  app.run(debug=True) # Colocando o true o site atusliza as informaões automoaticamnte
  
