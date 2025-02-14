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
        self.font = pygame.font.Font(None,25)

        pygame.time.set_timer(self.screen_update,150)
    def update(self):
        self.snake.movesnake()
        self.check_collision()
        self.check_fail()
        
    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < self.cell_number or not 0 <= self.snake.body[0].y < self.cell_number:
            self.gameover()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.gameover()


    def gameover(self):
        self.snake.reset()
        
    def draw_grass(self):
        self.grass_colour = (167,209,61)
        for row in range (self.cell_number):
            if row % 2 == 0 :
                for col in range(self.cell_number):
                    if col % 2 == 0:
                        self.grass_rect = pygame.Rect(col*self.cell_size,row * self.cell_size,self.cell_size,self.cell_size)
                        pygame.draw.rect(self.display,self.grass_colour,self.grass_rect)
            else:
                for col in range(self.cell_number):
                    if col % 2 != 0:
                        self.grass_rect = pygame.Rect(col*self.cell_size,row * self.cell_size,self.cell_size,self.cell_size)
                        pygame.draw.rect(self.display,self.grass_colour,self.grass_rect)
    
    
    def draw_score(self):
        self.score_text = str(len(self.snake.body)-3) #the score will be linked to the size of the snake -3 because our snake starts of with 3 vectors
        self.score_surface = self.font.render(self.score_text,True,(56,74,12))
        self.score_x = int(self.cell_size*self.cell_number-60)
        self.score_y = int(self.cell_size*self.cell_number-40)
        self.score_rect = self.score_surface.get_rect(center = (self.score_x,self.score_y))
        self.apple_rect = self.apple.get_rect(midright = (self.score_rect.left,self.score_rect.centery))
        self.bg_rect = pygame.Rect(self.apple_rect.left,self.apple_rect.top,self.apple_rect.width+self.score_rect.width + 6,self.apple_rect.height)

        pygame.draw.rect(self.display,(167,209,61),self.bg_rect)
        self.display.blit(self.score_surface,self.score_rect)
        self.display.blit(self.apple,self.apple_rect)
        pygame.draw.rect(self.display,(56,74,12),self.bg_rect,2)

        


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
