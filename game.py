import pygame
from pygame.math import Vector2
import sys
from fruit import FRUIT
from snake import snake
class Game():
    def __init__(self,height,width,display):
        self.width = width
        self.height = height
        self.cell_size = 40
        self.cell_number = 20
        self.apple = pygame.image.load("graphics/apple.png").convert_alpha()
        self.display  = display
        self.clock = pygame.time.Clock()
        self.fruit = FRUIT(self)
        self.snake = snake(self)
        self.screen_update = pygame.USEREVENT
        pygame.time.set_timer(self.screen_update,150)
    def update(self):
        self.snake.movesnake()
        self.check_collision()
        self.check_fail()
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
    def check_fail(self):
        if not 0 <= self.snake.body[0].x < self.cell_number or not 0 <= self.snake.body[0].y < self.cell_number:
            self.gameover()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.gameover()


    def gameover(self):
        pygame.quit()
        sys.exit()
        pygame.display.quit()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    pygame.display.quit()
                if event.type == self.screen_update:
                    self.update()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if self.snake.direction.y != 1:
                            self.snake.direction = Vector2(0,-1)
                    if event.key == pygame.K_DOWN:
                        if self.snake.direction.y != -1:
                            self.snake.direction = Vector2(0,1)
                    if event.key == pygame.K_LEFT:
                        if self.snake.direction.x != 1:
                            self.snake.direction = Vector2(-1,0)
                    if event.key == pygame.K_RIGHT:
                        if self.snake.direction.x != -1:
                            self.snake.direction = Vector2(1,0)
            self.display.fill((175,215,70))
            self.draw_elements()
            pygame.display.update()
            self.clock.tick(60)
