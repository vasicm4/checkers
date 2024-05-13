from Square import *
from Constants import *

class Checker:
    def __init__(self, square: Square, color) -> None:
        self._square = square
        self._color = color
        self._queen = False
        self._eaten = False
        self._side = True if color == "RED" else False
        self.clicked = False

    def draw(self, display) -> None:
        radius = CELL // 2 - PADDING
        pygame.draw.circle(display, self.color, ((ord(self._square._file) - ord('a')) * CELL + CELL // 2, (self._square._rank - 1) * CELL + CELL // 2) , radius)

    def is_clicked(self) -> bool:
        rect = pygame.Rect((ord(self._square._file) - ord('a')) * CELL, (self._square._rank - 1) * CELL, CELL, CELL)
        action = False
        pos = pygame.mouse.get_pos()
        if rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return action

    def promote(self) -> None:
        if self.square.rank == 8 and self._side:
            self._queen = True
        elif self.square.rank ==1 and not self._side:
            self._queen = True

    def move(self, square: Square) -> None:
        self.square = square
        self.promote()

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
