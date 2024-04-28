import pygame
from Square import *

files = [chr(i) for i in range(ord('a'), ord('i') + 1)]
ranks = [i for i in range(1,9)]

class Board:
    def __init__(self, board_size: (int, int)) -> None:
        self._board_size = board_size
        self._board_color = (181, 136, 99)

    # def generate_board(self):
    #     board = pygame.Surface((self.board_size[0], self.board_size[1]))
    #     board.fill((181, 136, 99))
    #     for x in range(0, 8, 1):
    #         if x % 2 == 0:
    #             for y in range(0, 8, 2):
    #                 pygame.draw.rect(board, (240, 217, 181), (x * cell, y * cell, cell, cell))
    #         else:
    #             for y in range(1, 8, 2):
    #                 pygame.draw.rect(board, (240, 217, 181), (x * cell, y * cell, cell, cell))