import pygame
import sys
from game import *

screen = pygame.display.set_mode((850, 750))

game = Game()
game.resize_images()
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame. MOUSEBUTTONDOWN:
            game.add_bullet(screen)
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_d]:
        game.move_right()
    if pressed[pygame.K_a]:
        game.move_left()
    if pressed[pygame.K_w]:
        game.move_up()
    if pressed[pygame.K_s]:
        game.move_down()
    
    
    game.show_floor(screen)
    game.show_bullets
    if pygame.mouse.get_focused():
        game.point_at(*pygame.mouse.get_pos())
    game.show_player(screen)

    pygame.display.update()
    clock.tick(120)
