import pygame

class ship:
    """Manages the ship behavior"""

    def __init__(self, screen) -> None:
        """Initialice the ship and stablish its start point"""
        self.screen  = screen

        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        return self.image.blit(self.image, self.rect)