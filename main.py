import pygame
from math import atan2, degrees
from game import *
wn = pygame.display.set_mode((850, 750))

player = Player()
player.resize_image()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEMOTION:
            player.point_at(*pygame.mouse.get_pos())

    # wn.blit(tank, Player)
    pygame.display.update()

