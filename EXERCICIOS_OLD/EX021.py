import playsound

n = (input('Qual o caminho do arquivo da musica? '))
playsound.playsound(n)
print('played music using playsound')

'''import pygame

pygame.init()
n = (input('Qual o caminho do arquivo da musica? '))

pygame.mixer.music.load('n')
pygame.mixer.music.play()
pygame.event.wait()
print('played music using pygame')'''