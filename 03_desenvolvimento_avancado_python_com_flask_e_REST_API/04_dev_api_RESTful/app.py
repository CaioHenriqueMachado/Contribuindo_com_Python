from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades
import json


app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    { 'id': 0,
      'nome': 'Caio',
      'habilidades': ['Python', 'Flask', 'Django']
     },
    { 'id': 1,
      'nome': 'Paulo',
      'habilidades': ['HTML', 'CSS', 'Angular']
     }
]

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'Erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido, procure o administrador'
            response = {'status': 'Erro', 'mensagem': mensagem}
        return response
    def put(self, id):
        dados = json.loads(request.data.decode('utf-8'))
        desenvolvedores[id] = dados
        return dados
    def delete(self, id):
        desenvolvedores.pop(id)
        return {'Status': 'sucesso', 'mensagem': 'Registro excluído'}

class listar_desenvolvedores(Resource):
    # CRIAR DESENVOLVEDOR
    def get(self):
        dados = json.loads(request.data.decode('utf-8'))
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]
    # LISTAR DESENVOLVEDORES
    def post(self):
        return desenvolvedores

api.add_resource(listar_desenvolvedores, '/dev/')
api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(Habilidades, '/habilidades/')


if __name__ == "__main__":
    app.run(debug=True)