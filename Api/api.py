import json

from Controller.Main import *
from flask import Flask
from flask import request, jsonify

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
def NovaRota(novaRota):
    if controller_api.arquivo.writeArquivo(novaRota):
        controller_api.atualizaGrafo(controller_api, novaRota)
        return '<h1>Rota incluida com sucesso</h1>'
    else:
        return '<h1>Não foi possivel incluir rota</h1>'

@app.route('/caminho/<rotaPedida>', methods=['GET'])
def retornaRotaECusto(rotaPedida):
    rota = rotaPedida.split('-')
    origem = Vertice(rota[0])
    destino = Vertice(rota[1])
    return json.dumps(printRota(origem, destino))


