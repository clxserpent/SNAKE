import pygame
pygame.init()
from pygame.math import Vector2
class snake:
    def __init__(self,game):
        self.game = game
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False

        self.head_up = pygame.image.load("graphics/head_up.png")
        self.head_down = pygame.image.load("graphics/head_down.png")
        self.head_right = pygame.image.load("graphics/head_right.png")
        self.head_left = pygame.image.load("graphics/head_left.png")

        self.tail_left = pygame.image.load("graphics/tail_left.png")
        self.tail_right = pygame.image.load("graphics/tail_right.png")
        self.tail_up = pygame.image.load("graphics/tail_up.png")
        self.tail_down = pygame.image.load("graphics/tail_down.png")

        self.body_vertical = pygame.image.load("graphics/body_vertical.png")
        self.body_horizontal = pygame.image.load("graphics/body_horizontal.png")

        self.body_tr = pygame.image.load("graphics/body_tr.png")
        self.body_tl = pygame.image.load("graphics/body_tl.png")
        self.body_br = pygame.image.load("graphics/body_br.png")
        self.body_bl = pygame.image.load("graphics/body_bl.png")
        
    def draw_snake(self):
        for index,block in enumerate(self.body):
            self.x_pos = int(block.x*self.game.cell_size)
            self.y_pos = int(block.y*self.game.cell_size)
            
    def movesnake(self):
        if self.new_block == True:
            self.body_copy = self.body[:]
            self.body_copy.insert(0,self.body_copy[0] + self.direction)
            self.body = self.body_copy[:]
            self.new_block = False
        else:
            self.body_copy = self.body[:-1]
            self.body_copy.insert(0,self.body_copy[0] + self.direction)
            self.body = self.body_copy[:]
    def add_block(self):
        self.new_block =True


