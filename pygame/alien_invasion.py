

import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def run_game():
    #initializing a space ship and its location
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Space Invasion")


    # Creating an space ship
    ship = Ship(ai_settings,screen)

    # Creating an alien ship
    #alien = Alien(ai_settings, screen)
    aliens = Group()

    bullets = Group ()

    # Creating the alien group
    gf.create_fleet(ai_settings,screen,ship,aliens)

    # Main loop.
    while True:

        #
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings,aliens)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)


run_game()
