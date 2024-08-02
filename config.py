class Config:
    def __init__(self) -> None:
        """Initialize the game congurations"""
        self.screen_width = 800
        self.screen_heigth = 600
        self.bg_color = (230,230,230)
        self.speed_ship_factor = 1.5

        self.bullet_speed_factor = 0.5
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.allowed_bullets = 3    

        #Alien configs

        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        
        #Fleet direction = 1 represents right and -1 represents left 
        self.fleet_direction = 1

