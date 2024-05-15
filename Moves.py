import Game
import Square

class Moves:
    def __init__(self):
        self._player_moves = {}
        self._computer_moves = {}
        self._last_move = {}
        self._player_state = 1000
        self._computer_state = 1000

    def load_player_moves(self, checkers: dict) -> None:
        pass

    def load_computer_moves(self, checkers: dict) -> None:
        pass

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

    @property
    def player_moves(self):
        return self._player_moves

    @property
    def computer_moves(self):
        return self._computer_moves

    @property
    def computer(self):
        return self._computer

    @property
    def player(self):
        return self._player

    @property
    def computer_state(self):
        return self._computer_state

    @property
    def player_state(self):
        return self._player_state

    @property
    def last_move(self):
        return self._last_move

    @last_move.setter
    def last_move(self, map):
        self._last_move = map

    def last_move_setter(self, game:Game, start: Square, finish: Square):
        for string in self.last_move:
            game.get_square(int(string[0]), string[1]).color_setter((181, 136, 99))
            string = self._last_move[string]
            game.get_square(int(string[0]), string[1]).color_setter((181, 136, 99))
        start.color_setter((255, 255, 0))
        finish.color_setter((255, 255, 0))
        self._last_move = {str(start):str(finish)}


    @computer.setter
    def computer(self, computer):
        self._computer = computer

    @player.setter
    def player(self, player):
        self._player = player

    @computer_state.setter
    def computer_state(self, value):
        self._computer_state = value

    @player_state.setter
    def player_state(self,value):
        self._player_state = value