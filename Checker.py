from Square import *
from Constants import *

class Checker:
    def __init__(self, square: Square) -> None:
        self._square = square
        self._is_queen = False
        self._is_eaten = False

    @property
    def is_eaten(self) -> bool:
        return self._is_eaten

    def eat(self) -> None:
        self._is_eaten = True

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
