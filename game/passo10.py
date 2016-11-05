#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

# Inicialização do pygame
pygame.init()
clock = pygame.time.Clock()

# Tamanho e nome da janela
tela = pygame.display.set_mode([700, 497])
pygame.display.set_caption("Meu primeiro game")

# Jogador
player_x = 350  # Posiçao inicial
player_y = 450

# bola
bola_x = 150
bola_y = 250

# direção da bola
bola_descendo = True
bola_para_direita = True

parede_esquerda = pygame.Rect(0, 0, 15, 497)
parede_direita = pygame.Rect(685, 0, 700, 497)
teto = pygame.Rect(0, 0, 700, 15)

ciclo = 0
acabou = False
velocidade = 3
velocidade_jogador = 0

pontos = 0

letras = pygame.font.SysFont(None, 55)

while not acabou:

    # limpa a tela (preenche com preto)
    tela.fill([0, 0, 0])

    # desenha a pontuação
    pontuacao = letras.render(str(pontos), True, [255, 255, 255])
    tela.blit(pontuacao, [350, 20])

    # desenha paredes
    pygame.draw.rect(tela, [255,255,255], parede_esquerda)
    pygame.draw.rect(tela, [255,255,255], parede_direita)
    pygame.draw.rect(tela, [255,255,255], teto)

    # define o jogador (retângulo)
    jogador = pygame.Rect(player_x, player_y, 80, 15)
    # desenha o jogador
    pygame.draw.rect(tela, [255,255,255], jogador)

    # define a bola
    bola = pygame.Rect(bola_x, bola_y, 15, 15)
    # desenha a bola
    pygame.draw.rect(tela, [255,255,255], bola)

    # Atualiza o fundo
    pygame.display.flip()
    clock.tick(30)
    ciclo += 1

    # muda a posição da bola
    if bola_para_direita:
        bola_x += velocidade
    else:
        bola_x -= velocidade
    if bola_descendo:
        bola_y += velocidade
    else:
        bola_y -= velocidade

    # colisões
    if jogador.colliderect(bola) and bola_descendo:
        bola_descendo = False
        velocidade += 1
        pontos += 1
    if bola.colliderect(teto):
        bola_descendo = True
    if bola.colliderect(parede_direita):
        bola_para_direita = False
    if bola.colliderect(parede_esquerda):
        bola_para_direita = True

    player_x += velocidade_jogador

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            acabou = True
        # Apertar uma tecla
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocidade_jogador = -5 
            if event.key == pygame.K_RIGHT:
                velocidade_jogador = 5 
            if event.key == pygame.K_ESCAPE:
                acabou = True
        if event.type == pygame.KEYUP:
            velocidade_jogador = 0
