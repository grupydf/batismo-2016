import pygame  # importa biblioteca de jogos

pygame.init()  # inicializa o jogo
# clock = pygame.time.Clock()

# Tamanho e nome da janela
tela = pygame.display.set_mode([700, 497])
pygame.display.set_caption("Meu jogo!")

jogador_x = 300
jogador_y = 400

bola_x = 200
bola_y = 100

bola_descendo = True
bola_para_direita = True
acabou = False

pontos = 0
letras = pygame.font.SysFont(None, 55)

while not acabou:

    tela.fill([0, 0, 0])

    # desenha a pontuação
    placar = letras.render(str(pontos), True, [255, 255, 255])
    tela.blit(placar, [350, 20])

    if bola_descendo:
        bola_y = bola_y + 0.1
    else:
        bola_y = bola_y - 0.1
    # se passar da tela, volta!
    if bola_y <= 0:
        bola_descendo = True

    if bola_para_direita:
        bola_x = bola_x + 0.1
    else:
        bola_x = bola_x - 0.1
    # se passar da tela, volta!
    if bola_x >= 700:
        bola_para_direita = False
    if bola_x <= 0:
        bola_para_direita = True


    jogador = pygame.Rect(jogador_x, jogador_y, 80, 20)
    pygame.draw.rect(tela, [255, 255, 255],jogador)
    bola = pygame.Rect(bola_x, bola_y, 20, 20)
    pygame.draw.rect(tela, [255, 255, 255],bola)

    if jogador.colliderect(bola):
        bola_descendo = False
        pontos = pontos + 1

    pygame.display.flip()

    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jogador_x = jogador_x - 10
            if evento.key == pygame.K_RIGHT:
                jogador_x = jogador_x + 10
        if evento.type == pygame.QUIT:
            acabou = True


















