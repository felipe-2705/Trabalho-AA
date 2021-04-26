import csv 
arq = []
arestas_number = 0

def build_dimacs_line(vertice1, vertice2):
    return "e %s %s\n" % (str(vertice1),str(vertice2))

def add_aresta(vertice1,vertice2):
    global arq 
    global arestas_number
    if ([vertice1,vertice2] in arq ) or ([vertice2,vertice1] in arq): 
        return 
    arq.append([vertice1,vertice2])
    arestas_number+=1
 

arquivo_grafo =  "./grafos/grafo3.csv"

vertice = 0
with open(arquivo_grafo,newline='') as csv_file: 
    csv_leitor  = csv.reader(csv_file,delimiter=',')
    for arestas in csv_leitor:
        arestas = list(map(int,arestas))
        for a in arestas:
            add_aresta(vertice,a)
        vertice += 1


with open("./grafos/grafo3.dimacs","w") as new_file:
    new_file.write("p edge %s %s\n" % (str(vertice),str(arestas_number)))
    for line in arq:
        string =  build_dimacs_line(line[0],line[1])
        new_file.write(string)

