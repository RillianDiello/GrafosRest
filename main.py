
import csv, sys, json
from utils.Grafo import *
from utils.Vertice import *
from flask import Flask

app = Flask(__name__)

grafo = Grafo()

arquivoGrafo = []

@app.route('/', methods=['GET'])
def home():
    menu =  []
    menu.append('<h1>Menu</h1>')
    menu.append('<p>/arquivo/nome_do_arquivo</p>')
    menu.append('<p>/caminho/Origem-Destino</p>')
    return ''.join(menu)

@app.route('/arquivo/<name>')
def openFile(name):
    arquivos  = openArquivo(name)
    return json.dumps(arquivos)

@app.route('/caminho/<rotaPedida>')
def retornaRotaECusto(rotaPedida):
    rota = rotaPedida.split('-')
    origem = Vertice(rota[0])
    destino = Vertice(rota[1])
    return json.dumps(printRota(origem, destino))



def adicionaVerticeAoGrafo(Grafo, Vertice):
    exists = Grafo.busca_Vertice(Vertice.getId())
    if (exists):
        return False
    else:
        Grafo.novo_Vertice(Vertice.getId())

def adicionarArestaAoGrafo(Grafo, LinhaCsv):
    v1 = Vertice(LinhaCsv[0])
    v2 = Vertice(LinhaCsv[1])

    arestaJaExiste = Grafo.busca_Aresta(v1,v2)

    if arestaJaExiste is None:
        Grafo.nova_Aresta(v1.getId(), v2.getId(), int(LinhaCsv[2]))
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

    for arquivo in arquivos:
        for i in range(0, 2):
            vertice = Vertice(arquivo[i])
            adicionaVerticeAoGrafo(grafo, vertice)
        adicionarArestaAoGrafo(grafo, arquivo)
    return arquivos


if __name__ == '__main__':

    app.run(host='127.0.0.10', port='5000', debug=True)

    args = []

    for param in sys.argv:
        args.append(param)
    nome_ficheiro = args[1]

    arquivos = openArquivo(nome_ficheiro)






