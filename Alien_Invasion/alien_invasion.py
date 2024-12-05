import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
#overall class to manage assets and behavior

    def __init__(self):
        #initialize game and create resources
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #create instance to store game statisitics & create scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        #background color
        self.bg_color = (230, 230, 230)

        #start Alien Invasion in inactive state
        self.game_active = False

        # Make play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        #start main loop
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
            self._update_screen()

            # make most recent draw screen visible
            pygame.display.flip()
            self.clock.tick(60)

    def _check_events(self):
        #check for keypresses and mouse events
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)    
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start new game when player clicks play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            
            #reset game settings
            self.settings.initialize_dynamic_settings()

            #reset game stats
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.game_active = True

            #get rid of any remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

            #create new fleet and center ship
            self._create_fleet()
            self.ship.center_ship()

            #hide mouse cursor
            pygame.mouse.set_visible(False)
    
    def _check_keydown_events(self, event):                
        """respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_bullets(self):
        """update bullets position and removes old bullets"""
        #update bullet positions
        self.bullets.update()

        #get rid of disappeared bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """respond to bullet-alien collision"""
        #remove any bullets and aliens that collided
        collisions = pygame.sprite.groupcollide(self.bullets,
                                                self.aliens, True, True)
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        
        if not self.aliens:
            #destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            #Increase level
            self.stats.level += 1
            self.sb.prep_level()

    def _update_screen(self):
        #update images on screen and flip to new screen
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()  
        self.ship.blitme()
        self.aliens.draw(self.screen)

        #Draw score information
        self.sb.show_score()

        #draw play button if game is inactive
        if not self.game_active:
            self.play_button.draw_button()

    def _fire_bullet(self):
        """create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        """create fleet of aliens"""
        #make an alien and add until no room left
        #spacing between aliens is one alien width and one alien height
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            #finished row, reset x value and increment y value
            current_x = alien_width
            current_y += 2 * alien_height
    
    def _create_alien(self, x_position, y_position):
            """create alien and place in fleet"""
            new_alien = Alien(self)
            new_alien.x = x_position
            new_alien.rect.x = x_position
            new_alien.rect.y = y_position
            self.aliens.add(new_alien)

    def _update_aliens(self):
        """update positions of aliens in fleet"""
        self._check_fleet_edges()
        self.aliens.update()

        #look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        #look for aliens hitting bottom of screen
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """respond appropriately if any aliens have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """drop entire fleet and change fleet direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """respond to ship being hit by alien"""
        if self.stats.ships_left > 0:
            #decrement ships_left, and update scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            #get rid of any remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

            #create new fleet and center ships
            self._create_fleet()
            self.ship.center_ship()

            #pause
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Check if alien reaches bottom of screen"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break
   
if __name__ == '__main__':
    #make game instance and run game
    ai = AlienInvasion()
    ai.run_game()