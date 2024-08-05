import pygame.font
from config import Config
from game_stats import Stats
class Marker():

    def __init__(self, config:Config, screen, stats:Stats) -> None:
        self.screen = screen
        self.screen_rect = screen.get_rect()      
        self.config = config
        self.stats = stats

        self.text_color  = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.create_score()
        self.create_top_score()

    def create_score(self):
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_img = self.font.render(score_str, True, self.text_color, self.config.bg_color )

        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20 
        self.score_rect.top = 20

    def create_top_score(self):
        rounded_score = int(round(self.stats.top_score, -1))
        score_str = "{:,}".format(rounded_score)
        self.top_score_img = self.font.render(score_str, True, self.text_color, self.config.bg_color )

        self.top_score_rect = self.top_score_img.get_rect()
        self.top_score_rect.centerx = self.screen_rect.centerx
        self.top_score_rect.top = self.score_rect.top

    def show_score(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.top_score_img, self.top_score_rect)
