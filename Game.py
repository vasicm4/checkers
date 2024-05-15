from Constants import *
from Square import Square
from Checker import Checker
class Game:
    def __init__(self, forcejump: bool = False) -> None:
        self._force_jump = forcejump
        self._over = False
        self._squares = {}
        self._checkers = {}
        self.squares_fill()
        self.checkers_fill()
        self._turn = True
        self._end = False
        if forcejump:
            self._game_mode = "FORCEJUMP"
        else:
            self._game_mode = "REGULAR"

    def squares_fill(self):
        for rank in RANKS:
            self._squares[rank] = {}
            for file in FILES:
                if ((ord(file) - ord('a')) + (8 - rank)) % 2 == 1:
                    self._squares[rank][file] = Square(file, rank)

    def checkers_fill(self):
        for rank in self._squares.keys():
            self._checkers[rank] = {}
            for file in self._squares[rank].keys():
                if ((ord(file) - ord('a')) + (8 - rank)) % 2 == 1:
                    if rank < 4:
                        self._checkers[rank][file] = Checker(self._squares[rank][file], True)
                    elif rank > 5:
                        self._checkers[rank][file] = Checker(self._squares[rank][file], False)

    def move_checker(self, checker, square):
        self._checkers[checker.square.rank][checker.square.file] = None
        checker.move(square)
        self._checkers[square.rank][square.file] = checker

    def reset(self):
        self._over = False
        self.squares_fill()
        self.checkers_fill()
        self._turn = True
        self._end = False


    def checker_in_square(self,square: Square) -> bool:
        if square.file in self._checkers[square.rank]:
            if self._checkers[square.rank][square.file]:
                return True
        return False



    def get_square(self, rank: int, file: str) -> Square:
        return self._squares[rank][file]


    def get_checker(self, file: str, rank: int) -> Checker:
        return self._checkers[rank][file]

    def get_game_mode(self) -> str:
        return self._game_mode

    def get_force_jump(self) -> bool:
        return self._force_jump

    @property
    def turn(self):
        return self._turn

    @turn.setter
    def turn(self, turn):
        self._turn = turn

    @property
    def is_ended(self):
        return self._end

    def end(self):
        self._end = True