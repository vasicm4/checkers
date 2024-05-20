import Game
import Square

class Moves:
    def __init__(self):
        self._player_moves = {}
        self._computer_moves = {}
        self._last_move = {}
        self._player_state = 0
        self._computer_state = 0

    def load_player_moves(self, game: Game) -> None:
        for rank in game._checkers.keys():
            for file in game._checkers[rank].keys():
                hashmap = {}
                square = game.get_square(rank,file)
                if game.get_checker(rank, file):
                    if game.get_checker(rank, file)._eaten:
                        continue
                if game.checker_in_square(square):
                    if game.checker_in_square(square)._side:
                        all = game.checker_in_square(square).all_moves_available(self, game)
                        for i in range(len(all)):
                            hashmap.update({i+1 : all[i]})
                        if len(all) != 0:
                            self._player_moves.update({str(square):hashmap})

    def load_computer_moves(self, game: Game) -> None:
        for rank in game._checkers.keys():
            for file in game._checkers[rank].keys():
                hashmap = {}
                square = game.get_square(rank,file)
                if game.get_checker(rank, file):
                    if game.get_checker(rank, file)._eaten:
                        continue
                if game.checker_in_square(square):
                    if not game.checker_in_square(square)._side:
                        all = game.checker_in_square(square).all_moves_available(self, game)
                        for i in range(len(all)):
                            hashmap.update({i + 1: all[i]})
                        if len(all) != 0:
                            self._computer_moves.update({str(square): hashmap})

    def left_move_plus(self,game:Game, square:Square):
        if square.file == 'a' or square.rank == 8:
            return False
        return game.get_square(square.rank + 1, chr(ord(square.file) - 1))

    def left_move_minus(self,game:Game,  square:Square):
        if square.file == 'a' or square.rank == 1:
            return False
        return game.get_square(square.rank - 1, chr(ord(square.file) - 1))

    def right_move_plus(self,game:Game,  square:Square):
        if square.file == 'h' or square.rank == 8:
            return False
        return game.get_square(square.rank + 1, chr(ord(square.file) + 1))

    def right_move_minus(self,game:Game,  square:Square):
        if square.file == 'h' or square.rank == 1:
            return False
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
        start.color_setter((50,205,50))
        finish.color_setter((34,139,34))
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


    @player_moves.setter
    def player_moves(self, value):
        self._player_moves = value

    @computer_moves.setter
    def computer_moves(self, value):
        self._computer_moves = value