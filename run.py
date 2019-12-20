from Api.api import *
from Models.Arquivo import *
from Models.Grafo import *
from Controller.Main import *

if __name__ == '__main__':

    args = []

    for param in sys.argv:
        args.append(param)
    # nome_ficheiro = args[1]
    nome_ficheiro = 'input-fileCp.csv'