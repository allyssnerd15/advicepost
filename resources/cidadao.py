from flask_restful import Resource, reqparse
from models.cidadao import ModelProprietario


class Proprietarios(Resource):
    def get(self):
        return {'cidadao': [dados.json() for dados in ModelProprietario.query.all()]}

class Proprietario(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('id')
    argumentos.add_argument('Nome')
    argumentos.add_argument('Modelo')
    argumentos.add_argument('cor')


    def get_dono(self, id):
        id = ModelProprietario.find_id(id)
        if id:
            return id.json()
        return {'message': 'Cidadao não encontrado'}, 404
    
    
    def get_modelo(self, modelo):
        modelo = ModelProprietario.find_modelo(modelo)
        if modelo:
            return modelo.json()
        return {'message': 'model not found'}, 404
        

    def post(self, id):
        if ModelProprietario.find_id(id):
            return {f"message": "id '{id}' already exists "}
        
        dados = Proprietario.argumentos.parse_args()
        new_car = ModelProprietario(id, **dados)
        try:
            new_car.save_cadastro()
        except:
            return {'message': 'Houve um erro interno ao tentar salvar os dados'}
        return new_car.json(), 200
     
    def put(self, id):
        dados = Proprietario.argumentos.parse_args()
        new_car = ModelProprietario.find_id(id)
        if new_car:
            new_car.update_car(**dados)
            try:
                new_car.save_cadastro()
            except:
                return {'message': 'Houve um erro interno ao tentar salvar os dados'}
            return new_car.json(), 200
        car_new = ModelProprietario(id, **dados)
        return car_new.json(), 201
    
    def delete(self, id):
        dados = ModelProprietario.find_id(id)
        if dados:
            try:
                dados.delete_dados()
            except:
                return {'Messagem': 'Houve um erro interno para excluir dados'}
            return {'Message': 'Cidadao deletado'}
        return {'Message': 'Cidadao not found'}, 404
       

