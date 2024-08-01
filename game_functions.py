import sys
import pygame
from config import config
from ship import Ship

def verify_events(ship:Ship):
    """Response for the keyboard and mouse events"""

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_RIGHT:
                      ship.rect.centerx += 1
                 elif event.key == pygame.K_LEFT:
                      ship.rect.centerx -= 1
                      

def update_screen(config:config, screen, ship:Ship):
    """Update the screen and show the new screen"""

    screen.fill(config.bg_color)
    ship.blitme()
    pygame.display.flip()