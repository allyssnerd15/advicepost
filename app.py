from flask import Flask
from flask_restful import Api
from resources.cidadao import Proprietarios, Proprietario

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
api = Api(app)

@app.before_first_request
def cria_banco():
    banco.create_all()  
    
api.add_resource(Proprietarios, '/', '/proprietario')
#api.add_resource(Proprietario, '/proprietario/modelo<string:Modelo>')
api.add_resource(Proprietario, '/proprietario/<string:id>', '/proprietario/modelo<string:Modelo>')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)