from pygame.sprite import Group
import sys
import pygame
from config import Config
from ship import Ship
import game_functions as gf


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

    #Game loop
    while True:
        gf.verify_events(conf, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(conf, screen, ship, bullets)  

run_game()
