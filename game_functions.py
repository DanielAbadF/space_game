import sys
import pygame
from config import Config
from ship import Ship
from bullet import Bullet
from alien import Alien
from pygame.sprite import Group
from time import sleep
from button import Button
from game_stats import Stats

def verify_keyDown_events(event, configs:Config, screen, ship:Ship, bullets:Group):
     if event.key == pygame.K_RIGHT:
            ship.moving_right = True
     elif event.key == pygame.K_LEFT:
        ship.moving_left = True
     elif event.key == pygame.K_SPACE:
          fire_bullet(configs, screen, ship, bullets)
     elif event.key == pygame.K_q:
          sys.exit()
    

def check_play_button(config, screen, stats:Stats, play_button, ship:Ship, aliens:Group, bullets:Group, mouse_x, mouse_y):
     if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
          pygame.mouse.set_visible(False)
          stats.reset_stats()
          stats.game_active = True
          aliens.empty()
          bullets.empty()
          create_fleet(config, screen, ship, aliens)
          ship.center_ship()


def verify_keyUp_events(event, ship:Ship):
     if event.key == pygame.K_RIGHT:
            ship.moving_right = False
     elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def verify_events(config, screen, stats, play_button,aliens:Group, ship:Ship, bullets:Group):
    """Response for the keyboard and mouse events"""

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                 verify_keyDown_events(event, config, screen, ship, bullets)
            elif event.type == pygame.KEYUP:
                 verify_keyUp_events(event, ship)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                 mouse_x, mouse_y = pygame.mouse.get_pos()
                 check_play_button(config, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def update_screen(config:Config, screen, stats:Stats, ship:Ship, aliens:Group, bullets:Group, play_button:Button):
    """Update the screen and show the new screen"""

    screen.fill(config.bg_color)
    ship.blitme()
    aliens.draw(screen)
    for bullet in bullets.sprites():
         bullet.draw_bullet()
    if not stats.game_active:
         play_button.draw_button() 
    pygame.display.flip()

    

def update_bullets(conf, screen, ship, aliens, bullets:Group):
     bullets.update()
     remove_bullets_out(bullets)
     check_alien_bullet_collisions(bullets, aliens)
     new_fleet_if_empty(conf, screen, ship, aliens, bullets)

def remove_bullets_out(bullets:Group):
     for bullet in bullets.copy():
          if bullet.rect.bottom <= 0:
               bullets.remove(bullet)

def check_alien_bullet_collisions(aliens, bullets):
     pygame.sprite.groupcollide(bullets, aliens, True, True)

def new_fleet_if_empty(conf, screen, ship, aliens, bullets):
     if(len(aliens) == 0):
          bullets.empty()
          create_fleet(conf, screen, ship, aliens)

def ship_chashed(stats, config, screen, ship, aliens, bullets):
     """Response for the crash of the ship and an alien"""
     if stats.ships_left > 0:
          stats.ships_left -= 1

          aliens.empty()
          bullets.empty()

          #Creates a new fleet and center the ship
          create_fleet(config, screen, ship, aliens) 
          ship.center_ship()
          sleep(0.5)
     else:
          stats.game_active = False
          pygame.mouse.set_visible(True)

def check_aliens_bottom(config, stats, screen, ship, aliens, bullets):
     screen_rect = screen.get_rect() 

     for alien in aliens.sprites():
          if alien.rect.bottom >= screen_rect.bottom:
               ship_chashed(stats, config, screen, ship, aliens, bullets)
               break

def update_aliens(configs, stats, screen,ship, aliens:Group, bullets):
      check_fleet_edges(configs, aliens)
      aliens.update()
      if(pygame.sprite.spritecollideany(ship, aliens)):
           ship_chashed(stats, configs, screen, ship, aliens, bullets)     

      check_aliens_bottom(configs, stats, screen, ship, aliens, bullets)

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