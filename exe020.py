#faça um programa que abra e reproduza um arquivo de mp3

import pygame
pygame.init()
pygame.mixer.music.load('exe020.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)




