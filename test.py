import pygame
pygame.init()

def f():
    music = pygame.mixer.music.load("music.mp3")

    pygame.mixer.music.play(-1) # -1 will ensure the song keeps looping
