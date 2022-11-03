# Faça um programa em Python que abra e reproduza o áudio de
# um arquivo mp3

import pygame
# iniciando o pygame
pygame.init()
# chamando a música
pygame.mixer.music.load("021.mp3")
# dando play na música
pygame.mixer.music.play()
# comando input() para reproduzir a música
# tendo em vista que houve atualização no pygame
# e só o comando acima não reproduz a música de fato
input()
# finaliza a reprodução
pygame.event.wait()
