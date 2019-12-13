
import csv, sys, json
from utils.Grafo import *
from utils.Vertice import *
from flask import Flask
from flask import request, jsonify

app = Flask('grafoApi')
app.config["DEBUG"] = True

grafo = Grafo()

arquivoGrafo = []

nome_ficheiro = ''

@app.route('/', methods=['GET'])
def home():
    menu =  []
    menu.append('<h1>Menu</h1>')
    menu.append('<p>/arquivo/nome_do_arquivo</p>')
    menu.append('<p>/caminho/Origem-Destino</p>')
    menu.append('<p>/novaRota/Origem,Destino,Custo</p>')
    return ''.join(menu)

@app.route('/', methods=['GET'])
@app.route('/arquivo/<name>')
def openFile(name):
    arquivos  = openArquivo(name)
    return jsonify(arquivos)

@app.route('/', methods=['GET'])
@app.route('/caminho/<rotaPedida>')
def retornaRotaECusto(rotaPedida):
    rota = rotaPedida.split('-')
    origem = Vertice(rota[0])
    destino = Vertice(rota[1])
    return json.dumps(printRota(origem, destino))

@app.route('/', methods=['GET'])
@app.route('/novaRota/<novaRota>')
def NovaRota(novaRota):
    if writeArquivo(novaRota):
        return '<h1>Rota incluida com sucesso</h1>'
    else:
        return '<h1>Não foi possivel incluir rota</h1>'



def adicionaVerticeAoGrafo(Vertice):
    exists = grafo.busca_Vertice(Vertice.getId())
    if (exists):
        return False
    else:
        grafo.novo_Vertice(Vertice.getId())

def adicionarArestaAoGrafo(LinhaCsv):
    v1 = Vertice(LinhaCsv[0])
    v2 = Vertice(LinhaCsv[1])

    arestaJaExiste = grafo.busca_Aresta(v1,v2)

    if arestaJaExiste is None:
        grafo.nova_Aresta(v1.getId(), v2.getId(), int(LinhaCsv[2]))
    else:
        print("já existe")

def printRota(Origem, Destino):

    grafo.Depth_first_search()
    grafo.imprime_Grafo_com_Destino(Origem.getId(), Destino.getId())
    resposta = grafo.Dijkstra(Origem.getId())
    custo = 0
    for ele in resposta:
        if ele.id == Destino.getId():
            custo = ele.estimativa

    return custo


def openArquivo(nome_ficheiro):
    arquivos = []
    with open(nome_ficheiro, 'r') as ficheiro:
        reader = csv.reader(ficheiro, delimiter=',', quoting=csv.QUOTE_NONE)
        try:
            for linha in reader:
                arquivos.append(linha)
        except csv.Error as e:
            sys.exit('ficheiro %s, linha %d: %s' % (nome_ficheiro, reader.line_num, e))

    return arquivos


def writeArquivo(NovaRota):
    try:
        with open(nome_ficheiro, 'a+') as ficheiro:
            ficheiro.write('\n')
            ficheiro.write(NovaRota)
            ficheiro.write('\n')

        atualizaGrafo(NovaRota)
        return True
    except:
        return False



def criaGrafo(dadosEntrada):
    try:
        for arquivo in dadosEntrada:
            for i in range(0, 2):
                vertice = Vertice(arquivo[i])
                adicionaVerticeAoGrafo(vertice)
            adicionarArestaAoGrafo(arquivo)
    except:
        sys.exit('Erro ao construir Grafo')


def atualizaGrafo(listaNovaRota):
    listaNovaRota = listaNovaRota.split(',')

    v1 = Vertice(listaNovaRota[0])
    adicionaVerticeAoGrafo(v1)

    v2 = Vertice(listaNovaRota[1])
    adicionaVerticeAoGrafo(v2)

    adicionarArestaAoGrafo(listaNovaRota)

if __name__ == '__main__':

    args = []

    for param in sys.argv:
        args.append(param)
    nome_ficheiro = args[1]
    # nome_ficheiro = 'input-fileCp.csv'

    arquivos = openArquivo(nome_ficheiro)
    criaGrafo(arquivos)

    app.run(host='127.0.0.10', port='5000', debug=True)






