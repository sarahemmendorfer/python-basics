import socket
import pygame

pygame.init() #inicia o pygame
pygame.mixer.music.load('msn.mp3') #carrega arquivo
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 12000))

while True:
    message, address = server_socket.recvfrom(1024)
    pygame.mixer.music.play()
    print(message)
    message = input("resposta: ")
    server_socket.sendto(message.encode('utf-8'), address)