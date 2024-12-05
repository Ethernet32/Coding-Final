import pygame
import random

class Game:
    def __init__(self, bird_img, pipe_img, background_img, ground_img):
        self.bird = pygame.image.load(bird_img).convert_alpha()

        self.pipe = pygame.image.load(pipe_img).convert_alpha()
        self.background = pygame.image.load(background_img).convert_alpha()
        self.ground = pygame.image.load(ground_img).convert_alpha()
        self.ground_position = 0
        self.active = True
        self.bird_movement = 0
        self.rotated_bird = pygame.Surface((0,0))
        self.pipes = []
        self.pipe_height = [280, 425, 562]
        self.score = 0
        self.font = pygame.font.SysFont(None, 48)
        self.high_score = 0

    def resize_images(self):
        self.bird = pygame.transform.scale(self.bird, (51,34))
        self.pipe = pygame.transform.scale(self.pipe, (80,439))
        self.background = pygame.transform.scale(self.background, (400,700))
        self.ground = pygame.transform.scale(self.ground, (470,160))
        self.bird_rect = self.bird.get_rect(center = (70,180))