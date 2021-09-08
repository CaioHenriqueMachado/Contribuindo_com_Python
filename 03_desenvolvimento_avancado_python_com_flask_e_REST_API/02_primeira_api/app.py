from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/<int:id>', methods=['GET', 'POST'])
def pessoas(id):
    return jsonify({'id': id, 'nome': 'Caio', 'profissão': 'desenvolvedor'})


# @app.route('/soma/<int:valor1>/<int:valor2>/', methods=['GET', 'POST'])
# def soma(valor1, valor2):
#     return jsonify({'soma': valor1 + valor2})


# Em body tipo -> raw -> JSON preencher {"valores": [10,5,3]} e irá retornar a soma
@app.route('/soma', methods=['POST'])
def soma():
    dados = json.loads(request.data.decode('utf-8'))
    total = sum(dados['valores'])
    print(total)
    return jsonify ({'soma': total})

if __name__ == "__main__":
    app.run(debug=True)