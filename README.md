# Rota de Viagem #

Um turista deseja viajar pelo mundo pagando o menor preço possível independentemente do número de conexões necessárias.
Vamos construir um programa que facilite ao nosso turista, escolher a melhor rota para sua viagem.

Para isso precisamos inserir as rotas através de um arquivo de entrada.

## Input Example ##
```csv
GRU,BRC,10
BRC,SCL,5
GRU,CDG,75
GRU,SCL,20
GRU,ORL,56
ORL,CDG,5
SCL,ORL,20
```

## Explicando ## 
Caso desejemos viajar de **GRU** para **CDG** existem as seguintes rotas:

1. GRU - BRC - SCL - ORL - CDG ao custo de **$40**
2. GRU - ORL - CDG ao custo de **$61**
3. GRU - CDG ao custo de **$75**
4. GRU - SCL - ORL - CDG ao custo de **$48**
5. GRU - BRC - CDG ao custo de **$45**

O melhor preço é da rota **40** logo, o output da consulta deve ser **CDG - SCL - ORL - CDG**.


### Solução ###

A solução proposta para este desafio teve como base os Grafos. Grafos são algumas das estruturas fundamentais dentro da 
computação, sendo constituidos basicamente de vertices e arestas. Arestas estas que podem ser direcionadas e possuirem
um custo ou peso associado. 

De maneira direta cada linha do arquivo representa uma origem e um destino, bem como o custo envolvido entre eles.
Desta forma foi construido um grafo direcional com pesos associados. Apartir da construção desta estrutura foram implementados
alguns dos algoritmos conhecidos dentro de teoria dos Grafos para a solução do problema.

Basicamente o problema a ser resolvido e o conhecido caminho minimo ou caxeiro viajante. Este é um dos problemas mais famosos e 
estudados dentro da Computação e existem atualmente diversas formas de solução para este problema.

Visando uma maior riqueza do código forma desenvolvidos vários algoritmos existentes dentro da teoria dos Grafos, entre eles destacam-se:

* Busca em profundiade;
* Busca em Largura;
* Dijkstra;
* BellManFord e BellManFord2;
* Entre muitos outros;

No entanto para o problema em questão, foram utilizados apenas dois deles, sendo: a busca em profundidade que tem como objetivo
retornar a rota que deve ser feita vizando o menor custo. E o Algoritmo de Dijkstra que provem o valor do menor custo envolvido 
mediante o uso de uma estimativa inicial.


### Execução do programa ###
Neste projeto foram construidas duas interfaces, denominadas console.py e run.py. Sendo que ambas leêm um argumento de 
linha de comando que indica qual o arquivo será utilizado para a
A inicializacao do teste se dará por linha de comando onde o primeiro é a solução que deseja executar e o segundo 
argumento é o arquivo com a lista de rotas inicial.

Caso você deseje executar a solução run.py:
```shell
$ python run.py input-routes.csv
```
Caso deseje executar a soluçaão console.py:
```shell
$ python console.py input-routes.csv
```
### Explicando as interfaces ###
A solução console é a simples, basicamente ela le o arquivo de entrada. Constrói um grafo tendo como base as linhas do arquivo.
É disponibilizado um menu de operações, dentro do próprio console e toda a interação também ocorre ali:

```
        /////////  MENU  /////////
        1 - Para listar Rotas 
        2 - Para add nova rota
        3 - Para consultar rota
        0 - Para sair
        //////////////////////////
```

A cada uma das opções do menu são disponibilizadas instruções sobre a utilização da seção, por exemplo. Ao solicitar a 
inclusão de uma nova rota, é apresentado no console uma mensagem indicando qual o formato valido para 
realizar esta operação.

O principal ponto negativo desta solução está literalmente na dificuldade de interação entre o usuario e aplicação.


