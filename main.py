import pygame
from game import Game
HEIGHT = 800
WIDTH = 800
display = pygame.display.set_mode((HEIGHT,WIDTH))
game = Game(HEIGHT,WIDTH,display)
icon = pygame.image.load("snake.ico")
pygame.display.set_icon(icon)
pygame.display.set_caption('Snake')
game.run()
