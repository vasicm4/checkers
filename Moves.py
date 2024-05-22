import Game
import Square
from Constants import *

class Moves:
    def __init__(self):
        self._player_moves = {}
        self._computer_moves = {}
        self._last_move = {}

    def count_checkers(self, game: Game) -> tuple:
        player_state = 0
        computer_state = 0
        for rank in game._checkers.keys():
            for file in game._checkers[rank].keys():
                if game.checker_in_square(game.get_square(rank,file)):
                    if game.checker_in_square(game.get_square(rank,file))._side:
                        player_state += BASIC_PIECE
                        if game.checker_in_square(game.get_square(rank,file)).is_queen:
                            player_state += QUEEN_WEIGHT
                        if rank > 5:
                            player_state += ADVANCED
                        if (file == 'a' or file == 'h') and (rank == 1 or rank == 8):
                            player_state += CORNER
                        elif file == 'a' or file == 'h':
                            player_state += WALL
                    else:
                        computer_state += BASIC_PIECE
                        if game.checker_in_square(game.get_square(rank,file)).is_queen:
                            computer_state += QUEEN_WEIGHT
                        if rank < 4:
                            computer_state += ADVANCED
                        if (file == 'a' or file == 'h') and (rank == 1 or rank == 8):
                            computer_state += CORNER
                        elif file == 'a' or file == 'h':
                            player_state += WALL
        return player_state, computer_state


    def evaluate(self, game: Game) -> int:
        player_state, computer_state = self.count_checkers(game)
        for square in self._computer_moves.keys():
            for i in self._computer_moves[square].keys():
                if abs(self._computer_moves[square][i].rank - self._computer_moves[square][i].rank) == 2:
                    computer_state += ATTACK_WEIGHT
                    player_state += CAN_BE_CAPTURED
        for square in self._player_moves.keys():
            for i in self._player_moves[square].keys():
                if abs(self._player_moves[square][i].rank - self._player_moves[square][i].rank) == 2:
                    player_state += ATTACK_WEIGHT
                    player_state += CAN_BE_CAPTURED
        return computer_state - player_state


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
        if len(self._player_moves) == 0:
            game._end = True
        if game._game_mode == "FORCEJUMP":
            to_eat = []
            for start in self._player_moves.keys():
                for i in self._player_moves[start].keys():
                    if abs(int(start[0]) - self.player_moves[start][i].rank) == 2:
                        to_eat.append({start:self._player_moves[start][i]})
            if len(to_eat) != 0:
                self._player_moves = {}
                for hashmap in to_eat:
                    for key in hashmap.keys():
                        try:
                            self._player_moves[key].update({key:{len(self._player_moves[key]) + 1:hashmap[key]}})
                        except KeyError:
                            self._player_moves.update({key:{1:hashmap[key]}})

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
        if len(self._computer_moves) == 0:
            game._end = True
        if game._game_mode == "FORCEJUMP":
            to_eat = []
            for start in self._computer_moves.keys():
                for i in self._computer_moves[start].keys():
                    if abs(int(start[0]) - self._computer_moves[start][i].rank) == 2:
                        to_eat.append({start:self._computer_moves[start][i]})
            if len(to_eat) != 0:
                self._computer_moves = {}
                for hashmap in to_eat:
                    for key in hashmap.keys():
                        try:
                            self._computer_moves[key].update({key:{len(self._player_moves[key]) + 1:hashmap[key]}})
                        except KeyError:
                            self._computer_moves.update({key:{1:hashmap[key]}})

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

    def last_move_color(self, game):
        for key in self._last_move:
            game.get_square(int(key[0]), key[1]).color_setter((50,205,50))
            game.get_square(int(self._last_move[key][0]), self._last_move[key][1]).color_setter((34,139,34))



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