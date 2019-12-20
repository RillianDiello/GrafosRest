# -*- coding: utf-8 -*-
#pacotes nativos
import sys
import os
import time

from Models.Grafo import *
from Models.Arquivo import *


class Main(object):

    def __init__(self, interface = None, arquivo_entrada = None):
        self.arquivo_entrada = arquivo_entrada
        self.arquivo = Arquivo(self.arquivo_entrada)
        self.grafo = Grafo()
        self.interface = interface


    def validar_arquivo(self):

        try:
            # Abro os aqruivos para garantir que não estão corrompidos
            e = open(self.arquivo_entrada, "r")
            # verifica se existe conteudo no arquivo de entrada
            if len(e.readline()) == 0:
                raise IOError

        # tratando os erros
        except IOError:
            # os.system("cls")
            print("\nArquivos de entradas invalidos ou corrompidos")
            sys.exit(0)

    def monta_grafo(self):
        try:
            for arquivo in self.arquivo.dadosEntrada:
                for i in range(0, 2):
                    vertice = Vertice(arquivo[i])
                    self.adicionaVerticeAoGrafo(vertice)
                self.adicionarArestaAoGrafo(arquivo)
        except:
            sys.exit('Erro ao construir Grafo')


    # chama o metodo que ler os dados do arquivo de entrada
    def tratar_dados_de_entrada(self):
        return self.arquivo.ler_entrada()

    def adicionaVerticeAoGrafo(self, vertice):
        exists = self.grafo.busca_Vertice(vertice.getId())
        if (exists):
            return False
        else:
            self.grafo.novo_Vertice(vertice.getId())

    def adicionarArestaAoGrafo(self, linhaCsv):
        v1 = Vertice(linhaCsv[0])
        v2 = Vertice(linhaCsv[1])

        arestaJaExiste = self.grafo.busca_Aresta(v1, v2)

        if arestaJaExiste is None:
            self.grafo.nova_Aresta(v1.getId(), v2.getId(), int(linhaCsv[2]))
        else:
            print("já existe")

    def atualizaGrafo(self, listaNovaRota):
            listaNovaRota = listaNovaRota.split(',')

            v1 = Vertice(listaNovaRota[0])
            self.adicionaVerticeAoGrafo(self, v1)

            v2 = Vertice(listaNovaRota[1])
            self.adicionaVerticeAoGrafo(self, v2)

            self.adicionarArestaAoGrafo(self, listaNovaRota)