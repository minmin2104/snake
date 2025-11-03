import pygame


class _SnakeBody:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.position = pygame.math.Vector2(self.x, self.y)
        self.rect = pygame.Rect(self.position.x, self.position.y, width, height)
        self.movement_queue = []


class Snake:
    def __init__(self, game):
        self.game = game
        self.width = self.height = 25
        self.head = _SnakeBody(0, 0, self.width, self.height)
        self.body = [
            self.head
        ]
        self.body_pos_hist = []
        self.color = (0, 255, 0)
        self.speed = self.width
        self.movement = [0, 0]
        self.curr_move = [0, 0]
        self.last_update_time = 0
        self.update_cooldown = 0.125
        self.can_queue_input = True
        self.delay = 1

    def __translateX(self):
        self.head.position.x += self.movement[0] * self.speed

    def __translateY(self):
        self.head.position.y += self.movement[1] * self.speed

    def grow_body(self):
        self.body.append(_SnakeBody(self.body_pos_hist[-1].x, self.body_pos_hist[-1].y, self.width, self.height))

    def __translateHead(self):
        if self.head.movement_queue:
            self.curr_move = self.head.movement_queue.pop(0)
        self.body_pos_hist.append(self.head.position.copy())
        max_hist = len(self.body) * self.delay
        if len(self.body_pos_hist) > max_hist:
            self.body_pos_hist.pop(0)
        self.head.position.x += self.curr_move[0] * self.speed
        self.head.position.y += self.curr_move[1] * self.speed

    def __update_position(self):
        self.head.rect.x = self.head.position.x
        self.head.rect.y = self.head.position.y

    def __add_body(self, x, y):
        snake_body = _SnakeBody(x, y, self.width, self.height)
        self.body.append(snake_body)

    def __handle_wall(self):
        if self.head.position.x < 0:
            self.head.position.x = self.game.win_width - self.width
        elif self.head.position.x >= self.game.win_width:
            self.head.position.x = 0
        elif self.head.position.y < 0:
            self.head.position.y = self.game.win_height - self.height
        elif self.head.position.y >= self.game.win_height:
            self.head.position.y = 0

    def update(self):
        keys = self.game.keys
        if keys[pygame.K_UP] and self.curr_move != [0, 1]:
            self.movement = [0, -1]
        elif keys[pygame.K_LEFT] and self.curr_move != [1, 0]:
            self.movement = [-1, 0]
        elif keys[pygame.K_RIGHT] and self.curr_move != [-1, 0]:
            self.movement = [1, 0]
        elif keys[pygame.K_DOWN] and self.curr_move != [0, -1]:
            self.movement = [0, 1]

        if self.can_queue_input:
            if not all(val == 0 for val in self.movement):
                # Handle opposite movement is a no no
                if not self.head.movement_queue:
                    self.head.movement_queue = [self.movement]
                else:
                    if self.head.movement_queue[-1] != self.movement:
                        self.head.movement_queue.append(self.movement)
            self.can_queue_input = False

        if self.game.game_time - self.last_update_time >= self.update_cooldown:
            self.__translateHead()
            self.can_queue_input = True
            self.__handle_wall()
            for i in range(1, len(self.body)):
                index = -(i * self.delay)
                if len(self.body_pos_hist) >= abs(index):
                    self.body[i].position = self.body_pos_hist[index].copy()
                    self.body[i].rect.x = self.body[i].position.x
                    self.body[i].rect.y = self.body[i].position.y                    
            self.__update_position()
            self.last_update_time = self.game.game_time
        
    def render(self):
        for body in self.body:
            pygame.draw.rect(self.game.screen, self.color, body.rect)
