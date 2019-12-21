from Api.api import *
from Controller.Main import *
import json
from flask import Flask
from flask import jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

controller_api = Main()

@app.route('/', methods=['GET'])
def home():
    menu =  []
    menu.append('<h1>Menu</h1>')
    menu.append('<p>/arquivo/nome_do_arquivo</p>')
    menu.append('<p>/caminho/Origem-Destino</p>')
    menu.append('<p>/novaRota/Origem,Destino,Custo</p>')
    return ''.join(menu)

@app.route('/arquivo/<name>', methods=['GET'])
def openFile(name):
    arquivos = controller_api.arquivo.abrir_arquivo(name, 'r')
    lista_dados = arquivos.readlines()
    arquivos.close()
    return jsonify(lista_dados)

@app.route('/novaRota/<novaRota>',methods=['GET'])
def NovaRota(novarota):
    if controller_api.arquivo.writeArquivo(novarota):
        controller_api.atualizaGrafo(novarota)
        return '<h1>Rota incluida com sucesso</h1>'
    else:
        return '<h1>Não foi possivel incluir rota</h1>'

@app.route('/caminho/<rotaPedida>', methods=['GET'])
def retornaRotaECusto(rotaPedida):
    rota = rotaPedida.split('-')
    origem = Vertice(rota[0])
    destino = Vertice(rota[1])
    rota = controller_api.obtemRota(origem, destino)
    custo = controller_api.obtemCustoRota(origem, destino)
    return json.dumps([rota, custo])


if __name__ == '__main__':

    args = []

    for param in sys.argv:
        args.append(param)
    # nome_ficheiro = args[1]
    nome_ficheiro = 'input-fileCp.csv'

    app.run(host='127.0.0.10', port='5000', debug=True)