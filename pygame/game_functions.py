import sys

import pygame

from bullet import Bullet

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """ Event after clicking key"""
    if event.key == pygame.K_RIGHT:
        # Moving ship in right direction
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Moving ship in left direction
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        # Moving ship in left direction
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        # Moving ship in left direction
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings,screen, ship, bullets):
    """ Fire the bullet if the limit is not reached"""
    # Creating a new bullet and adding it to the group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def check_keyup_events(event,ship):
    """ Event after releasing key"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def update_bullets(bullets):
    """ Update bullets location and removing the bullets which goes outside the screen """

    #Update location of bullet
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))

def check_events(ai_settings,screen,ship,bullets):
    """ Reaction for mouse and keyboard events"""
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            sys.exit ()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


def update_screen(ai_settings, screen, ship,alien,bullets):
    """ Update a screen and going to a new screen"""
    # Screen refresh after every iteration
    screen.fill (ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme ()
    alien.blitme()
    # Displaying last modified screen
    pygame.display.flip ()