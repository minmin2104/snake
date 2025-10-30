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
        self.speed = self.width
        self.movement = [0, 0]
        self.last_update_time = 0
        self.update_cooldown = 0.5

    def __translateX(self):
        self.head.position.x += self.movement[0] * self.speed

    def __translateY(self):
        self.head.position.y += self.movement[1] * self.speed

    def __update_position(self):
        self.head.rect.x = self.head.position.x
        self.head.rect.y = self.head.position.y

    def __add_body(self, x, y):
        snake_body = _SnakeBody(x, y, self.width, self.height)
        self.body.append(snake_body)

    def update(self):
        keys = self.game.keys
        if keys[pygame.K_UP] and self.movement[1] == 0:
            self.movement = [0, -1]
        elif keys[pygame.K_LEFT] and self.movement[0] == 0:
            self.movement = [-1, 0]
        elif keys[pygame.K_RIGHT] and self.movement[0] == 0:
            self.movement = [1, 0]
        elif keys[pygame.K_DOWN] and self.movement[1] == 0:
            self.movement = [0, 1]

        if self.game.game_time - self.last_update_time >= self.update_cooldown:
            self.__translateX()
            self.__translateY()
            if self.head.position.x < 0:
                self.head.position.x = self.game.win_width - self.width
            elif self.head.position.x >= self.game.win_width:
                self.head.position.x = 0
            elif self.head.position.y < 0:
                self.head.position.y = self.game.win_height - self.height
            elif self.head.position.y >= self.game.win_height:
                self.head.position.y = 0
            self.__update_position()
            self.last_update_time = self.game.game_time

    def render(self):
        for body in self.body:
            pygame.draw.rect(self.game.screen, self.color, body.rect)
