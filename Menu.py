import os.path

import pygame
from Constants import *
import Game
import Moves

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
                self.game.reset()
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
        #checks if the button is clicked
        if self.forcejump.draw(self.display): #changes gamemode to forcejump
            self.forcejump.color = (255, 0, 0)
            self.regular.color = (0, 0, 0)
            self.forcejump.draw(self.display)
        if self.regular.draw(self.display): #changes gammemode to regular
            self.forcejump.color = (0,0,0)
            self.regular.color = (255, 0, 0)
            self.regular.draw(self.display)
        if self.start.draw(self.display): #starts the game with parameters set by the buttons
            if self.forcejump.color == (255, 0, 0) and self.regular.color == (0,0,0):
                self.game._game_mode = "FORCEJUMP"
            elif self.forcejump.color == (0, 0, 0) and self.regular.color == (255,0,0):
                self.game._game_mode = "REGULAR"
            self.start.color = (0, 0, 0)
            self.regular.color = (255, 0, 0)
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
        self.moves = Moves.Moves()
        self.available = []
        self.checker = None

    def generate_board(self):
        board = pygame.Surface((WIDTH, HEIGHT))
        board.fill((240, 217, 181))
        for rank in self.game._squares.keys():
            for file in self.game._squares[rank].keys():
                self.game._squares[rank][file].draw(board)
        return board

    def get_pos(self, pos):
        x, y = pos
        file = FILES[x // CELL]
        rank = 8 - y // CELL
        return rank, file

    def run(self):
        board = self.generate_board()
        if self.game.end():
            return "end"
        for dict in self.game._checkers.values():
            for checker in dict.values():
                if checker != None:
                    if not checker.is_eaten:
                        checker.draw(board)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and self.gameStateManager.get_state() == "board":
                    self.gameStateManager.set_state("pause")
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if not self.game.turn:
                continue
                #calls find move function
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    rank, file = self.get_pos(pos)
                    if file in self.game._squares[rank] and self.checker != None:
                        square = self.game._squares[rank][file]
                        if square in self.available:
                            self.moves.last_move_setter(self.game,self.checker.square, square)
                            self.game.move_checker(self.checker, square)
                            self.available.remove(square)
                            self.checker.moves_reset(self.available)
                            self.available = []
                            self.checker = None
                            self.game.turn = False
                            continue
                    if file in self.game._checkers[rank]:
                        checker = self.game._checkers[rank][file]
                        if checker == None:
                            continue
                        if checker.color == (255, 0, 0) or checker._color == (150,75,0):
                            if self.checker != None and self.checker != checker:
                                self.checker.chosen = False
                                self.checker.moves_reset(self.available)
                                self.available = []
                                self.checker = checker
                            if not checker.chosen:
                                self.checker = checker
                                checker.chosen = True
                                self.available = checker.moves_available(self.moves, self.game)
                            if len(self.available) == 0:
                                self.checker.chosen = False
                                self.checker = None
                        elif checker.color == (255,255,0):
                            checker.chosen = False
                            checker.moves_reset(self.available)
                            self.available = []
        self.display.blit(board, (0, 0))


if __name__ == '__main__':
    main = Main()
    main.run()
