import pygame,sys,random

pygame.init()

class FRUIT:
    def __init__(self,game):
        self.game = game
        self.randomize()
    def draw_fruit(self):
        self.fruit_rect = pygame.Rect(int(self.pos.x*self.game.cell_size),int(self.pos.y*self.game.cell_size),self.game.cell_size,self.game.cell_size)
        self.game.display.blit(self.game.apple,self.fruit_rect)

    def randomize(self):
        self.x = random.randint(0,self.game.cell_number-1)
        self.y = random.randint(0,self.game.cell_number-1)
        self.pos = pygame.math.Vector2(self.x,self.y)