from Elementos import *

graph1 = graph

def isGoal(s):
    if s == 76:
        return True
    else:
        return False


def bfs(graph, root):
    candidatos = [root] # Fronteira de busca
    fathers = dict() # Armazenar os pais dos nós no caminho percorrido
    visited = set() # Armazena os nós já visitados para evitar loops
    visited.add(root)
    resposta = []


    while(len(candidatos) > 0): # Encerra a busca apenas com a fronteira vazia
        father = candidatos[0]
        # print("Candidatos: ", candidatos)
        del candidatos[0]
        # print("Visitado: ", father)

        if isGoal(father): # Se for um nó final
            res = [] # Acumula o caminho do começo até o nó final
            node = father # Começo a reconstruir o caminho a partir do nó final
            while node != root: # Volta no caminho até encontrar o nó inicial
                res.append(node)
                node = fathers[node]
            res.append(root)
            res.reverse()


            # print("Solução", res, "Valor custo = ", conta)
            resposta = res





        for son in graph[father]: # Para todos os nós, pega os filhos
            if son not in visited: # Para cada filho, verifica se já não foi visitado
                # print("Inserted = ", son, father)
                visited.add(son)
                fathers[son] = father
                candidatos.append(son)

    return resposta


# resposta_bfs = bfs(graph1, 0)


def dfs(graph, start):
    visitados = set()
    fathers = dict()

    def dfs_inter(grafo, vertice):
        visitados.add(vertice)

        if isGoal(vertice):
            res = []  # Acumula o caminho do começo até o nó final
            node = vertice  # Começo a reconstruir o caminho a partir do nó final
            while node != start:  # Volta no caminho até encontrar o nó inicial
                res.append(node)
                node = fathers[node]
            res.append(start)
            res.reverse()
            # print("Solução Profundidade", res, "Valor custo = ", conta)
            return res



        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                fathers[vizinho] = vertice
                resp = dfs_inter(grafo, vizinho)
                if resp is not None:
                    return resp

    return dfs_inter(graph, start)


# resposta_dfs = dfs(graph1, 0)