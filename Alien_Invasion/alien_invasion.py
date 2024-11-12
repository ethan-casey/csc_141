import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
#overall class to manage assets and behavior

    def __init__(self):
        #initialize game and create resources
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        #background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        #start main loop
        while True:
            self._check_events()
            self._update_screen()

            # make most recent draw screen visible
            pygame.display.flip()
            self.clock.tick(60)

    def _check_events(self):
        #check for keypresses and mouse events
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
    
    def _update_screen(self):
        #update images on screen and flip to new screen
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

if __name__ == '__main__':
    #make game instance and run game
    ai = AlienInvasion()
    ai.run_game()