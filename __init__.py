import csv, sys, json
from Models.Grafo import *
from Models.Vertice import *
from flask import Flask
from flask import request, jsonify, render_template, request, url_for, redirect
from app.view import *

app = Flask(__name__)
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