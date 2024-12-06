import pygame
from game import *
import sys
screen = pygame.display.set_mode((850, 750))

game = Game()
game.resize_images()
clock = pygame.time.Clock() 


game.show_floor(screen)
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEMOTION:
            game.point_at(*pygame.mouse.get_pos())


    # wn.blit(tank, Player)
    pygame.display.update()
    clock.tick(120)
