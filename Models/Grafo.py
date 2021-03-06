from Models.Vertice import *
from Models.Aresta import *
import sys


# Grafo
class Grafo:
    def __init__(self, direcionado=True):
        self.lista_Vertices = []
        self.lista_Arestas = []
        self.direcionado = direcionado
        self.tempo = 0

    def novo_Vertice(self, identificador):
        # string = input(str("Identificador do Vertice: "))
        self.lista_Vertices.append(Vertice(identificador))

    def busca_Aresta(self, u, v):  # Método recebe dois objetos do tipo Vértice
        for w in self.lista_Arestas:
            origem = w.getOrigem()
            destino = w.getDestino()
            if origem.getId() == u.getId() and destino.getId() == v.getId():
                return w

    def busca_Vertice(self, identificador):  # Método recebe um int
        for i in self.lista_Vertices:
            if identificador == i.getId():
                return i
        else:
            return None

    def nova_Aresta(self, origem, destino, peso):  # Método recebe dois identificadores
        origem_aux = self.busca_Vertice(origem)
        destino_aux = self.busca_Vertice(destino)
        if (origem_aux is not None) and (destino_aux is not None):
            self.lista_Arestas.append(Aresta(origem_aux, destino_aux, peso))
        else:
            print("Um do Vertice ou ambos são invalidos")

        if self.direcionado == False:
            self.lista_Arestas.append(Aresta(destino_aux, origem_aux, peso))  # Aresta(u,v) e Aresta(v,u)

    def esta_Vazio(self):
        if len(self.lista_Vertices) == 0:
            return True
        else:
            return False

    def busca_Adjacente(self, u):  # Método recebe um vertice
        for i in range(len(self.lista_Arestas)):
            origem = self.lista_Arestas[i].getOrigem()
            destino = self.lista_Arestas[i].getDestino()
            if (u.getId() == origem.getId()) and (destino.getVisitado() == False):
                destino.setVisitado(True)  # Para que não retorn o mesmo vertice seguidas veses
                return destino
        else:
            return None

    def busca_Adjacentes(self, u):  # Método recebe um vertice e localizada seus adjacentes

        adjacentes = []
        for i in range(len(self.lista_Arestas)):
            origem = self.lista_Arestas[i].getOrigem()
            destino = self.lista_Arestas[i].getDestino()
            if (u.getId() == origem.getId()) and (destino.getVisitado() == False):
                # destino.setVisitado(True)  # Para que não retorn o mesmo vertice seguidas veses
                adjacentes.append(destino)
        return adjacentes

    ####################################################################

    def Depth_first_search(self):
        self.tempo = 0
        for v in self.lista_Vertices:
            v.setVisitado(False)
            v.input = 0
            v.output = 0
        for v in self.lista_Vertices:
            if not v.getVisitado():
                self.visita(v)

    def visita(self, u):
        u.setVisitado(True)
        self.tempo += 1
        u.setImput(self.tempo)
        v = self.busca_Adjacente(u)  # retorna apenas não visitado ou nulo
        while v is not None:
            v.predecessor.append(u.getId())
            self.visita(v)
            v = self.busca_Adjacente(u)

        self.tempo += 1
        u.setOutput(self.tempo)

    ####################################################################

    def inicializa_Fonte(self, fonte):  # Função usado no BFS e Dijkstra Método recebe um Objeto
        for v in self.lista_Vertices:
            v.setEstimativa(99999)
            v.setVisitado(False)
            v.setColor('B')
        fonte.setEstimativa(0)
        fonte.setColor('C')

    ####################################################################

    def Breadth_first_search(self, identificador):
        fonte = self.busca_Vertice(identificador)
        if fonte is None:
            return "Vertce Nulo"
        self.inicializa_Fonte(fonte)
        lista = [fonte]
        while 0 != len(lista):
            u = lista[0]  # recebe o vertice q está no inicio da fila
            # v = self.busca_Adjacente(u)  # retorna adjacente não visitado
            adjs = self.busca_Adjacentes(u)
            for v in adjs:
                if(v.getColor() == 'B'):
                    self.tempo += 1
                    v.setEstimativa(u.getEstimativa() + self.busca_Aresta(u, v).getPeso())
                    v.setImput(self.tempo)
                    v.setColor('C')
                    v.setPai(u.getId())
                    lista.append(v)
            u.setVisitado(True)


            u.setColor('P')
            lista.pop(0)

    def imprime_Grafo_com_Destino(self, origem, destino):
        retorno = []
        destino_Aux = self.busca_Vertice(destino)
        if len(destino_Aux.predecessor) == 0:
            return None
        else:
            retorno.append(self.imprime_Grafo(origem, destino, retorno))
            return retorno


    def imprime_Grafo(self, origem, destino, caminho):

        if origem == destino:
            return origem
        else:
            destino_Aux = self.busca_Vertice(destino)
            if len(destino_Aux.predecessor) == 0:
                return None
            else:
                caminho.append(destino)
                return self.imprime_Grafo(origem, destino_Aux.predecessor[0], caminho)

    def imprimirRotaDijsktra(self, resposta, destino):
        rota = []
        for vertice in resposta:
            if(vertice.getId() == destino):
                rota = vertice.predecessor
                rota.append(destino)
                return rota, vertice.getEstimativa()

        return rota
    ####################################################################

    def relaxa_Vertice(self, u, v, w):
        if v.getEstimativa() > (u.getEstimativa() + w.getPeso()):
            v.setEstimativa(u.getEstimativa() + w.getPeso())
            v.predecessor.append(u.getId())  # guarda apenas o id

    def Dijkstra(self, origem):
        fonte = self.busca_Vertice(origem)
        if fonte is None:
            return "Vertice Nulo"

        self.inicializa_Fonte(fonte)
        lista = []
        resposta = []  # conjunto resposta
        for i in self.lista_Vertices:
            lista.append(i)
        while len(lista) != 0:
            lista.sort()  # ordeno a lista baseado na estimativa
            u = lista[0]
            v = self.busca_Adjacente(u)
            if v is None:
                for i in self.lista_Vertices:  # como o vetice u marcou seus adj como visitado nenhum outro vértice visitara
                    i.setVisitado(False)  # esse vertice então preciso marcar como não visitado pra bucar os adj de outro vertice
                self.tempo += 1
                u.setImput(self.tempo)  # apenas mostra a ordem de visitação do grafo
                resposta.append(lista[0])
                lista.pop(0)  # retiro vertice sem adjacente da lista

            else:
                w = self.busca_Aresta(u, v)
                if w is not None:
                    self.relaxa_Vertice(u, v, w)

        return resposta


    ####################################################################

    def BellManFord2(self, origem):
        acc = 0
        fonte = self.busca_Vertice(origem)
        self.inicializa_Fonte(fonte)
        for i in range(1, len(self.lista_Vertices) - 1):
            for w in self.lista_Arestas:
                u = w.getOrigem()
                v = w.getDestino()
                if u.getEstimativa() + w.getPeso() < v.getEstimativa():
                    v.predecessor = [u.getId()]
                    v.setEstimativa(u.getEstimativa() + w.getPeso())

        for w in self.lista_Arestas:
            u = w.getOrigem()
            v = w.getDestino()
            if u.getEstimativa() + w.getPeso() < v.getEstimativa():
                acc = acc + 1
        if acc > 0:
            return True
        else:
            return False

    ####################################################################
    def Bellman_Ford(self, origem):
        fonte = self.busca_Vertice(origem)
        self.inicializa_Fonte(fonte)
        for i in range(1, len(self.lista_Vertices) - 1):
            for w in self.lista_Arestas:
                u = w.getOrigem()
                v = w.getDestino()
                # self.relaxa_Vertice(u, v, w)
                if u.getEstimativa() + w.getPeso() < v.getEstimativa():
                    print(u.getEstimativa(), w.getPeso(), v.getEstimativa())
                    v.setEstimativa(u.getEstimativa() + w.getPeso())
                    v.predecessor = u.getId()  # guarda apenas o id

        for w in self.lista_Arestas:
            u = w.getOrigem()
            v = w.getDestino()
            if u.getEstimativa() + w.getPeso() < v.getEstimativa():
                return False  # Não existe ciclo negativo
            else:
                return True  # Exixte ciclo negatio

    ####################################################################

    def Minimum_spanning_tree(self, origem):  # Prim
        fonte = self.busca_Vertice(origem)
        if fonte is None:
            return "Vertice Nulo"

        self.inicializa_Fonte(fonte)
        lista = []
        for i in self.lista_Vertices:
            lista.append(i)
        lista.sort()
        while len(lista) != 0:
            # ordeno a lista baseado na estimativa
            u = lista[0]
            v = self.busca_Adjacente(u)

            if v is None:
                for i in lista:  # como o vetice u marcou seus adj como visitado nenhum outro vértice visitara
                    i.setVisitado(
                        False)  # esse vertice então preciso marcar como não visitado pra bucar os adj de outro vertice
                    # retiro vertice sem adjacente
                lista.sort()
                self.tempo += 1
                u.setImput(self.tempo)
                lista.remove(u)
            else:
                w = self.busca_Aresta(u, v)
                if lista.count(v) > 0:
                    if v.getEstimativa() > w.getPeso():
                        v.predecessor = [u.getId()]
                        v.setEstimativa(w.getPeso())

        for u in self.lista_Vertices:
            if len(u.predecessor) > 0:
                print(u.predecessor, "------", u.getId())
        self.lista_Vertices.sort(key=lambda u: u.input, reverse=False)
        for i in self.lista_Vertices:
            print(i)

    ####################################################################

    def is_Cyclic(self):
        if (len(self.lista_Arestas) > len(self.lista_Vertices) - 1):
            print("Grafo Cíclico por Nº Aresta : %i > Nº Vértices: %i" % (
                len(self.lista_Arestas), len(self.lista_Vertices)))
        else:
            print("Grafo Acíclico")

    ####################################################################
    def grafo_Transposto(self):  # w(u,v) passa a ser w(v,u)
        for i in range(len(self.lista_Arestas)):
            origem = self.lista_Arestas[0].getOrigem()
            destino = self.lista_Arestas[0].getDestino()
            self.lista_Arestas.pop(0)
            self.lista_Arestas.append(Aresta(destino, origem, 0))

    def Strong_component_algorithm(self):
        print("Busca em Profundidade")
        self.Depth_first_search()
        self.lista_Vertices.sort(key=lambda u: u.output, reverse=True)  # ordena a lista em ralação a vertice.output
        for w in self.lista_Arestas:
            print(w)
        self.grafo_Transposto()
        print("Grafo Transposto:")
        for w in self.lista_Arestas:
            print(w)
        for i in self.lista_Vertices:
            i.input = 0
            i.output = 0
            i.setVisitado(False)
        print("\nComponetes fortemente Conexos\n")
        for i in self.lista_Vertices:
            if not i.getVisitado():
                self.visita(i)

    ####################################################################
    def cria_Euleriano(self):
        pass

    def eh_euleriano(self):
        for u in self.lista_Vertices:
            if self.grau(u) % 2 != 0:
                return False
        return True

    def grau(self, u):
        grau = 0
        for w in self.lista_Arestas:
            if u == w.getOrigem():
                grau += 1
        return grau

    ####################################################################
    def eh_Ponto(self, u):
        for v in self.lista_Vertices:
            v.setVisitado(False)

        u.setVisitado(True)
        self.visita(self.busca_Adjacente(u))
        for v in self.lista_Vertices:
            if v.getVisitado() == False:
                return True

    def Articulation(self):
        art = []
        for u in self.lista_Vertices:
            if self.eh_Ponto(u):
                art.append(u.getId())
        print("Pontos de Articulação", art)
        ####################################################################
