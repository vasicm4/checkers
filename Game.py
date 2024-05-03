from Constants import *
from Square import Square
class Game:
    def __init__(self, forcejump: bool = False) -> None:
        self._force_jump = forcejump
        self._over = False
        self._squares = {}
        self._checkers = []
        if forcejump:
            self._game_mode = "FORCEJUMP"
        else:
            self._game_mode = "REGULAR"
    def squares_fill(self):
        for rank in RANKS:
            self._squares[rank] = {}
            for file in FILES:
                if ((ord(file) - ord('a')) + (rank - 1)) % 2 == 0:
                    self._squares[rank][file] = Square(file, rank)
