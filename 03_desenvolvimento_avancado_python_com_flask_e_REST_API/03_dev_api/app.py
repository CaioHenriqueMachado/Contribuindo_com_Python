from flask import Flask, jsonify, request
import json

app = Flask(__name__)

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

# Devolve, apaga, e altera um desenvolvedor
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'Erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido, procure o administrador'
            response = {'status': 'Erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data.decode('utf-8'))
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'Status': 'sucesso', 'mensagem': 'Registro excluído'})


#Lista desenvolvedores e inclui um novo desenvolvedor.
@app.route('/dev/', methods=['GET', 'POST'])
def listar_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data.decode('utf-8'))
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)
    
if __name__ == "__main__":
    app.run(debug=True)