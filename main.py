from snake import Snake
from food import Food
import pygame
import random


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

        self.snake = Snake(self)
        self.food = Food(self, self.get_random_pos())
        self.score = 0

    def get_random_pos(self, width_height_offset=25):
        x = random.randint(0, (self.win_width - width_height_offset) // width_height_offset) * width_height_offset
        y = random.randint(0, (self.win_height - width_height_offset) // width_height_offset) * width_height_offset
        return pygame.math.Vector2(x, y)

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
            
            self.food.render()
            self.snake.render()
            
            pygame.display.flip()

            self.dt = self.clock.tick(self.fps) / 1000
            self.game_time += self.dt

    def clean_up(self):
        pygame.quit()
    
        
if __name__ == "__main__":
    game = Game(800, 600, "Da Snake")
    game.main()
    game.clean_up()
