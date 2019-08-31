import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """ Class represents a singel alien ship"""

    def __init__(self, ai_settings,screen):
        """ In"""
        super(Alien, self).__init__()
        self.screen = screen
        self.add_settings = ai_settings

        # Loading the alien image and define it location
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()

        # Setting the alien ship in top left corner of a screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien x cooridate
        self.x = float(self.rect.x)

    def blitme(self):
        """ Displaying alien ship in its location"""
        self.screen.blit(self.image,self.rect)