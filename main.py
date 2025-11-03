from snake import Snake
from food import Food
from game_state import GameState
import pygame
import random
import os

class Game:
    def __init__(self, win_width, win_height, win_title):
        self.fps = 60
        self.game_state = None
        self.running = True

        pygame.init()
        self.win_width = win_width
        self.win_height = win_height
        self.screen = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption(win_title)
        self.clock = pygame.time.Clock()
        self.pressed_keys = None
        self.dt = 0
        self.game_time = 0
        self.game_state = GameState.GamePlaying

        self.snake = Snake(self)
        self.food = Food(self, self.get_random_pos())
        self.init_score()

    def get_random_pos(self, width_height_offset=25):
        x = random.randint(0, (self.win_width - width_height_offset) // width_height_offset) * width_height_offset
        y = random.randint(0, (self.win_height - width_height_offset) // width_height_offset) * width_height_offset
        return pygame.math.Vector2(x, y)

    def init_score(self):
        retro_font = os.path.join("assets", "retro_gaming.ttf")
        self.score_text = pygame.font.Font(retro_font)
        self.score = 0

    def render_score(self):
        score_text_surface = self.score_text.render(f"Score: {self.score:0>3}", True, pygame.Color(255, 255, 255))
        self.screen.blit(score_text_surface, (self.win_width - score_text_surface.get_width() - 5, 5))

    def main(self):
        while self.running:
            # Poll input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
            self.keys = pygame.key.get_pressed()
            
            # Update & Render
            self.screen.fill((0, 0, 0))
            
            self.snake.update()
            self.food.update()
            
            self.snake.render()
            self.food.render()
            self.render_score()
            
            if self.game_state == GameState.GameOver:
                self.running = False
            
            pygame.display.flip()

            self.dt = self.clock.tick(self.fps) / 1000
            self.game_time += self.dt

    def clean_up(self):
        pygame.quit()
    
        
if __name__ == "__main__":
    game = Game(800, 600, "Da Snake")
    game.main()
    game.clean_up()
