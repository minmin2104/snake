import pygame


class _SnakeBody:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.position = pygame.math.Vector2(self.x, self.y)
        self.rect = pygame.Rect(self.position.x, self.position.y, width, height)


class Snake:
    def __init__(self, game):
        self.game = game
        self.head = _SnakeBody(0, 0, 25, 25)
        self.body = None
        self.color = (0, 255, 0)

    def update(self):
        pass

    def render(self):
        pygame.draw.rect(self.game.screen, self.color, self.head.rect)
