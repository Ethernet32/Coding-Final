import pygame
from math import atan2, degrees
from player import *

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