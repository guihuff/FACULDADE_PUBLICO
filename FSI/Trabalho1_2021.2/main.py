import pygame
from Elementos import casa
from Busca import *
from BuscaA import *
from BuscaGulosa import *


nos = casa


class personagem(pygame.sprite.Sprite): #Personagem
    def __init__(self, string):
        pygame.sprite.Sprite.__init__(self)
        self.Imagem = pygame.image.load(string)
        self.rect =self.Imagem.get_rect()


    def colorcar(self, superfice, x, y):
        self.rect.centerx = x+15
        self.rect.centery = y+15
        superfice.blit(self.Imagem, self.rect)


def DrawJogo(res): #Desenha o Jogo

    pygame.init() #inicio da biblioteca Pygames
    dis = pygame.display.set_mode((500, 300)) #Display
    clock = pygame.time.Clock() #Tempo
    velocidade = 2 #Velocidade
    posicao = 0 #Posicao
    contagem = 0 #Contagem de pontos
    baus = 0 #Contagem de Baus cada bau é -5
    score_font = pygame.font.SysFont("comicsansms", 25) # DEclaração da fonte
    pygame.display.set_caption('Tabuleiro')  # Nome da tela
    jogador = personagem('img/perso.png')  # Objeto jogador
    bau_tesouro = personagem('img/pngwing.com.png')  # Objeto bau
    game_over = False  # Loop de continuação

    def score(soma):    # Função de somar o score e imprimir
        valor = score_font.render("Custo: " + str(soma) + " Baus: " + str(baus), True, (255, 255, 255))
        dis.blit(valor, [0, 250])   #Mostra na tela



    while not game_over:

        dis.fill((0, 0, 0)) # Reseta tabuleiro

        for event in pygame.event.get(): #Verifica se o jogo foi fechado
            if event.type == pygame.QUIT:
                game_over = True


        for i in nos:       #Desenha o Mapa
            pygame.draw.rect(dis, nos[i][0][1], [nos[i][3]*35, nos[i][2]*35, 35, 35])
            if nos[i][1]:       #Desenha os Baus
                bau_tesouro.colorcar(dis, nos[i][3]*35, nos[i][2]*35)
        pygame.draw.rect(dis, (200, 200, 200), [nos[76][3] * 35, nos[76][2] * 35, 35, 25])


        if len(res) > 0:  #Verifica se ainda tem resposta
            posicao = res[0]    #Pega a posição do personagem
            del res[0]      #Remove
            contagem = contagem + nos[posicao][0][0] # faz a contagem de pontos
            if nos[posicao][1]:
                contagem = contagem - 5
                baus = baus + 1
                nos[posicao][1] = False  # remove se o personagem passou por um Bau
        jogador.colorcar(dis, nos[posicao][3]*35, nos[posicao][2]*35)
        score(contagem) #Chama a função de imprimir contagem



        pygame.display.update() #Update do display



        
        

        clock.tick(velocidade)  #velociade


    pygame.quit()
    quit()


def DrawMenu(resp):  # Desenha o Jogo




    pygame.init()  # inicio da biblioteca Pygames
    dis = pygame.display.set_mode((500, 300))  # Display

    score_font = pygame.font.SysFont("comicsansms", 25)  # DEclaração da fonte
    pygame.display.set_caption('Menu')  # Nome da tela

    def texto(String, x, y):  # Função score e imprimir
        valor = score_font.render(str(String), True, (255, 255, 255))
        dis.blit(valor, [x, y])  # Mostra na tela

    game_over = False  # Loop de continuação
    while not game_over:

        dis.fill((0, 0, 0))  # Reseta tabuleiro

        texto("Pressione as setas para escolher o método", 0, 40)
        texto("ESQUERDA = Busca em Largura", 40, 70)
        texto("CIMA = Busca em Profundidade", 40, 100)
        texto("DIREITA = A*", 40, 130)
        texto("BAIXO = Gulosa", 40, 160)


        for event in pygame.event.get():  # Verifica se o jogo foi fechado
            if event.type == pygame.QUIT:
                game_over = True

            comandos = pygame.key.get_pressed()
            if comandos[pygame.K_LEFT]:
                DrawJogo(resp[0])
            if comandos[pygame.K_UP]:
                DrawJogo(resp[1])
            if comandos[pygame.K_RIGHT]:
                DrawJogo(resp[2])
            if comandos[pygame.K_DOWN]:
                DrawJogo(resp[3])


        pygame.display.update()  # Update do display

    pygame.quit()
    quit()

# print(resposta_dfs)
# print("Digite qual vai ser o metodo 0-BL, 1-BP, 2-A*")
# teste = int(input('Digite AQUI: '))
grafo_final = graph
resp = [bfs(grafo_final, 0), dfs(grafo_final, 0), A_estrela(grafo_final, 0), gulosa(grafo_final, 0)]
DrawMenu(resp)
# DrawJogo(resp[0])
# DrawJogo(resp[1])
# DrawJogo(resp[2])