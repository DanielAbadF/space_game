from pygame.sprite import Group
import sys
import pygame
from config import Config
from ship import Ship
import game_functions as gf
from alien import Alien
from game_stats import Stats 
from button import Button

def run_game():
    pygame.init()
    conf = Config()
    screen = pygame.display.set_mode((conf.screen_width,conf.screen_heigth))
    pygame.display.set_caption("Invasion alienigena")

    #Stablish background color
    bg_color = conf.bg_color


    #Game start button
    play_button = Button(conf, screen, "Play")

    #Game stats
    stats = Stats(conf)
    #Create a ship
    ship = Ship(conf, screen)
    #Group to store bullets 
    bullets = Group()
    #Create an alien fleet
    aliens = Group()

    gf.create_fleet(conf, screen, ship, aliens)


    #Game loop
    while True:
        gf.verify_events(conf, screen, stats, play_button, aliens, ship, bullets)
        if stats.game_active:       
            ship.update()
            gf.update_bullets(conf, screen, ship, aliens, bullets)
            gf.update_aliens(conf, stats, screen, ship, aliens, bullets )  
        gf.update_screen(conf, screen, stats, ship, aliens, bullets, play_button)  
    
run_game()
