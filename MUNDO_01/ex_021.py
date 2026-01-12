# EXERCICIO 021:
# Faca um programa em python que abra e reproduza o audio de um arquivo mp3.

import pygame

pygame.init()
pygame.mixer.init()

musica = input('Digite o caminho do arquivo de musica: ')
  
pygame.mixer.music.load(musica)
pygame.mixer.music.play()

# pygame.event.wait() ->nao sei pq mas nao esta funcionando soh com event.wait
while pygame.mixer.music.get_busy() == True:
    continue