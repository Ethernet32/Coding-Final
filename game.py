
import pygame
from math import atan2, degrees
screen = pygame.display.set_mode((850, 750))

class Game(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ground = pygame.image.load('img/ground.png')
        self.groundrect = self.ground.get_rect()
        self.player = pygame.image.load('img/player.png')
        self.playerrect = self.player.get_rect()
        self.bullet = pygame.image.load('img/bullet.png')
        self.bullet_list = []
        self.rbullet = []
        self.bulletrect = self.bullet.get_rect()
        self.floor_x = 0
        self.floor_y = 0
        self.health = 100
        self.active = True
        self.rotated_image = self.player
        self.new_rect = self.playerrect
        self.playerrect.center = (850/2, 750/2)
        self.groundrect.center = ((2550/2, 2250/2))
        self.enemy = pygame.image.load('img/zom1.png')
        self.enemy_list = []
        self.ri = pygame.image.load('img/bullet.png')
        self.new_r = self.bullet.get_rect()
    def resize_images(self):
        self.player = pygame.transform.scale(self.player, (64, 60))
        self.ground = pygame.transform.scale(self.ground, (2550, 2250))
        self.bullet = pygame.transform.scale(self.bullet, (10, 20))

    def show_floor(self, screen):
        screen.blit(self.ground, (self.floor_x-850, self.floor_y-850))

    def point_at(self, x, y):
        angle = atan2(y - self.playerrect.centery, x - self.playerrect.centerx)
        self.rotated_image = pygame.transform.rotate(self.player, degrees(-1*(angle)))
        self.new_rect = self.rotated_image.get_rect(center=self.playerrect.center)

    def show_player(self, screen):
        screen.blit(self.rotated_image, self.new_rect.topleft)

    def add_bullet(self):
        bullet = self.bullet.get_rect(center = self.playerrect.center)
        self.bullet_list.append(bullet)
        self.rbullet.append(bullet)

    def rotate_bullet(self, x, y):
        print("rotated")
        for bullet in self.rbullet:
            angle = atan2(y - bullet.centery, x - bullet.centerx)
            self.ri = pygame.transform.rotate(self.bullet, degrees(-1*(angle)))
            self.new_r = self.rotated_image.get_rect(center=bullet.center)
            print(f"bullet list {self.bullet_list}")
            print(f"rbullet list {self.rbullet}")
            self.rbullet.remove(bullet)

    def show_bullets(self, screen):
        if len(self.bullet_list) >= 1:
            for bullet in self.bullet_list:
                screen.blit(self.ri, bullet)

    def move_bullet(self):
        for bullet in self.bullet_list:
            bullet.centerx -= 1
            if bullet.centerx <= -40:
                self.bullet_list.remove(bullet)

    def move_right(self):
        self.floor_x -= 2
        if self.floor_x <= -750:
            self.floor_x += 750
        self.floor_x -= 2
        if self.floor_x <= -750:
            self.floor_x += 750
    def move_left(self):
        self.floor_x += 2
        if self.floor_x >= 750:
            self.floor_x -= 750
        self.floor_x += 2
        if self.floor_x >= 750:
            self.floor_x -= 750
    def move_up(self):
        self.floor_y += 2
        if self.floor_y >= 750:
            self.floor_y -= 750
        self.floor_y += 2
        if self.floor_y >= 750:
            self.floor_y -= 750
    def move_down(self):
        self.floor_y -= 2
        if self.floor_y <= -750:
            self.floor_y += 750
    def add_enemy(self):
        enemy = self.enemy.get_rect(midbottom = (30,30))
        self.bullet_list.append(enemy)
        print("add_enemy method")

    def show_enemy(self, screen):
        for enemy in self.enemy_list:
            screen.blit(self.enemy, enemy)
