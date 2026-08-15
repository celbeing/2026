class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

    def set_left(self, child):
        self.left = child
        if child is not None:
            child.parent = self

    def set_right(self, child):
        self.right = child
        if child is not None:
            child.parent = self

    def rotate(self):
        x = self
        p = x.parent
        if p is None:
            return

        g = p.parent

        if p.left is x:
            p.left = x.right
            if x.right is not None:
                x.right.parent = p
            x.right = p
        else:
            p.right = x.left
            if x.left is not None:
                x.left.parent = p
            x.left = p

        x.parent = g
        if g is not None:
            if g.left is p:
                g.left = x
            else:
                g.right = x
        p.parent = x

    def splay(self):
        while self.parent is not None:
            x = self
            p = x.parent
            if p.parent is None:
                x.rotate()
                return
            g = p.parent
            if (g.left is p) == (p.left is x):
                p.rotate()
            else:
                x.rotate()
            x.rotate()

    def insert(self, value):
        now = self

        while 1:
            if value < now.key:
                if now.left is None:
                    new_node = Node(value)
                    now.left = new_node
                    new_node.parent = now
                    break
                now = now.left

            else:
                if now.right is None:
                    new_node = Node(value)
                    now.right = new_node
                    new_node.parent = now
                    break
                now = now.right

        new_node.splay()
        return new_node