import sys
import pygame
from config import Config
from ship import Ship
from bullet import Bullet
from alien import Alien
from pygame.sprite import Group

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

def update_screen(config:Config, screen, ship:Ship, aliens:Group, bullets:Group):
    """Update the screen and show the new screen"""

    screen.fill(config.bg_color)
    ship.blitme()
    aliens.draw(screen)
    for bullet in bullets.sprites():
         bullet.draw_bullet()
    pygame.display.flip()

def update_bullets(bullets):
     bullets.update()

     for bullet in bullets.copy():
          if bullet.rect.bottom <= 0:
               bullets.remove(bullet)

def update_aliens(configs, aliens:Group):
      check_fleet_edges(configs, aliens)
      aliens.update()

def fire_bullet(configs, screen, ship, bullets):
      if len(bullets) < configs.allowed_bullets:
               new_bullet = Bullet(configs, screen, ship)
               bullets.add(new_bullet)

def change_fleet_direction(config:Config, aliens:Group):
     for alien in aliens.sprites():
          alien.rect.y += config.fleet_drop_speed

     config.fleet_direction = config.fleet_direction * -1

def check_fleet_edges(config:Config, aliens:Group):
     for alien in aliens.sprites():
          if alien.check_edges():
               change_fleet_direction(config, aliens)
               return

def get_number_aliens_row(config, alien_width):
     avariable_space_x = config.screen_width - 2 * alien_width
     return int(avariable_space_x / (2 * alien_width))

def get_number_aliens_column(config:Config, ship_height, alien_height):
     avariable_space_y = config.screen_heigth - 3 * alien_height - ship_height
     return int(avariable_space_y / (2 * alien_height))

def create_alien(conf, screen, aliens, alien_number, row_number):
     alien = Alien(conf, screen)
     alien.rect.left = (2 * alien.rect.width * alien_number) + alien.rect.width
     alien.x = (2 * alien.rect.width * alien_number) + alien.rect.width
     alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number 
     aliens.add(alien)

def create_fleet(conf, screen, ship:Ship, aliens):
     """Creates an entire alien fleet"""

     alien = Alien(conf, screen)
     number_aliens_row = get_number_aliens_row(conf, alien.rect.width)
     number_of_rows = get_number_aliens_column(conf, ship.rect.height, alien.rect.height)
     #Creates an alien row
     for col in range(number_aliens_row):
          for row in range(number_of_rows):
               create_alien(conf, screen, aliens, col, row)