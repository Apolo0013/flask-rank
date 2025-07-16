from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/rank/get', methods=['POST', 'GET'])
def PegarPessoalDosRanko():
    # - 1 retorna uma lista com todos no rank
        # Top: todos
        # Top: 10
        # Top: 5
    return {'fsd': 'teu cu'}, 200


@app.route('/rank/add', methods=['POStT'])
def AddAPessoalDB():
    # - 1 add ele em um json simple
    # - 2 verificar se ele ja esta no banco de dados
    pass

if __name__ == '__main__':
    app.run(app)