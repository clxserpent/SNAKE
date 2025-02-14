import pygame
pygame.init()
from pygame.math import Vector2
class snake:
    def __init__(self,game):
        self.game = game
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.new_block = False

        self.head_up = pygame.image.load("graphics/head_up.png").convert_alpha()
        self.head_down = pygame.image.load("graphics/head_down.png").convert_alpha()
        self.head_right = pygame.image.load("graphics/head_right.png").convert_alpha()
        self.head_left = pygame.image.load("graphics/head_left.png").convert_alpha()

        self.tail_left = pygame.image.load("graphics/tail_left.png").convert_alpha()
        self.tail_right = pygame.image.load("graphics/tail_right.png").convert_alpha()
        self.tail_up = pygame.image.load("graphics/tail_up.png").convert_alpha()
        self.tail_down = pygame.image.load("graphics/tail_down.png").convert_alpha()

        self.body_vertical = pygame.image.load("graphics/body_vertical.png").convert_alpha()
        self.body_horizontal = pygame.image.load("graphics/body_horizontal.png").convert_alpha()

        self.body_tr = pygame.image.load("graphics/body_tr.png").convert_alpha()
        self.body_tl = pygame.image.load("graphics/body_tl.png").convert_alpha()
        self.body_br = pygame.image.load("graphics/body_br.png").convert_alpha()
        self.body_bl = pygame.image.load("graphics/body_bl.png").convert_alpha()
        
    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        for index,block in enumerate(self.body):
            self.x_pos = int(block.x * self.game.cell_size)
            self.y_pos = int(block.y * self.game.cell_size)
            self.block_rect = pygame.Rect(self.x_pos,self.y_pos,self.game.cell_size,self.game.cell_size)
            
            if index == 0:
                self.game.display.blit(self.head,self.block_rect)
            elif index == len(self.body)-1:
                self.game.display.blit(self.tail,self.block_rect)
            else:
                self.previous_block = self.body[index+1] - block
                self.next_block = self.body[index - 1] - block
                if self.previous_block.x == self.next_block.x:
                    self.game.display.blit(self.body_vertical,self.block_rect)
                elif self.previous_block.y == self.next_block.y:
                    self.game.display.blit(self.body_horizontal,self.block_rect)
                else:
                    if self.previous_block.x == -1 and self.next_block.y == -1 or self.previous_block.y == -1 and self.next_block.x == -1:
                        self.game.display.blit(self.body_tl,self.block_rect)
                    elif self.previous_block.x == -1 and self.next_block.y == 1 or self.previous_block.y == 1 and self.next_block.x == -1:
                        self.game.display.blit(self.body_bl,self.block_rect)               
                    elif self.previous_block.x == 1 and self.next_block.y == -1 or self.previous_block.y == -1 and self.next_block.x == 1:
                        self.game.display.blit(self.body_tr,self.block_rect)
                    elif self.previous_block.x == 1 and self.next_block.y == 1 or self.previous_block.y == 1 and self.next_block.x == 1:
                        self.game.display.blit(self.body_br,self.block_rect)     
                
                
                




    
    def reset(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)


    def update_head_graphics(self):
        self.head_relation  = self.body[1] - self.body[0]
        if self.head_relation == Vector2(1,0):
            self.head = self.head_left
        elif self.head_relation == Vector2(0,-1):
            self.head = self.head_down
        elif self.head_relation == Vector2(0,1):
            self.head = self.head_up
        elif self.head_relation == Vector2(-1,0):
            self.head = self.head_right
    
    def update_tail_graphics(self):
        self.tail_relation = self.body[-2] - self.body[-1]
        if self.tail_relation == Vector2(1,0):
            self.tail = self.tail_left
        elif self.tail_relation == Vector2(0,-1):
            self.tail = self.tail_down
        elif self.tail_relation == Vector2(0,1):
            self.tail = self.tail_up
        elif self.tail_relation == Vector2(-1,0):
            self.tail = self.tail_right
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


