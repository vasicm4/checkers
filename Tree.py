import Moves
import Game
import copy
class Node:
    def __init__(self, moves, game):
        self.moves = moves
        self.game = game
        self.parent = None
        self.children = []

class MovesTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return "MovesTree"

    def add_root(self, moves, game):
        self.root = Node(moves,game)

    def add_node(self, node, moves, game):
        new_node = Node(moves, game)
        node.children.append(new_node)
        new_node.parent = node

    def is_root(self, node):
        return node.parent

    def is_leaf(self, node):
        return node.children

    def parent(self, node: Node):
        return node.parent

    def children(self, node: Node):
        return node.children

    def num_children(self, node: Node):
        return len(node.children)

    def replace(self,old: Node, new:Node):
        new.parent = old.parent
        new.parent.children.remove(old)
        new.parent.children.add(new)
        new.children = old.children
        for child in old.children:
            if child != None:
                child.parent = new

    def generate_tree(self, moves, game, depth):
        self.root = Node(moves, game)
        if depth == 0:
            return self.root

        # Determine current player moves
        if not self.root.game._turn:
            self.root.moves.player_moves = {}
            self.root.moves.load_computer_moves(self.root.game)
            move_dict = self.root.moves.computer_moves
            next_turn = True
        else:
            self.root.moves.computer_moves = {}
            self.root.moves.load_player_moves(self.root.game)
            move_dict = self.root.moves.player_moves
            next_turn = False

        # Iterate over the moves
        for start in move_dict.keys():
            for i in move_dict[start].keys():
                move = move_dict[start][i]
                # Create a new game instance and copy the current game state
                new_game = Game.Game(self.root.game._force_jump)
                for rank in self.root.game._checkers.keys():
                    new_game._checkers[rank] = {}
                    for file in self.root.game._checkers[rank].keys():
                        new_game._checkers[rank][file] = copy.deepcopy(self.root.game._checkers[rank][file])
                # Perform the move
                checker = new_game.checker_in_square(new_game.get_square(int(start[0]), start[1]))
                new_moves = Moves.Moves()
                new_moves.last_move = {start:move}
                new_game.move_checker(checker, move)
                new_game._turn = next_turn

                # Create the child tree
                child_tree = MovesTree()
                child_node = child_tree.generate_tree(new_moves, new_game, depth - 1)
                self.root.children.append(child_node)

        return self.root


    # def generate_tree(self, moves, game, depth):
    #     self.root = Node(moves, game)
    #     if depth == 0:
    #         return self.root
    #     if not self.root.game._turn:
    #         self.root.moves.player_moves = {}
    #         self.root.moves.load_computer_moves(self.root.game)
    #         for start in self.root.moves.computer_moves.keys():
    #             for i in self.root.moves.computer_moves[start].keys():
    #                 moves = Moves.Moves()
    #                 move = self.root.moves.computer_moves[start][i]
    #                 game = Game.Game(self.root.game._force_jump)
    #                 game._checkers = self.root.game._checkers.copy()
    #                 checker = game.checker_in_square(game.get_square(int(start[0]), start[1]))
    #                 moves.last_move_setter(game, checker.square, move)
    #                 game.move_checker(checker, move)
    #                 game._turn = True
    #                 child_node = MovesTree.generate_tree(MovesTree(), moves, game, depth - 1)
    #                 self.root.children.append(child_node)
    #     else:
    #         self.root.moves.computer_moves = {}
    #         self.root.moves.load_player_moves(self.root.game)
    #         for start in self.root.moves.player_moves.keys():
    #             for i in self.root.moves.player_moves[start].keys():
    #                 moves = Moves.Moves()
    #                 move = self.root.moves.player_moves[start][i]
    #                 game = Game.Game(self.root.game._force_jump)
    #                 game._checkers = self.root.game._checkers.copy()
    #                 checker = game.checker_in_square(game.get_square(int(start[0]), start[1]))
    #                 moves.last_move_setter(game, checker.square, move)
    #                 game.move_checker(checker, move)
    #                 game._turn = False
    #                 child_node = MovesTree.generate_tree(MovesTree(), moves, game, depth - 1)
    #                 self.root.children.append(child_node)
    #     return self.root


    def minimax(self, depth, alpha, beta, maxPC):
        if depth == 0 or self.root.game._end:
            return self.root.moves.evaluate(self.root.game), None
        best_move = None
        if maxPC:
            maxEval = float("-inf")
            for child in self.root.children:
                evaluated, _ = self.minimax(depth - 1, alpha, beta, False)
                if evaluated > maxEval:
                    maxEval = evaluated
                    best_move = child
                alpha = max(alpha, evaluated)
                if beta <= alpha:
                    break
            if best_move == None:
                return maxEval, None
            return maxEval, best_move.moves.last_move
        else:
            minEval = float('inf')
            for child in self.root.children:
                evaluated, _ = self.minimax(depth - 1, alpha, beta, True)
                minEval = min(minEval, evaluated)
                beta = min(beta, evaluated)
                if evaluated < minEval:
                    minEval = evaluated
                    best_move = child
                if beta<=alpha:
                    break
            if best_move == None:
                return minEval, None
            return minEval, best_move.moves.last_move

    def depth(self, node):
        pass

    def height(self):
        pass

    def preorder(self):
        pass

    def postorder(self):
        pass




