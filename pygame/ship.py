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
        # self.rect.centery = self.screen_rect.centery
        #self.rect.midright = self.screen_rect.midright
        self.rect.bottom = self.screen_rect.bottom
        #A ship coordinate of ship's centre point is store in float
        self.center = float(self.rect.centerx)
        # self.center = float (self.rect.centery)

        # Different option of moving the space ship
        self.moving_right = False
        self.moving_left = False
        # self.moving_up = False
        # self.moving_down = False

    def update(self):
        """Updating ship's location based on a different option of movement"""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left >0:
            self.center -= self.ai_settings.ship_speed_factor
        # if self.moving_up and self.rect.top >0:
        #     self.center -= self.ai_settings.ship_speed_factor
        # if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
        #     self.center += self.ai_settings.ship_speed_factor

        # Updating object rect based on self.center value
        self.rect.centerx = self.center
        # self.rect.centery = self.center

    def blitme(self):
        """Displaying a space ship in its current location"""
        self.screen.blit(self.image,self.rect)