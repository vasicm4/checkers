from Constants import *
import pygame
class Square:
    def __init__(self, file: str, rank: int) -> None:
        self._file = file
        self._rank = rank
        self._color = (240, 217, 181)

    def calculate_position(self):
        self.x = (ord(self.file) - ord('a')) * CELL + CELL // 2
        self.y = (self.rank - 1) * CELL + CELL // 2

    def draw(self, board):
        pygame.draw.rect(board, (181, 136, 99), ((self._rank - 1) * CELL,(ord(self._file) - ord('a')) * CELL,  CELL, CELL))

    def __str__(self) -> str:
        return "Field: " + self.file + str(self.rank)

    def __eq__(self, other) -> bool:
        return self.file == other.file and self.rank == other.rank

    def __iter__(self):
        return iter([self.file, self.rank])

#implement find square method

    @property
    def x(self) -> int:
        return self.x

    @property
    def y(self) -> int:
        return self.y

    @x.setter
    def x(self, x: int) -> None:
        self.x = x

    @y.setter
    def y(self, y: int) -> None:
        self.y = y

    @property
    def file(self) -> str:
        return self.file

    @property
    def rank(self) -> int:
        return self.rank

    @property
    def square(self) -> tuple:
        return self.square

    @file.setter
    def file(self, file):
        self.file = file

    @rank.setter
    def rank(self, rank):
        self.rank = rank

