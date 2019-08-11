import pygame




class Ship():

    def __init__(self,ai_settings,screen):
        """ initializing a space ship and its location"""
        self.screen = screen
        self.ai_settings = ai_settings

        #Loading the space ship image and creating its rectangle.
        self.image = pygame.image.load('ship.BMP')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Setting every new ship in the bottom of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #A ship coordinate of ship's centre point is store in float
        self.center = float(self.rect.centerx)

        # Different option of moving the space ship
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updating ship's location based on a different option of movement"""

        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor
        # Updating object rect based on self.center value
        self.rect.centerx = self.center

    def blitme(self):
        """Displaying a space ship in its current location"""
        self.screen.blit(self.image,self.rect)