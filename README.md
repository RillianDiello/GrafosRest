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

A solução proposta para este desafio teve como base o estudo de Algoritmos de Grafos. Grafos são algumas das estruturas 
fundamentais dentro da computação, sendo constituidos basicamente de vertices e arestas. Arestas estas que podem ser 
direcionadas e possuirem um custo ou peso associado. 

Assim sendo, uma simples interpretação do arquivo de entrada, nos permite compreender que cada Origem e Destino 
correspode a um vertice, e a existência de uma conexão entra eles, corresponde a uma aresta, tal que o custo associado 
a conexão seria o custo da nossa aresta.

Partindo desta analagocia, basicamente o problema a ser resolvido e o conhecido caminho minimo ou caxeiro viajante.
Este é um dos problemas mais famosos e estudados dentro da Computação e existem atualmente diversas formas de solução 
para este problema. No entanto, é importante compreender que este problema se enquadra no que chamamos dentro da 
computação de problema NP-Completo. "Busquem conhecimento"

Uma das solução mais conhecida para esse tipo de problema é o algoritmo de Dijkstra. Esse algoritimo utiliza de uma
euristica para supor uma distancia maxima entre quaisquer dois vertices, e então realiza um processo de percurso dentro 
do grafo, partindo de um vertice origem X e identificando todas as menores distancias para que X atinja os demais.

O algoritmo de Dijkstra fornece uma solução muito cabivel dentro de diversos problemas computacionais envolvendo
o problema dos caminhos minimos. No entanto ele parte de algumas pré-condições para que seu funcionamento seja
garantindo. A primeira delas é que não existam arestas com pesos negativos, assim sendo não posso ter uma aresta cujo o
peso seja -1, -2 e assim por diante. Para esse caso existem outras soluções como o algoritmo de BellManFord, que não 
suporta ciclos negativos.

Como me baseie em um material de estudo, em alguns slides e até alguns códigos perdidos, enquanto estudava. Existem
diversos outros algoritmos implementados como: Busca em Largura, Busca em Profundidade, Euler, Arvore Geradora Minima,
Ciclos, Matriz Transpostas e etc.

No entanto para o problema em questão, foi utilizando realmente apenas o Dijkstra, pois estamos assumindo que vc não 
pode viajar em uma rota de avião de um lugar para outro sem pagar nada.

Foi utilizada a linguagem Python. Why?? O Python é uma linguagem que possui uma otima relação com problemas desta
natureza, além de ser uma linguagem relativamente fácil de ser utilizada. Outro ponto é que foi desenvolvida uma
interface Web utilizando uma API do python (Flask), e eu queria estudar como era isso =D.

#### Etapas de Solução ####

A solução deste probelma compreendeu a implementação de duas interfaces, uma console e outra web. Também foram 
desenvolvidas classes para representar os elementos que compõe o nosso o Grafo. Sendo classes para Arestas, Vertices e o
Grafo propriamente. 

Foi também necessário o desenvolvimento de um classe Arquivo, para manipular a leitura do nosso arquivo de entrada, bem
como as manipuluações necessárias como a inclusão de uma nova rota. E alem disso, foi desenvolvida uma classe Main.py
que engloba todas as operações e manipulações necessárias para a utilização dos grafos.


### Execução do programa ###
Neste projeto foram construidas duas interfaces, denominadas console.py e run.py. Sendo que ambas leêm um argumento de 
linha de comando que indica qual o arquivo será utilizado para a a construção do Grafo de origem. Para efeito de testes
a aplicação em console está com o arquivo estatico, mas pode ser mudado facilmente.
A inicializacao dos programas se da por linha de comando. Caso você deseje executar a solução run.py:
```shell
$ python run.py input-routes.csv
```
Caso deseje executar a soluçaão console.py:
```shell
$ python console.py input-routes.csv
```
### As interfaces ###
Aqui serão descritas as duas interfaces e algumas de suas peculiaridades:

#### Console ####
A solução console é a simples, basicamente ela le o arquivo de entrada. Constrói um grafo tendo como base as linhas do
arquivo. É disponibilizado um menu de operações bem básico, seguindo o que muita gente vê em programação I e II, e dentro
do próprio console ocorre toda a interação.

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
realizar esta operação. Não realizei um tratamento de exceptions tão efetivo visto que é uma aplicação bem simples, mas 
recomendo sempre o uso de tratamentos, visto que usuarios são em suma "difíceis".

Aqui temos um exemplo de saida, de uma operação no console, em que solicitamos a lista de rotas disponiveis:

![](/images/ExemploSaidaRotas.png)

O principal ponto negativo desta solução está literalmente na dificuldade de interação entre o usuario e aplicação.


