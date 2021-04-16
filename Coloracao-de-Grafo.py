### Trabalho Analise de Algoritmos #####
### Professor: Paulo Henrique 
### Alunos: Felipe Augusto Ferreira de Castro | Matrícula: 11711BCC033 

import csv 

#################### GRAPH DEFINITION SECTION #################################
class Vertice:
    def __init__(self,value,arestas):
        ## value valor atribuido ao vertice 
        ## arestas uma lista de indexadores para os outros vertices que ele aponta 
        self.__Value = value
        self.__Arestas = arestas  
    def get_value(self):
        return self.__Value
    def get_Arestas(self):
        return self.__Arestas
    def exist_aresta(self,vertice_index):
        return vertice_index in self.__Arestas
    def set_value(self,newvalue):
        self.__Value = newvalue
    def insere_aresta(self,vertice_index):
        self.__Arestas.append(vertice_index)
    def remove_aresta(self,vertice_index):
        if(vertice_index in self.__Arestas):
            self.__Arestas.pop(vertice_index)


class Grafo:
    def __init__(self):
        self.__Vertices = []
        self.__Arestas_number = 0 
    def insere_vertice(self,vertice): 
        ## vertice um objeto da classe vertice  
        self.__Vertices.append(vertice)
    def insere_aresta(self,vertice_index_1,vertice_index_2):
        if self.vertice_exist_aresta(vertice_index_1,vertice_index_2):
            return 
        self.__Vertices[vertice_index_1].insere_aresta(vertice_index_2)
        self.__Vertices[vertice_index_2].insere_aresta(vertice_index_1)
        self.__Arestas_number += 1
    def remove_aresta(self,vertice_index_1,vertice_index_2):
        self.__Vertices[vertice_index_1].remove_aresta(vertice_index_2)
        self.__Vertices[vertice_index_2].remove_aresta(vertice_index_1)
        self.__Arestas_number -= 1
    def remove_vertice(self,vertice_index):
        self.__Vertices.pop(vertice_index)
        for vertice in self.__Vertices:
            vertice.remove_aresta(vertice_index)
    def vertice_get_value(self,vertice_index):
        return self.__Vertices[vertice_index].get_value()
    def vertice_get_arestas(self,vertice_index):
        return self.__Vertices[vertice_index].get_Arestas()
    def vertice_set_value(self,vertice_index,newvalue):
        self.__Vertices[vertice_index].set_value(newvalue)
    def vertice_exist_aresta(self,vertice_index1,vertice_index_2):
        return vertice_index_2 in self.__Vertices[vertice_index1].get_Arestas()
    def get_vertices_number(self):
        return len(self.__Vertices)
    def get_arestas_number(self):
        return len(self.__Arestas_number)

############################################ END GRAPH DEF SECTION #########################################################

############################################ GRAPH COLOR SECTION ####################################################



def colore_grafo(grafo):
    #### para cada vertice i do grafo vamos olhar todas a cores de seus vizinhos
    i = 0
    for i in range(grafo.get_vertices_number()):
        colors = []
        for vertice in grafo.vertice_get_arestas(i):
             colors.append(grafo.vertice_get_value(vertice))
        color = 1
        able = True
        while True:       ### enquanto nao encontrarmos uma cor possivel de colorir esse vertice 
            for c in colors:
                ### verificamos se os visinhos possuem esta cor     
                if color == c:
                    ### caso um visinho tenha a mesma cor desabilite a flag     
                    able = False
                    break
            if able == True:
                ### caso esteja abilitada significa que a cor pode ser aplicada a este vertice 
                break
            color += 1
            able =True
        grafo.vertice_set_value(i,color) ## atribuimos a cor para o vertice i 


### ler grafo de um arquivo csv 
arquivo_grafo =  "grafo1.csv"
cores = ["vermelhor","azul","verde"]
grafo = Grafo()
### lendo vertices do arquvio 
with open(arquivo_grafo,newline='') as csv_file: 
    csv_leitor  = csv.reader(csv_file,delimiter=',')
    for arestas in csv_leitor:
        v  = Vertice(0,[])
        grafo.insere_vertice(v)

### lendo arestas 
with open(arquivo_grafo,newline='') as csv_file: 
    csv_leitor  = csv.reader(csv_file,delimiter=',')
    max_line =  grafo.get_vertices_number()/2
    i = 0
    for arestas in csv_leitor:
        arestas = list(map(int,arestas)) ## converte de string para inteiro 
        for aresta in arestas:
            grafo.insere_aresta(i,aresta)
        i+=1

colore_grafo(grafo)

i = 0 
for i in range(grafo.get_vertices_number()):
    print(grafo.vertice_get_arestas(i))


i = 0 
for i in range(grafo.get_vertices_number()):
    print("vertice[",i,"]"," : ",cores[grafo.vertice_get_value(i)-1])