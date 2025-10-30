from snake import Snake
import pygame


class Game:
    def __init__(self, win_width, win_height, win_title):
        self.fps = 60
        self.game_state = None
        self.running = True

        pygame.init()
        self.__win_width = win_width
        self.__win_height = win_height
        self.screen = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption(win_title)
        self.clock = pygame.time.Clock()
        self.pressed_keys = None
        self.dt = 0

        self.snake = Snake(self)
        self.food = None
        self.score = 0

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
            self.snake.render()
            
            pygame.display.flip()

            self.dt = self.clock.tick(self.fps) / 1000

    def clean_up(self):
        pygame.quit()
    
        
if __name__ == "__main__":
    game = Game(800, 600, "Da Snake")
    game.main()
    game.clean_up()
