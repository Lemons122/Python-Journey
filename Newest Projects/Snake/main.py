import pygame
from pygame.locals import *
import time
import random

size = 40


class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("resources/SnakeApple.png").convert()
        self.parent_screen = parent_screen
        self.x = size * 3
        self.y = size * 3

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def spawn(self):
        self.x = random.randint(1, 20) * size
        self.y = random.randint(1, 20) * size


class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/SnakeBody.png").convert()
        self.x = [size] * length
        self.y = [size] * length
        self.direction = ''

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_right(self):
        self.direction = 'right'

    def move_left(self):
        self.direction = 'left'

    def draw(self):
        self.parent_screen.fill((0, 0, 0))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def walk(self):

        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'up':
            self.y[0] -= size
        if self.direction == 'down':
            self.y[0] += size
        if self.direction == 'right':
            self.x[0] += size
        if self.direction == 'left':
            self.x[0] -= size
        self.draw()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((800, 800))
        self.surface.fill((0, 0, 0))
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + size:
            if y1 >= y2 and y1 < y2 + size:
                return True
        return False

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            print('Collision has occurred')
            self.snake.increase_length()
            self.apple.spawn()

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (200, 200, 200))
        self.surface.blit(score, (10, 10))

    def run(self):

        pygame.display.flip()

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:  # Lets the program exit via escape key
                        running = False
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                elif event.type == QUIT:  # Lets the program exit
                    running = False
            self.play()
            self.display_score()
            time.sleep(0.3)


if __name__ == "__main__":
    game = Game()
    game.run()
