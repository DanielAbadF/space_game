class Stats():
    """Stats of the game"""

    def __init__(self, config) -> None:
        self.config = config
        self.reset_stats()

        #Initialize the gamer in an active state 
        self.game_active = False
        self.top_score = 0

    def reset_stats(self):
        """Initialize stats that can change during the game"""
        self.ships_left = self.config.number_ships
        self.score = 0