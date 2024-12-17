
import pygame
import random
from math import *
import sys

pygame.init()
screen = pygame.display.set_mode((850, 750))

class Game(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ground = pygame.image.load('img/ground.png')
        self.groundrect = self.ground.get_rect()
        self.player_img = pygame.image.load('img/player.png')
        self.player = pygame.transform.scale(self.player_img, (64, 60))
        self.playerrect = self.player.get_rect()
        self.bullet_img = pygame.image.load('img/bullet.png')
        self.bullet = pygame.transform.scale(self.bullet_img, (20, 20))
        self.bulletrect = self.bullet.get_rect()
        self.bullet_list = []
        self.enemy_img = pygame.image.load('img\zom1.png')
        self.enemy = pygame.transform.scale(self.enemy_img, (90, 70))
        self.enemyrect = self.enemy.get_rect()
        self.enemy_list = []
        self.enemy_health = 1
        self.enemy_damage = 10
        self.floor_x = 0
        self.floor_y = 0
        self.font = pygame.font.SysFont('Arial', 48)
        self.health = 100
        self.player_damage = 1
        self.active = True
        self.rotated_image = self.player
        self.new_rect = self.playerrect
        self.rotated_enemy = self.enemy
        self.new_enemy_rect = self.enemyrect
        self.playerrect.center = (850/2,750/2)
        self.groundrect.center = ((2550/2, 2250/2))
        self.pointed = False
        self.enemy_spawn = [(-100, -100), (-100, 0), (-100, 100), (-100, 200), (-100, 300), (-100, 400), (-100, 500), (-100, 600), (-100, 700), (-100, 850), (0, -100), (100, -100), (200, -100), (300, -100), (400, -100), (500, -100), (600, -100), (700, -100), (800, -100), (950, -100), (950, 0), (950, 100), (950, 200), (950, 300), (950, 400), (950, 500), (950, 600), (950, 700), (950, 850), (-100, 850), (0, 850), (100, 850), (200, 850), (300, 850), (400, 850), (500, 850), (600, 850), (700, 850), (850, 850)]
        self.score = 0
        self.hurt = pygame.image.load('img/hurt.png')

    def resize_images(self):
        self.ground = pygame.transform.scale(self.ground, (2550, 2250))
        self.hurt = pygame.transform.scale(self.hurt, (2550, 2250))

    def show_floor(self, screen):
        screen.blit(self.ground, (self.floor_x - 850, self.floor_y - 850))

    def point_at(self, x, y):
        angle = atan2(y - self.playerrect.centery, x - self.playerrect.centerx)
        self.rotated_image = pygame.transform.rotate(self.player, degrees(-1 * (angle)))
        self.new_rect = self.rotated_image.get_rect(center=self.playerrect.center)

    def show_player(self, screen):
        screen.blit(self.rotated_image, self.new_rect.topleft)

    def add_bullet(self, x, y):
        dx = x - self.playerrect.centerx
        dy = y - self.playerrect.centery
        distance = sqrt(dx ** 2 + dy ** 2)
        slope_x = dx / distance
        slope_y = dy / distance
        bullet = self.bullet.get_rect(center=self.playerrect.center)
        self.bullet_list.append((bullet, slope_x, slope_y))

    def show_bullets(self, screen):
        for bullet, _, _ in self.bullet_list:
            screen.blit(self.bullet, bullet)

    def move_bullet(self):
        for index, (bullet, slope_x, slope_y) in enumerate(self.bullet_list):
            bullet.centerx += slope_x * 5
            bullet.centery += slope_y * 5
            if not screen.get_rect().colliderect(bullet):
                self.bullet_list.pop(index)

    def add_enemy(self, x, y):
        enemy = self.enemy.get_rect(center=random.choice(self.enemy_spawn))
        self.enemy_list.append(enemy)

    def show_enemy(self, x, y):
        for enemy in self.enemy_list:
            angle = atan2(y - enemy.centery, x - enemy.centerx)
            rotated_enemy = pygame.transform.rotate(self.enemy, degrees(-1 * angle))
            enemy_rect = rotated_enemy.get_rect(center=enemy.center)
            enemy.center = enemy_rect.center
            screen.blit(rotated_enemy, enemy_rect.topleft)

    def move_enemy(self):
        for enemy in self.enemy_list:
            dx = self.playerrect.centerx - enemy.centerx
            dy = self.playerrect.centery - enemy.centery
            distance = sqrt(dx ** 2 + dy ** 2)
            eslope_x = dx / distance
            eslope_y = dy / distance
            enemy.centerx += eslope_x * 2.5
            enemy.centery += eslope_y * 2.5

    def p_e_collision(self,screen):
        if self.health <= 0:
            self.active = False
        for enemy in self.enemy_list:
            if self.playerrect.colliderect(enemy):
                self.health -= self.enemy_damage
                self.enemy_list.remove(enemy)
                self.hurts(screen)
    def hurts(self,screen):
        screen.blit(self.hurt, (self.floor_x - 850, self.floor_y - 850))
        pygame.time.wait(10)
    
    def b_e_collision(self):
        for enemy in self.enemy_list:
            collide_list = enemy.collidelistall(self.bullet_list)
            if collide_list:
                print("hit")

    def show_score(self, game_state, screen, color):
        score_surface = self.font.render(str(self.score), True, color)
        score_rect = score_surface.get_rect(center = (202, 75))
        screen.blit(score_surface, score_rect)
        if game_state == "Game_Over":
            restart_text1 = self.font.render("Press Space Bar", True, color)
            restart_rect1 = restart_text1.get_rect(center=(200, 280))
            screen.blit(restart_text1, restart_rect1)
            restart_text2 = self.font.render("To Play Again", True, color)
            restart_rect2 = restart_text2.get_rect(center=(200, 340))
            screen.blit(restart_text2, restart_rect2)
            high_score_surface = self.font.render("High Score: {:d}".format(int(self.high_score)), True, color)
            high_score_rect = high_score_surface.get_rect(center = (200, 610))
            screen.blit(high_score_surface, high_score_rect)

    def move_right(self,speed):
        for i in range(speed):
            self.floor_x -= .5
            if self.floor_x <= -750:
                self.floor_x += 750
            for enemy in self.enemy_list:
                enemy.centerx -=.5

    def move_left(self,speed):
        for i in range(speed):
            self.floor_x += .5
            if self.floor_x >= 750:
                self.floor_x -= 750
            for enemy in self.enemy_list:
                enemy.centerx +=.5

    def move_up(self,speed):
        for i in range(speed):
            self.floor_y += .5
            if self.floor_y >= 750:
                self.floor_y -= 750
            for enemy in self.enemy_list:
                enemy.centery += .5

    def move_down(self,speed):
        for i in range(speed):
            self.floor_y -= .5
            if self.floor_y <= -750:
                self.floor_y += 750
            for enemy in self.enemy_list:
                enemy.centery -= .5
