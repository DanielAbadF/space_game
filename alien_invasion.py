import sys
import pygame
from config import config
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    conf = config()
    screen = pygame.display.set_mode((conf.screen_width,conf.screen_heigth))
    pygame.display.set_caption("Invasion alienigena")

    #Stablish background color
    bg_color = conf.bg_color

    #Create a ship
    ship = Ship(screen)

    #Game loop
    while True:
        gf.verify_events()
        screen.fill(bg_color)
        ship.blitme()
        pygame.display.flip()   

run_game()
