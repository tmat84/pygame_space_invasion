import sys

import pygame

from bullet import Bullet
from alien import Alien

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """ Event after clicking key"""
    if event.key == pygame.K_RIGHT:
        # Moving ship in right direction
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Moving ship in left direction
        ship.moving_left = True
    # elif event.key == pygame.K_UP:
    #     # Moving ship in left direction
    #     ship.moving_up = True
    # elif event.key == pygame.K_DOWN:
    #     # Moving ship in left direction
        #ship.moving_down = True
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

def get_number_aliens_x(ai_settings,alien_width):
    # Creating alien and indicate their number in the row
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x / (2*alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """ Determine how many rows will fit the screen"""
    available_space_y = (ai_settings.screen_height-
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number,row_number):
    """ Creating alien and setting in it in the row"""
    alien = Alien (ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add (alien)


def create_fleet(ai_settings,screen,ship,aliens):
    """ Creating aliens group"""
        # The distance between the aliens is equal to a width of a alien
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows (ai_settings, ship.rect.height, alien.rect.height)
    # Creating the first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # Creating an alien and setting it in the row
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

def check_fleet_edges(ai_settings, aliens):
    """ Right reaction when alien comes to edge """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    """ Move the whole fleet down and change the movement direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_events(ai_settings,screen,ship,bullets):
    """ Reaction for mouse and keyboard events"""
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            sys.exit ()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


def update_screen(ai_settings, screen, ship,aliens,bullets):
    """ Update a screen and going to a new screen"""
    # Screen refresh after every iteration
    screen.fill (ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme ()
    aliens.draw(screen)
    # Displaying last modified screen
    pygame.display.flip ()

def update_functions(aliens):
     aliens.update ()

def update_aliens(ai_settings,aliens):
    """ Update locatiozation evevry ship in the fleet"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
