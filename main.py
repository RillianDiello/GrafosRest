
import csv, sys, json
from utils.Grafo import *
from utils.Vertice import *
from flask import Flask

app = Flask(__name__)

arquivoGrafo = []

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/<name>')
def hello_name(name):
    arquivos  = openArquivo(name)
    return json.dumps(arquivos)



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

def printRota(Grafo, Origem, Destino):

    grafo.Depth_first_search()
    Grafo.imprime_Grafo_com_Destino(Origem.getId(), Destino.getId())
    resposta = grafo.Dijkstra(Origem.getId())
    for ele in resposta:
        if ele.id == Destino.getId():
            print('Custo ', ele.estimativa)


def openArquivo(nome_ficheiro):
    # nome_ficheiro = 'input-file.csv'
    arquivos = []
    with open(nome_ficheiro, 'r') as ficheiro:
        reader = csv.reader(ficheiro, delimiter=',', quoting=csv.QUOTE_NONE)
        try:
            for linha in reader:
                arquivos.append(linha)
        except csv.Error as e:
            sys.exit('ficheiro %s, linha %d: %s' % (nome_ficheiro, reader.line_num, e))
    return arquivos

if __name__ == '__main__':

    app.run(host='127.0.0.10', port='5000', debug=True)

    args = []

    # Ler argumento linha de comando e abrindo arquivo
    for param in sys.argv:
        args.append(param)
    # nome_ficheiro = args[1]
    nome_ficheiro = 'input-file.csv'
    arquivos = openArquivo(nome_ficheiro)

    with open(nome_ficheiro, 'r') as ficheiro:
        reader = csv.reader(ficheiro, delimiter=',', quoting=csv.QUOTE_NONE)
        try:
            for linha in reader:
                arquivos.append(linha)
        except csv.Error as e:
            sys.exit('ficheiro %s, linha %d: %s' % (nome_ficheiro, reader.line_num, e))

    grafo = Grafo()

    for arquivo in arquivos:
        for i in range(0, 2):
            vertice = Vertice(arquivo[i])
            adicionaVerticeAoGrafo(grafo, vertice)
        adicionarArestaAoGrafo(grafo, arquivo)

    # for ele in grafo.lista_Vertices:
    #     print(ele.getId())
    #
    # print('**************************')


    # for aresta in grafo.lista_Arestas:
    #         print(aresta.getOrigem().getId())
    #         print(aresta.getPeso())
    #         print(aresta.getDestino().getId())
    #         print('-------------------------')


    # print('DE-PARA')
    # origem, destino = map(str, sys.stdin.readline().split('-'))
    # origem = origem.replace('\n','')
    # destino = destino.replace('\n','')

    # ver1 = Vertice('GRU')
    # ver2 = Vertice('CDG')
    # printRota(grafo, ver1, ver2)

    #

