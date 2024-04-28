import pygame
from Constants import *

#initialization of the game
pygame.init()
screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")
clock = pygame.time.Clock() #controling framerate

#starting menu
button = pygame.rect.Rect(300, 300, 200, 100)


#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((2, 122, 4))
    pygame.display.update()
    clock.tick(60)
