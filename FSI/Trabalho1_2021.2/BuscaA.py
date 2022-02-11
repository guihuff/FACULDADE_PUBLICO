from Elementos import *

novo_dicionario = dict()

for i in casa:
    novo_dicionario[i] = casa[i][1]

def isGoal(s):
    if s == 76:
        return True
    else:
        return False

def hRef(n): #Heuristica definida, contagem de blocos no eixo x e y até o destino + uma soma para cada linha
    H = {
        0: 24, 1: 23, 2: 22, 3: 21, 4: 20, 5: 19,
        13: 18, 15: 16, 16: 15, 17: 16,
        21: 17, 22: 16, 23: 15, 26: 12, 27: 13, 29: 15,
        32: 14, 35: 10, 37: 11, 38: 12, 39: 13,
        40: 12, 41: 11, 42: 12, 43: 10, 44: 9, 45: 8, 47: 8,
        50: 10, 53: 7, 56: 4, 57: 5,
        60: 8, 61: 7, 62: 6, 63: 5, 64: 4, 65: 3, 66: 2,
        76: 0}

    return H[n]

def A_estrela(grafo, root):
    candidatos = [root] # É uma lista de nós que foram visitados, mas que os vizinhos nem sempre foram inspecionados, começa com o nó inicial
    visited = set() # É uma lista de nós que foram visitados e quem são os vizinhos sempre inspecionados

    poo = {} # poo tem distâncias presentes do início para todos os outros nós o valor padrão é +infinito
    poo[root] = 0

    par = {} # par contém um mapeamento adjacente de todos os nós
    par[root] = root

    while (len(candidatos) > 0):
        n = None
        # print(n, " = ", candidatos)

        for v in candidatos:  # ele encontrará um nó com o menor valor de f () -
            bau = 0
            if (novo_dicionario[v]): #Verifica se tem Bau para alterar a heuristica
                bau = 5
                novo_dicionario[v] = False
            if n == None or poo[v] + (hRef(v)-bau) < poo[n] + hRef(n):
                n = v

        if n == None:
            print('Caminho não existe!')
            return None
        if isGoal(n): # se o nó atual é a parada então começamos de novo do início
            res = []

            while par[n] != n:
                res.append(n)
                n = par[n]

            res.append(root)

            res.reverse()


            # print("Solução A*", res, "Valor custo = ", conta)
            return res

        for m in grafo[n]: # para todos os vizinhos do nó atual, faça
            peso = casa[m][0][0]
            if casa[m][1]:
                peso = peso - 5
            # se o nó atual não estiver presente em open_lst e closed_lst adicione-o a open_lst e observe n como é par
            if m not in candidatos and m not in visited:
                candidatos.append(m)
                par[m] = n
                poo[m] = poo[n] + casa[m][0][0]
            else: # caso contrário, verifique se é mais rápido visitar primeiro n, depois m
                if poo[m] > poo[n] + casa[m][0][0]: # E, se for, atualize os dados par e dados poo
                    poo[m] = poo[n] + casa[m][0][0]
                    par[m] = n

                    if m in visited: # E, se o nó estava no closed_lst, movemos para open_lst
                        visited.remove(m)
                        candidatos.append(m)

        candidatos.remove(n) # removemos n do open_lst
        visited.add(n) # E adicionamos ao closed_lst
        # Pois, todos os seus vizinhos foram inspecionados

# graph = graph
# respA = A_estrela(graph, 0)

