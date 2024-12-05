class GameStats:
    """track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """initialize stats"""
        self.settings = ai_game.settings
        #Highscore should never be reset
        self.high_score = 0
        self.reset_stats()

    def reset_stats(self):
        """initialize statistics that can change during game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1