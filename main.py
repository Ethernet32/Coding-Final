import pygame
import sys
from game import *
from fractions import Fraction

screen = pygame.display.set_mode((850, 750))
game = Game()
game.resize_images()
clock = pygame.time.Clock()

SPAWNENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWNENEMY, 1000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            game.add_bullet(*pygame.mouse.get_pos())

        if pygame.mouse.get_focused():
            game.point_at(*pygame.mouse.get_pos())

        if event.type == SPAWNENEMY:
            game.add_enemy(850/2, 750/2)
        

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_d]:
        if pressed[pygame.K_w] or pressed[pygame.K_s] or pressed[pygame.K_a]:
            game.move_right(3)
        else:
            game.move_right(4)
    if pressed[pygame.K_a]:
        if pressed[pygame.K_w] or pressed[pygame.K_s] or pressed[pygame.K_d]:
            game.move_left(3)
        else:
            game.move_left(4)
    if pressed[pygame.K_w]:
        if pressed[pygame.K_d] or pressed[pygame.K_s] or pressed[pygame.K_a]:
            game.move_up(3)
        else:
            game.move_up(4)
    if pressed[pygame.K_s]:
        if pressed[pygame.K_d] or pressed[pygame.K_w] or pressed[pygame.K_a]:
            game.move_down(3)
        else:
            game.move_down(4)
    
    if game.active == True:
        game.show_floor(screen)
        game.show_bullets(screen)
        game.move_bullet()
        game.move_enemy()
        game.show_enemy(850/2, 750/2)
        game.show_player(screen)
        game.p_e_collision()
        game.b_e_collision()

    pygame.display.update()
    clock.tick(120)
