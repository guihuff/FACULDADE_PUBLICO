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

def menorEntre2(m, teste):
    # print("Testando : ", m )
    bau = 0
    if(novo_dicionario[m]):
        bau = 5
    if (hRef(m)-bau) < teste:
        return True
    else:
        return False

def gulosa(grafo, root):
    candidatos = [root]
    visited = set()
    visited.add(root)

    par = {}  # par contém um mapeamento adjacente de todos os nós
    par[root] = root

    while(len(candidatos) > 0):
        father = candidatos[0]
        # print(father, ":= ", candidatos)
        del candidatos[0]
        # print(father, ": ", candidatos)

        if isGoal(father):  # se o nó atual é a parada então começamos de novo do início
            res = []

            for x in par: # Passando pela lista de vizitas
                # print(x)
                res.append(int(x)) #Forçamdp ser int


            # print("Solução Gulosa", res, "Valor custo = ", conta)
            return res

        testar_valor_h = None
        anterior = None
        # print(grafo[father])
        for k in grafo[father]: #Olha os filhos do nó

            if testar_valor_h == None: #Recebe o valor de H do primeiro filho
                bau = 0
                if (novo_dicionario[k]):
                    bau = 5
                    novo_dicionario[k] = False
                testar_valor_h = hRef(k) - bau
                anterior = k
            else:
                if menorEntre2(k, testar_valor_h): #Verifica se o H é menor
                    bau = 0
                    if (novo_dicionario[k]):
                        bau = 5
                        novo_dicionario[k] = False
                    testar_valor_h = hRef(k) - bau
                    anterior = k


        visited.add(anterior)
        if anterior in par:#Se ja existe a chave então vira string
            par[str(anterior)] = father
        else:
            par[anterior] = father
        candidatos.append(anterior)
        # print(par)




# graph = graph
# resp_gulosa = gulosa(graph, 0)