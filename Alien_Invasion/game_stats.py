class GameStats:
    """track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """initialize stats"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """initialize statistics that can change during game"""
        self.ships_left = self.settings.ship_limit