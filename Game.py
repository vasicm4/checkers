from Constants import *
from Square import Square
from Checker import Checker
class Game:
    def __init__(self, forcejump: bool = False) -> None:
        self._force_jump = forcejump
        self._over = False
        self._squares = {}
        self._checkers = {}
        if forcejump:
            self._game_mode = "FORCEJUMP"
        else:
            self._game_mode = "REGULAR"

    def squares_fill(self):
        for rank in RANKS:
            self._squares[rank] = {}
            for file in FILES:
                if ((ord(file) - ord('a')) + (rank - 1)) % 2 == 1:
                    self._squares[rank][file] = Square(file, rank)

    def checkers_fill(self):
        for rank in self._squares.keys():
            self._checkers[rank] = {}
            for file in self._squares[rank].keys():
                if ((ord(file) - ord('a')) + (rank - 1)) % 2 == 1:
                    if rank < 4:
                        self._checkers[rank][file] = Checker(self._squares[rank][file], "BLACK")
                    elif rank > 5:
                        self._checkers[rank][file] = Checker(self._squares[rank][file], "RED")

    def get_square(self, file: str, rank: int) -> Square:
        return self._squares[rank][file]

    def get_checker(self, file: str, rank: int) -> Checker:
        return self._checkers[rank][file]

    def get_game_mode(self) -> str:
        return self._game_mode

    def get_force_jump(self) -> bool:
        return self._force_jump

