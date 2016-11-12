#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

# Inicialização do pygame
pygame.init()
clock = pygame.time.Clock()

# Tamanho e nome da janela
tela = pygame.display.set_mode([700, 497])
pygame.display.set_caption("Passo 2")

# Jogador
player_x = 350  # Posiçao inicial
player_y = 450

# bola
bola_x = 350
bola_y = 250

ciclo = 0

while ciclo < 100:

    # define o jogador (retângulo)
    player_area = pygame.Rect(player_x, player_y, 80, 15)
    # desenha o jogador
    pygame.draw.rect(tela, [255,255,255], player_area)

    # define a bola
    area_bola = pygame.Rect(bola_x, bola_y, 15, 15)
    # desenha a bola
    pygame.draw.rect(tela, [255,255,255], area_bola)

    # Atualiza o fundo
    pygame.display.flip()
    clock.tick(60)
    ciclo += 1
