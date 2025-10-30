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
        self.width = self.height = 25
        self.head = _SnakeBody(0, 0, self.width, self.height)
        self.body = [self.head]
        self.color = (0, 255, 0)
        self.speed = self.head.width
        self.movement = [0, 0]
        self.last_update_time = 0
        self.update_cooldown = 0.5

    def __translateX(self):
        self.head.position.x += self.movement[0] * self.speed
        self.head.rect.x = self.head.position.x

    def __translateY(self):
        self.head.position.y += self.movement[1] * self.speed
        self.head.rect.y = self.head.position.y

    def __add_body(self, x, y):
        snake_body = _SnakeBody(x, y, self.width, self.height)
        self.body.append(snake_body)

    def update(self):
        keys = self.game.keys
        if keys[pygame.K_UP]:
            self.movement = [0, -1]
        elif keys[pygame.K_LEFT] and self.movement[0] != 1:
            self.movement = [-1, 0]
        elif keys[pygame.K_RIGHT] and self.movement[0] != -1:
            self.movement = [1, 0]
        elif keys[pygame.K_DOWN]:
            self.movement = [0, 1]

        if self.game.game_time - self.last_update_time >= self.update_cooldown:
            self.__translateX()
            self.__translateY()
            self.last_update_time = self.game.game_time

    def render(self):
        for body in self.body:
            pygame.draw.rect(self.game.screen, self.color, body.rect)
