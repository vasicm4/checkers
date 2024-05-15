from Square import *
from Constants import *
import Moves
class Checker:
    def __init__(self, square: Square, side:bool) -> None:
        self._side = side
        self._color = (255,0,0) if side else (0,0,0)
        self._square = square
        self._queen = False
        self._eaten = False
        self._chosen = False
        self._turn = True

    def draw(self, display) -> None:
        radius = CELL // 2 - PADDING
        pygame.draw.circle(display, self.color, ((ord(self._square._file) - ord('a')) * CELL + CELL // 2, (8 - self._square._rank) * CELL + CELL // 2) , radius)

    def promote(self) -> None:
        if self.square.rank == 8 and self._side:
            self._queen = True
        elif self.square.rank == 1 and not self._side:
            self._queen = True

    def moves_available(self, moves, game) -> list[Square]:
        available = []
        if self.is_queen:
            if moves.right_move_minus(game,self._square):
                available.append(moves.right_move_minus(game,self._square))
            if moves.left_move_minus(game, self._square):
                available.append(moves.left_move_minus(game, self._square))
        if moves.left_move_plus(game, self._square):
            available.append(moves.left_move_plus(game, self._square))
        if moves.right_move_plus(game, self._square):
            available.append(moves.right_move_plus(game, self._square))
        pos = []
        eat = []
        for square in available:
            if not game.checker_in_square(square):
                square.color_setter((255, 255, 0))
            else:
                if self.is_queen:
                    if moves.right_move_minus(game, square):
                        if game.checker_in_square(moves.left_move_plus(game,square)):
                            pos.append(square)
                        else:
                            eat.append(square)
                    if moves.left_move_minus(game,square):
                        if game.checker_in_square(moves.left_move_minus(game,square)):
                            pos.append(square)
                        else:
                            eat.append(square)
                if moves.left_move_plus(game, square):
                    if game.checker_in_square(moves.left_move_plus(game, square)):
                        pos.append(square)
                    else:
                        eat.append(square)
                if moves.right_move_plus(game,square):
                    if game.checker_in_square(moves.right_move_plus(game,square)):
                        pos.append(square)
                    else:
                        eat.append(square)
        for el in pos:
            available.remove(el)
        available += eat
        return available

    def moves_reset(self, moves) -> None:
        for element in moves:
            element.color_setter((181, 136, 99))

    def move(self, square: Square) -> None:
        self.square = square
        self.promote()
        self.chosen = False

    @property
    def chosen(self) -> bool:
        return self._chosen

    @chosen.setter
    def chosen(self, chosen: bool) -> None:
        self._chosen = chosen
        if self._chosen:
            self._color = (255,255,0)
        elif self.is_queen:
            self._color = (150,75,0)
        else:
            self._color = (255,0,0)

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
        self._color = (150,75,0)
