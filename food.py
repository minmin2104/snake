import pygame


class Food:
    def __init__(self, game, pos):
        self.game = game
        self.pos = pos
        self.color = (255, 0, 0)
        self.width = self.height = 25
        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.width, self.height)

    def update(self):
        if self.rect.colliderect(self.game.snake.head.rect):
            self.game.score += 1
            pos = self.game.get_random_pos()
            while pos == self.game.snake.head.position:
                pos = self.game.get_random_pos()
            self.pos = pos
            self.rect.x = self.pos.x
            self.rect.y = self.pos.y
            self.game.snake.grow_body()

    def render(self):
        pygame.draw.rect(self.game.screen, self.color, self.rect)
