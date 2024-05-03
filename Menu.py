import os.path

import pygame
from Constants import *
import Game


#initialization of the game
class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))
        pygame.display.set_caption("Checkers")
        self.clock = pygame.time.Clock()  # controling framerate
        self.gameStateManager = GameStateManager("start")
        self.game = Game.Game()
        self.menu = Menu(self.screen, self.gameStateManager, self.game)
        self.board = Board(self.screen, self.gameStateManager, self.game)
        self.pause = Pause(self.screen, self.gameStateManager, self.game)
        self.states = {"start": self.menu, "board": self.board, "pause": self.pause}

    def run(self):
        while True:
            state = self.states[self.gameStateManager.get_state()].run()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE and self.gameStateManager.get_state() == "board":
                        self.gameStateManager.set_state("pause")
                    elif event.key == pygame.K_ESCAPE and self.gameStateManager.get_state() == "pause":
                        self.gameStateManager.set_state("board")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()
            if state == "board":
                self.gameStateManager.set_state("board")
            elif state == "start":
                self.gameStateManager.set_state("start")
                self.board = Board(self.screen, self.gameStateManager, self.game)
            elif state == "pause":
                self.gameStateManager.set_state("pause")
            pygame.display.update()
            self.clock.tick(FPS)


class GameStateManager:
    def __init__(self, currentState):
        self.current_state = currentState

    def get_state(self):
        return self.current_state

    def set_state(self, state):
        self.current_state = state


#buttons
#add buttons that represent game modes regular and force jump and add event handling for them
class Button:
    def __init__(self, size, text, color, x, y):
        self.text = text
        self.color = color
        self.size = size
        self.font = pygame.font.Font("Jersey_25" + os.path.sep + "Jersey25-Regular.ttf", self.size)
        self.x = x
        self.y = y
        self.clicked = False

    def create(self):
        return self.font.render(self.text, True, self.color)

    def draw(self, display):
        rect = self.create().get_rect(center=(self.x, self.y))
        action = False
        pos = pygame.mouse.get_pos()
        if rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        display.blit(self.create(), rect)
        return action


#class main menu
class Menu:
    def __init__(self, display, gameStateManager, game):
        self.display = display
        self.gameStateManager = gameStateManager
        self.welcome = pygame.font.Font("Jersey_25" + os.path.sep + "Jersey25-Regular.ttf", size=150).render("WELCOME", True,
                                                                                                        (0, 0, 0))
        self.gamemode = pygame.font.Font("Jersey_25" + os.path.sep + "Jersey25-Regular.ttf", size=50).render("FORCE JUMP",
                                                                                                        True, (0, 0, 0))

        self.forcejump = Button(75, "YES", (0, 0, 0), 300, 500)
        self.regular = Button(75, "NO", (255, 0, 0), 500, 500)
        self.start = Button(100, "START", (0, 0, 0), 400, 650)
        self.game = game
    def run(self):
        self.display.fill((2, 122, 4))
        self.display.blit(self.welcome, self.welcome.get_rect(center=self.display.get_rect().center, top=150))
        self.display.blit(self.gamemode, self.gamemode.get_rect(center=self.display.get_rect().center, top=400))
        if self.forcejump.draw(self.display):
            self.game._force_jump = True
            self.forcejump.color = (255, 0, 0)
            self.forcejump.draw(self.display)
            self.regular.color = (0, 0, 0)
            self.forcejump.draw(self.display)
        if self.regular.draw(self.display):
            self.game._force_jump = False
            self.forcejump.color = (0,0,0)
            self.forcejump.draw(self.display)
            self.regular.color = (255, 0, 0)
            self.regular.draw(self.display)
        if self.start.draw(self.display):
            self.start.color = (0, 0, 0)
            self.regular.color = (0, 0, 0)
            self.forcejump.color = (0, 0, 0)
            return "board"

class Pause:
    def __init__(self, display, gameStateManager, game):
        self.display = display
        self.gameStateManager = gameStateManager
        self.game = game

    def run(self):
        self.display.fill((2, 122, 4))
        play = Button(100, "CONTINUE PLAYING",(0, 0, 0), 400,300)
        return_menu = Button(100, "RETURN TO MENU",(0, 0, 0), 400,500)
        if play.draw(self.display):
            return "board"
        if return_menu.draw(self.display):
            return "start"


class Board:
    def __init__(self, display, gameStateManager, game):
        self.display = display
        self.gameStateManager = gameStateManager
        self.game = game

    def run(self):
        board = pygame.Surface((WIDTH, HEIGHT))
        board.fill((181, 136, 99))
        self.game.squares_fill()
        for rank in self.game._squares.keys():
            for file in self.game._squares[rank].keys():
                self.game._squares[rank][file].draw(board)
        # for x in range(0, 8, 1):
        #     if x % 2 == 0:
        #         for y in range(0, 8, 2):
        #             pygame.draw.rect(board, (240, 217, 181), (x * CELL, y * CELL, CELL, CELL))
        #     else:
        #         for y in range(1, 8, 2):
        #             pygame.draw.rect(board, (240, 217, 181), (x * CELL, y * CELL, CELL, CELL))
        self.display.blit(board, (0, 0))


if __name__ == '__main__':
    main = Main()
    main.run()
