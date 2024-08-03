class Stats():
    """Stats of the game"""

    def __init__(self, config) -> None:
        self.config = config
        self.reset_stats()

    def reset_stats(self):
        """Initialize stats that can change during the game"""
        self.ships_left = self.config.number_ships