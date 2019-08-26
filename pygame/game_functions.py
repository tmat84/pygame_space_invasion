import sys

import pygame

def check_keydown_events(event,ship):
    """ Reaction on pressing the key"""
    if event.key == pygame.K_RIGHT:
        # Moving ship in right direction
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Moving ship in left direction
        ship.moving_left = True

def check_keyup_events(event,ship):
    """Reaction on letting the key"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    """ Reaction for mouse and keyboard events"""
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            sys.exit ()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


def update_screen(ai_settings, screen, ship):
    """ Update a screen and going to a new screen"""
    # Screen refresh after every iteration
    screen.fill (ai_settings.bg_color)
    ship.blitme ()
    # Displaying last modified screen
    pygame.display.flip ()