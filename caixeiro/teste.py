from math import sqrt
import random, decimal

f = open("cidades.txt","r")
l_caminho = f.read().split()
f.close()
caminho = {} #dicionario com a posicao de todas os caminhos {'city_number':[posX, posY]}

for x in range(0,len(l_caminho),3): #preenche o dicionario com os caminhos e posicoes
    caminho[l_caminho[x]] = [float(l_caminho[x+1]),float(l_caminho[x+2])]

def distancia(xyA,xyB): #calcula a distancia reta entre dois pontos
    xA, xB, yA, yB = (xyA[0]), (xyB[0]), (xyA[1]), (xyB[1])
    d = sqrt((xB-xA)**2 + (yB-yA)**2)
    return round(d,12)


caminho_custo = {} #dicionario com o custo de cada viagem {('cityA_number','cityB_number'): distancia}
for k in range(1,39):
    for c in range(1,39):
        caminho_custo[(str(k),str(c))] = distancia(caminho[str(k)],caminho[str(c)])

def custo_total(lista_caminho): #retorna o custo total de uma solucao
    custo = 0
    for caminho in range(len(lista_caminho)):
        if caminho == len(lista_caminho)-1: #se chegou no ultimo caminho soma o custo com a origem
            custo += caminho_custo[(str(lista_caminho[caminho]), str(lista_caminho[0]))]
        else:
            custo+=caminho_custo[(str(lista_caminho[caminho]),str(lista_caminho[caminho+1]))]
    return custo

def vizinho(solucao):
    solucao_anterior = solucao.copy()
    while True:
        posA = random.randint(0,37)
        posB = random.randint(0,37)
        a = solucao[posA]
        b = solucao[posB]
        solucao[posA] = b
        solucao[posB] = a

        posC = random.randint(0, 37)
        posD = random.randint(0, 37)
        c = solucao[posC]
        d = solucao[posD]
        solucao[posC] = d
        solucao[posD] = c

       
        if solucao != solucao_anterior:
            break
    return solucao

def probabilidade(custo_antigo,custo_novo,temperatura): #calcula a probabilidade de aceitacao da nova solucao
    decimal.getcontext().prec = 100
    diferenca_custo = custo_antigo - custo_novo
    custo_temp = diferenca_custo/temperatura
    p = decimal.Decimal(0)
    e = decimal.Decimal(2.71828)
    n_custo_temp = decimal.Decimal(-custo_temp)
    try:
        p = e**n_custo_temp
        resultado = repr(p)
    except decimal.Overflow:
        return 0.0

    try: #caso o numero tenha casas decimais
        fim = resultado.find("')")
        resultado = round(float(resultado[9:fim-1]), 3)

    except: #numero n tem casas decimais
        resultado = round(float(resultado[9:-2]))
    return resultado

def annealing(solution):
    print("Calculando rotas...\n")
    old_cost = custo_total(solution)
    T = 1.0
    T_min = 0.0000001
    alpha = 0.9
    melhor_solucao, best_cost = solution.copy(), old_cost
    while T > T_min:
        i = 1
        while i <= 500:
            new_solution = vizinho(solution)
            new_cost = custo_total(new_solution)
            ap = probabilidade(old_cost, new_cost, T)
            if ap > round(random.random(),3):
                solution = new_solution.copy()
                old_cost = new_cost
            i += 1

        T = T*alpha
    return melhor_solucao, best_cost

def gerasolucao(): #gera uma solucao aleatoria
    solucao_aleatoria = [x for x in range(1,39)]
    random.shuffle(solucao_aleatoria)
    return solucao_aleatoria
solucaoinicial = gerasolucao()
solucaofinal, cost = annealing(solucaoinicial)
print(solucaofinal, "Solução final da rota\n", cost,"Custo final da rota")
