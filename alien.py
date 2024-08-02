import pygame
import sys
from pygame.sprite import Group, Sprite
from config import Config

class Alien(Sprite):
    """Represent an alien ship"""

    def __init__(self, config:Config, screen) -> None:
        super(Alien, self).__init__()
        self.screen = screen
        self.config = config
        self.image = pygame.image.load('images/Alien.jpg')
        self.rect = self.image.get_rect()

        self.rect.left = 0
        self.rect.y = 0

        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien in his current location"""

        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += self.config.alien_speed_factor * self.config.fleet_direction
        self.rect.x = int(self.x)

    def check_edges(self):
        """Returns true if the alien in a border of the screen"""

        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0
