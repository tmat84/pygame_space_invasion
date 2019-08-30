class Settings():
    """CLass is holding all game settings"""

    def __init__(self):
        """ Initializing a game settings"""
        # Game settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Setting connected to a space ship
        self.ship_speed_factor = 1.5

        #Settings connected to a bullet
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3
