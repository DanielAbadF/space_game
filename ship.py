import pygame
from config import config

class Ship:
    """Manages the ship behavior"""

    def __init__(self, config:config,screen) -> None:
        """Initialice the ship and stablish its start point"""
        self.screen  = screen

        self.image = pygame.image.load('images/Ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

        self.center = float(self.rect.centerx)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if(self.moving_right == True):
            self.rect.centerx += self.config.speed_ship_factor 
        if(self.moving_left == True):
            self.rect.centerx -= self.config.speed_ship_factor