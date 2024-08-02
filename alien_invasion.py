from pygame.sprite import Group
import sys
import pygame
from config import Config
from ship import Ship
import game_functions as gf
from alien import Alien


def run_game():
    pygame.init()
    conf = Config()
    screen = pygame.display.set_mode((conf.screen_width,conf.screen_heigth))
    pygame.display.set_caption("Invasion alienigena")

    #Stablish background color
    bg_color = conf.bg_color

    #Create a ship
    ship = Ship(conf, screen)
    #Group to store bullets 
    bullets = Group()
    #Create an alien fleet
    aliens = Group()

    gf.create_fleet(conf, screen, ship, aliens)


    #Game loop
    while True:
        gf.verify_events(conf, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(conf, aliens)
        gf.update_screen(conf, screen, ship, aliens, bullets)  

run_game()
