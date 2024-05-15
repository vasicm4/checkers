class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []

class MovesTree:
    def __init__(self,value):
        self.root = Node(value)
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        return "MovesTree"

    @property
    def root(self):
        return self.root

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

    def depth(self, node):
        pass

    def height(self):
        pass

    def preorder(self):
        pass

    def postorder(self):
        pass




