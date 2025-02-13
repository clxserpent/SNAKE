import pygame
from game import Game
HEIGHT = 800
WIDTH = 800
display = pygame.display.set_mode((HEIGHT,WIDTH))
game = Game(HEIGHT,WIDTH,display)
game.run()
