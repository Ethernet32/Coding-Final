import pygame
import sys
from game import *
from fractions import Fraction
pygame.init()
screen = pygame.display.set_mode((850, 750))
speed = 0
game = Game()
game.resize_images()
clock = pygame.time.Clock()
color = (255,255,255)
SPAWNENEMY = pygame.USEREVENT + 1
SPEEDUP = pygame.USEREVENT + 4
SPAWNUP = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWNUP, 3000)
pygame.time.set_timer(SPEEDUP, 3000)
pygame.time.set_timer(SPAWNENEMY, random.randint(800-speed, 1500-speed))
start_screen = True
game.start(screen)
level = 1


while start_screen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            start_screen = False

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
        
        if event.type == SPAWNUP:
            speed += 1

        if game.score == 10*level:
            if level < 3:
                level += 1
            game.enemy = pygame.image.load(f'img/zom{level}.png')
            game.enemy_damage = random.randint(5*level, 16)
        
        if event.type == SPEEDUP:
            if game.espeed < 10:
                game.espeed += .1
            
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
        if pressed[pygame.K_w] or pressed[pygame.K_UP] or pressed[pygame.K_s] or pressed[pygame.K_DOWN] or pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
            game.move_right(3)
        else:
            game.move_right(4)
    if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
        if pressed[pygame.K_w] or pressed[pygame.K_UP] or pressed[pygame.K_s] or pressed[pygame.K_DOWN] or pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
            game.move_left(3)
        else:
            game.move_left(4)
    if pressed[pygame.K_w] or pressed[pygame.K_UP]:
        if pressed[pygame.K_d] or pressed[pygame.K_RIGHT] or pressed[pygame.K_s] or pressed[pygame.K_DOWN] or pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
            game.move_up(3)
        else:
            game.move_up(4)
    if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
        if pressed[pygame.K_d] or pressed[pygame.K_RIGHT] or pressed[pygame.K_w] or pressed[pygame.K_UP] or pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
            game.move_down(3)
        else:
            game.move_down(4)
    if pressed[pygame.K_SPACE] and game.active == False:
            game.active = True
            game.enemy = pygame.image.load('img/zom1.png')
            level = 1
            game.bullet_list = []
            game.enemy_list = []
            game.health = 100
            game.score = 0
            game.espeed = 2.5

            

    if game.active == True:
        game.show_floor(screen)
        game.p_e_collision(screen)
        game.show_bullets(screen)
        game.move_bullet()
        game.move_enemy()
        game.show_enemy(850/2, 750/2)
        game.show_player(screen)
        game.b_e_collision()
        game.show_score("playing", screen, (255,255,255))
        game.display_health(screen)
    else:
        screen.fill((0, 0, 0))
        game.update_high_score()
        restart_text1 = game.font.render("Press Space Bar", True, color)
        restart_rect1 = restart_text1.get_rect(center=(850/2, 280))
        screen.blit(restart_text1, restart_rect1)
        restart_text2 = game.font.render("To Play Again", True, color)
        restart_rect2 = restart_text2.get_rect(center=(850/2, 340))
        screen.blit(restart_text2, restart_rect2)
        high_score_surface = game.font.render("High Score: {:d}".format(int(game.high_score)), True, color)
        high_score_rect = high_score_surface.get_rect(center = (850/2, 510))
        screen.blit(high_score_surface, high_score_rect)


    pygame.display.update()
    clock.tick(120)
