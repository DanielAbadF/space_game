from typing import Any
from pygame.sprite import Group, Sprite
import pygame
from config import Config
from ship import Ship

class Bullet(Sprite):
    """Class to manage the bullets shot by the ship"""

    def __init__(self, config:Config, screen, ship:Ship) -> None:
        super(Bullet,self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0, config.bullet_width, config.bullet_height)
        self.rect.centerx = ship.rect.centerx   
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
        self.color = config.bullet_color
        self.speed = config.bullet_speed_factor

    def update(self) -> None:
        """Moves the bullet to the upper part of the screen"""

        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
