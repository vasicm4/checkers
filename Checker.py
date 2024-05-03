from Square import *
from Constants import *

class Checker:
    def __init__(self, square: Square, color) -> None:
        self._square = square
        self._color = color
        self._queen = False
        self._eaten = False

    def draw(self, display) -> None:
        radius = CELL // 2 - PADDING
        pygame.draw.circle(display, self.color, (self.square.x, self.square.y), radius)
        if self.is_queen:
            pygame.draw.circle(display, (0, 0, 0), (self.square.x, self.square.y),  radius+BORDER)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def is_eaten(self) -> bool:
        return self._eaten

    def eat(self) -> None:
        self._eaten = True

    @property
    def square(self) -> Square:
        return self._square

    @square.setter
    def square(self, square: Square) -> None:
        self._square = square

    @property
    def is_queen(self) -> bool:
        return self._queen

    @is_queen.setter
    def is_queen(self, queen: bool) -> None:
        self._queen = queen
