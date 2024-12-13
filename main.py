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
        game.move_right(2)
    if pressed[pygame.K_a]:
        game.move_left(2)
    if pressed[pygame.K_w]:
        game.move_up(2)
    if pressed[pygame.K_s]:
        game.move_down(2)

    game.show_floor(screen)
    game.show_bullets(screen)
    game.move_bullet()
    game.move_enemy()
    game.show_enemy(850/2, 750/2)
    game.show_player(screen)

    pygame.display.update()
    clock.tick(120)
