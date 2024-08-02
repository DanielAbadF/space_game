import sys
import pygame
from config import Config
from ship import Ship
from bullet import Bullet

def verify_keyDown_events(event, configs, screen, ship:Ship, bullets):
     if event.key == pygame.K_RIGHT:
            ship.moving_right = True
     elif event.key == pygame.K_LEFT:
        ship.moving_left = True
     elif event.key == pygame.K_SPACE:
          fire_bullet(configs, screen, ship, bullets)
     elif event.key == pygame.K_q:
          sys.exit()

def verify_keyUp_events(event, ship:Ship):
     if event.key == pygame.K_RIGHT:
            ship.moving_right = False
     elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def verify_events(config, screen, ship:Ship, bullets):
    """Response for the keyboard and mouse events"""

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                 verify_keyDown_events(event, config, screen, ship, bullets)
            elif event.type == pygame.KEYUP:
                 verify_keyUp_events(event, ship)

def update_screen(config:Config, screen, ship:Ship, bullets):
    """Update the screen and show the new screen"""

    screen.fill(config.bg_color)
    ship.blitme()
    for bullet in bullets.sprites():
         bullet.draw_bullet()
    pygame.display.flip()\

def update_bullets(bullets):
     bullets.update()

     for bullet in bullets.copy():
          if bullet.rect.bottom <= 0:
               bullets.remove(bullet)

def fire_bullet(configs, screen, ship, bullets):
      if len(bullets) < configs.allowed_bullets:
               new_bullet = Bullet(configs, screen, ship)
               bullets.add(new_bullet)