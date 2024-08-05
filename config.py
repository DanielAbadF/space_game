class Config:
    def __init__(self) -> None:
        """Initialize the game congurations"""
        self.screen_width = 1200
        self.screen_heigth = 800
        self.bg_color = (230,230,230)
        self.number_ships = 3

        
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.allowed_bullets = 3    

        #Alien configs
        self.fleet_drop_speed = 10

        self.acceleration_scale = 1.1

        self.initialize_dinamic_configs()
        
        

    def initialize_dinamic_configs(self):
        self.speed_ship_factor = 1.5
        self.alien_speed_factor = 1        
        self.bullet_speed_factor = 0.5  
        #Fleet direction = 1 represents right and -1 represents left 
        self.fleet_direction = 1

    def increase_speed(self):
        self.speed_ship_factor *= self.acceleration_scale
        self.bullet_speed_factor *= self.acceleration_scale
        self.alien_speed_factor *= self.acceleration_scale