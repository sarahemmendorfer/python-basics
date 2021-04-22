#ctrl c + ctrl v no arquivo mp3 (add na lista na esquerda)
import pygame
pygame.init() #inicia o pygame
pygame.mixer.music.load('nomedomp3') #carrega arquivo
pygame.mixer.music.play() #inicia a
pygame.event.wait()#fecha o programa qdo a musica acaba