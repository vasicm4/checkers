from Square import *

files = [chr(i) for i in range(ord('a'), ord('i') + 1)]
ranks = [i for i in range(1, 9)]

class Checker:
    def __init__(self, square: Square) -> None:
        self._square = square
        self._is_queen = False


    def move_left_up(self) -> None:
        if self.square.file == 'a' or self.square.rank == 1:
            return
        self.square.file = chr(ord(self.square.file) - 1)
        self.square.rank -= 1


    def move_left_down(self) -> None:
        if self.square.file == 'a' or self.square.rank == 1:
            return
        self.square.file = chr(ord(self.square.file) - 1)
        self.square.rank -= 1


    def move_right_up(self) -> None:
        if self.square.file == 'h' or self.square.rank == 8:
            return
        self.square.file = chr(ord(self.square.file) + 1)
        self.square.rank += 1


    def move_right_down(self) -> None:
        if self.square.file == 'h' or self.square.rank == 8:
            return
        self.square.file = chr(ord(self.square.file) + 1)
        self.square.rank += 1


    def moves_available(self) -> list:
        moves = []


    @property
    def square(self) -> Square:
        return self._square

    @square.setter
    def square(self, square: Square) -> None:
        self._square = square

    @property
    def is_queen(self) -> bool:
        return self._is_queen

    @is_queen.setter
    def is_queen(self, is_queen: bool) -> None:
        self._is_queen = is_queen

