import csv, sys, json
from utils.Grafo import *
from utils.Vertice import *
from flask import Flask
from flask import request, jsonify
from app.view import *

app = Flask('grafoApi')
app.config["DEBUG"] = True

grafo = Grafo()

arquivoGrafo = []

nome_ficheiro = ''

args = []

for param in sys.argv:
    args.append(param)
# nome_ficheiro = args[1]
nome_ficheiro = 'input-fileCp.csv'

arquivos = openArquivo(nome_ficheiro)
criaGrafo(arquivos)