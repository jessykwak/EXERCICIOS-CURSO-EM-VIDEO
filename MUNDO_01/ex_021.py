# EXERCICIO 021:
# Faca um programa em python que abra e reproduza o audio de um arquivo mp3.

import pygame

musica = input('Digite o caminho do arquivo de musica: ')
pygame.mixer.init()  
pygame.mixer.music.load(musica)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy() == True:
    continue