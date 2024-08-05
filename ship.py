import pygame
from config import Config

class Ship:
    """Manages the ship behavior"""

    def __init__(self, config:Config,screen) -> None:
        """Initialice the ship and stablish its start point"""
        self.screen  = screen
        self.config = config
        self.image = pygame.image.load('images/Ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.x = self.rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

        self.center = float(self.rect.centerx)

    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if(self.moving_right and self.rect.right < self.screen_rect.right):
            self.x += self.config.speed_ship_factor 
        if(self.moving_left and self.rect.left > self.screen_rect.left):
            self.x -= self.config.speed_ship_factor
        self.rect.centerx = self.x