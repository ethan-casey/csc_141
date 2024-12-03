import pygame

class Ship:
    def __init__(self, ai_game):
        #initialize the ship and it's starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #load ship image and get rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at bottom of screen
        self.rect.midbottom = self.screen_rect.midbottom

        #store float for ships exact horizontal position
        self.x = float(self.rect.x)

        #movement flags; start with ship not moving
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''update ship position based on movement flags'''
        #update ship x value, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        #update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        #draw ship at current location
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """center ship on screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)