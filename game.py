import pygame
from math import atan2, degrees
screen = pygame.display.set_mode((850, 750))

class Game(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ground = pygame.image.load('img\ground.png')
        self.player = pygame.image.load('img\player.png')
        self.x = 0
        self.y = 0
        self.rect = self.player.get_rect()
        self.health = 100
        self.active = True

    def resize_images(self):
        self.player = pygame.transform.scale(self.player, (60,60))
        self.ground = pygame.transform.scale(self.ground, (850, 750))

    def point_at(self, x, y):
        rotated_image = pygame.transform.rotate(self.player, degrees(atan2(x-self.rect.x, y-self.rect.y)))
        new_rect = rotated_image.get_rect(center=self.rect.center)
        screen.blit(rotated_image, new_rect.topleft)
    
    def show_floor(self, screen):
        screen.blit(self.ground, (0,0))
    
    def show_player(self, screen):
        screen.blit(self.player,(0,0))
