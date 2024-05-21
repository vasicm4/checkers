class Node:
    def __init__(self, start, end, evaluation):
        self.start = start
        self.end = end
        self.parent = None
        self.children = []

class MovesTree:
    def __init__(self):
        self.root = None
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        return "MovesTree"

    @property
    def root(self):
        return self.root

    def add_root(self, last_move, evaluation):
        for key in last_move.keys():
            for value in last_move.values():
                Node(key, value, evaluation)

    def add_node(self, node, start, end, evaluation):
        new_node = Node(start, end, evaluation)
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

    def minimax(self, position, depth, alpha, beta, maxPC):
        if depth == 0:
            return node.evaluation
        if maxPC:
            maxEval = -10000000
            for child in self.children():
                pos = self.minimax(position, depth - 1, alpha, beta, False)
                alpha = max(alpha, pos)
                if beta <= alpha:
                    break
            return maxEval
        else:
            minEval = 10000000
            for child in self.children():
                eval = self.minimax(position, depth - 1, alpha, beta, True)
                minEval = min(minEval, eval)
                beta = min(beta, eval)
            return minEval

    def depth(self, node):
        pass

    def height(self):
        pass

    def preorder(self):
        pass

    def postorder(self):
        pass




