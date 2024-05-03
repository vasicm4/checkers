import os.path

import pygame
from Constants import *
import Game

#initialization of the game
pygame.init()
screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")
clock = pygame.time.Clock() #controling framerate

#starting menu
welcome = pygame.font.Font("Jersey_25"+os.path.sep+"Jersey25-Regular.ttf", size=150).render("WELCOME", True, (0, 0, 0))
gamemode = pygame.font.Font("Jersey_25"+os.path.sep+"Jersey25-Regular.ttf", size=50).render("FORCE JUMP", True, (0, 0, 0))

#buttons
#add buttons that represent game modes regular and force jump and add event handling for them
class Button:
    def __init__(self,text, x, y):
        self.text = text
        self.rect = text.get_rect(center = (x,y))
        self.clicked = False
    def draw(self, screen):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.text, self.rect)

        return action




#class main menu
class Menu:
    forcejump = Button(
        pygame.font.Font("Jersey_25" + os.path.sep + "Jersey25-Regular.ttf", size=75).render("YES", True,
                                                                                             (0, 0, 0)), 300, 500)
    regular = Button(
        pygame.font.Font("Jersey_25" + os.path.sep + "Jersey25-Regular.ttf", size=75).render("NO", True, (0, 0, 0)),
        500, 500)
    start = Button(
        pygame.font.Font("Jersey_25" + os.path.sep + "Jersey25-Regular.ttf", size=100).render("START", True,
                                                                                              (0, 0, 0)), 400, 650)
    quit = Button(pygame.font.Font("Jersey_25" + os.path.sep + "Jersey25-Regular.ttf", size=50).render("EXIT", True,
                                                                                                       (255, 0, 0)),
                  400, 700)
    mode = None
    screen.fill((2, 122, 4))
    screen.blit(welcome, welcome.get_rect(center=screen.get_rect().center, top=150))
    screen.blit(gamemode, gamemode.get_rect(center=screen.get_rect().center, top=400))
    if forcejump.draw(screen):
        mode = True
        forcejump = Button(
            pygame.font.Font("Jersey_25" + os.path.sep + "Jersey25-Regular.ttf", size=75).render("YES", True, (255, 0, 0)),
            300, 500)
        regular = Button(
            pygame.font.Font("Jersey_25" + os.path.sep + "Jersey25-Regular.ttf", size=75).render("NO", True, (0, 0, 0)),
            500, 500)
    if regular.draw(screen):
        mode = False
        forcejump = Button(
            pygame.font.Font("Jersey_25" + os.path.sep + "Jersey25-Regular.ttf", size=75).render("YES", True, (0, 0, 0)),
            300, 500)
        regular = Button(
            pygame.font.Font("Jersey_25" + os.path.sep + "Jersey25-Regular.ttf", size=75).render("NO", True, (255, 0, 0)),
            500, 500)
    if start.draw(screen):
        game = Game.Game(mode)
        start = Button(pygame.font.Font("Jersey_25" + os.path.sep + "Jersey25-Regular.ttf", size=100).render("START", True,(255, 0, 0)),400, 650)
    if quit.draw(screen):
        pygame.quit()
        exit()
class Board:
    def __init__(self):
        board = pygame.Surface((WIDTH, HEIGHT))
        board.fill((181, 136, 99))
        for x in range(0, 8, 1):
            if x % 2 == 0:
                for y in range(0, 8, 2):
                    pygame.draw.rect(board, (240, 217, 181), (x * CELL, y * CELL, CELL, CELL))
            else:
                for y in range(1, 8, 2):
                    pygame.draw.rect(board, (240, 217, 181), (x * CELL, y * CELL, CELL, CELL))
        screen.blit(board, (0, 0))

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        Menu()
    pygame.display.update()
    clock.tick(60)
