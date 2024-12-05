import pygame
from math import atan2, degrees


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.floor = pygame.image.load('img\ground.png')
        self.image = pygame.image.load('img/player.png')
        self.x = 0
        self.y = 0
        self.rect = self.image.get_rect()
        self.health = 100
    def resize_images(self):
        self.image = pygame.transform.scale(self.image, (60,60))
        self.image = pygame.transform.scale(self.image, (850, 750))

    def point_at(self, x, y):
        rotated_image = pygame.transform.rotate(self.image, degrees(atan2(x-self.rect.x, y-self.rect.y)))
        new_rect = rotated_image.get_rect(center=self.rect.center)
        wn.fill((255, 255, 255))
        wn.blit(rotated_image, new_rect.topleft)