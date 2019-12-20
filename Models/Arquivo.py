# -*- coding: utf-8 -*-

import sys, csv
from Models.Vertice import *
from Models.Aresta import *
from Models.Grafo import *

class Arquivo(object):

	#Método construtor da classe
	def __init__(self, arquivo_entrada = None):
		self.arquivo_entrada = arquivo_entrada
		self.grafo = {}
		self.dadosEntrada = []


	def abrir_arquivo(self, arquivo, modo_abertura):
		return open(arquivo, modo_abertura)
	#Função ler os dados do arquivo de entrada grava em uma lista de dados e retorna está lista de dados
	def ler_arquivo(self):

		arq = self.abrir_arquivo(self.arquivo_entrada, "r")
		lista_dados = arq.readlines()
		arq.close()
		self.dadosEntrada = lista_dados

	#função que ler o arquivo de entrada
	def ler_entrada(self):
		self.ler_arquivo()
		self.monta_grafo()


		return self.grafo

	def writeArquivo(self,NovaRota):
		try:
			with open(self.dadosEntrada, 'a+') as ficheiro:
				ficheiro.write('\n')
				ficheiro.write(NovaRota)
				ficheiro.write('\n')

			return True
		except:
			return False