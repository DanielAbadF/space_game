import sys
import pygame

def verify_events():
    """Response for the keyboard and mouse events"""

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()