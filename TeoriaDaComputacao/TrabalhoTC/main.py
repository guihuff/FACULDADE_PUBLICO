#Guilherme Huff
#Problema da Mochila Inteira

def max(x, y):
    if(x > y):
        return x
    else:
        return y

def achSolucao(B, L):
    resp = []
    i = len(B)-1
    peso = len(B[0])-1
    print(B[i][peso])
    while i > 0:
        if (B[i][peso] == (L[i][0] + B[i-1][peso - L[i][1]])):
            resp.append(i)
            peso = peso - L[i][1]
        i -= 1
    return(resp)

def resMochila(L, W, B, n):
    for i in range(W + 1):
        B[0][i] = 0

    for i in range(1, n+1):
        for j in range(W+1):
            if (L[i][1] > j):
                B[i][j] = B[i-1][j]
            else:
                x = L[i][0] + B[i-1][j-L[i][1]]
                y = B[i-1][j]
                B[i][j] = max(x, y)


    return (B, achSolucao(B, L))



W = int(input("Peso Mochila: "))
n = int(input("Quantidade de itens: "))
L = {0:[0,0]}

for i in range(n):
    print("item:", i+1)
    v = int(input("Valor do Item: "))
    p = int(input("Peso: "))
    lista = [v, p]
    L[i+1] = lista

# W = 6
# n = 7
# L = {0:[0,0], 1:[60,1], 2:[150, 3], 3:[120, 3], 4:[160,4], 5:[200, 5], 6:[150, 5], 7:[60,6]}

B = [[None for i in range(W+1)] for j in range(n+1)]


pronto = resMochila(L, W, B, n)

for i in pronto[0]:
    print(i)
print("Lista de itens: Item:[Valor, peso]", L)
print("Itens a serem levador: ", pronto[1])
