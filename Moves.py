from Constants import *
from Checker import Checker
class Moves:
    def move_left_up(self, Checker: Checker) -> None:
        if Checker == 'a' or Checker.rank == 1:
            return
        Checker.file = chr(ord(Checker.file) - 1)
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
