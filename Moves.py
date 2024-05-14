import Game
import Square

class Moves:
    def __init__(self):
        self._player = {}
        self._computer = {}

    @property
    def computer(self):
        return self._computer

    @computer.setter
    def computer(self, computer):
        self._computer = computer

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        self._player = player

    def left_move_plus(self,game:Game, square:Square):
        if square.file == 'a' or square.rank == 8:
            return
        return game.get_square(square.rank + 1, chr(ord(square.file) - 1))

    def left_move_minus(self,game:Game,  square:Square):
        if square.file == 'a' or square.rank == 1:
            return
        return game.get_square(square.rank - 1, chr(ord(square.file) - 1))

    def right_move_plus(self,game:Game,  square:Square):
        if square.file == 'h' or square.rank == 8:
            return
        return game.get_square(square.rank + 1, chr(ord(square.file) + 1))

    def right_move_minus(self,game:Game,  square:Square):
        if square.file == 'h' or square.rank == 1:
            return
        return game.get_square(square.rank - 1, chr(ord(square.file) + 1))

