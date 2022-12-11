# Abrir um arquivo mp3 e reproduzir
# 'C:\Users\leand\Music\abc.mp3'
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
