import pygame
import sys
from settings import Settings


class Ship():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/ship1.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # center
        self.center = float(self.rect.centerx)

        # move标记
        self.moving_RIGHT = False
        self.moving_LEFT = False

    def update(self):

        if self.moving_RIGHT and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_LEFT and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
