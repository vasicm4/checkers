from Constants import *
from Checker import Checker
class Moves:
    def __init__(self):
        self._red_checkers = []
        self._black_chekers = []

    def get_red_checkers(self) -> list:
        return self._red_checkers

    def get_black_checkers(self) -> list:
        return self._black_chekers

    def move_left_up(self, checker: Checker) -> None:
        if checker.square.file == 'a' or checker.square.rank == 1:
            return
        checker.square.file = chr(ord(checker.square.file) - 1)
        checker.square.rank -= 1


    def move_left_down(self, checker: Checker) -> None:
        if checker.square.file == 'a' or checker.square.rank == 8:
            return
        checker.square.file = chr(ord(checker.square.file) - 1)
        checker.square.rank += 1

    def move_right_up(self, checker: Checker) -> None:
        if checker.square.file == 'h' or checker.square.rank == 8:
            return
        checker.square.file = chr(ord(checker.square.file) + 1)
        checker.square.rank += 1

    def move_right_down(self, checker: Checker) -> None:
        if checker.square.file == 'h' or checker.square.rank == 1:
            return
        checker.square.file = chr(ord(checker.square.file) + 1)
        checker.square.rank -= 1

