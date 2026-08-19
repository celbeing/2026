class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.count = 1

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

        p.update()
        x.update()

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

    def find(self, value):
        now = self
        while now is not None:
            if value == now.key:
                now.splay()
                return now

            if value < now.key:
                now = now.left
            else:
                now = now.right
        return None

    def delete(self, value):
        now = self.find(value)
        if now is None:
            return now

        now.splay()
        left = now.left
        right = now.right

        if left is not None:
            left.parent = None
        if right is not None:
            right.parent = None

        now.left = None
        now.right = None

        if left is None:
            return right

        new_root = left

        while new_root.right is not None:
            new_root = new_root.right

        new_root.splay()

        new_root.right = right

        if right is not None:
            right.parent = new_root

        return new_root

    def update(self):
        self.count = 1
        if self.left is not None:
            self.count += self.left.count
        if self.right is not None:
            self.count += self.right.count

    def kth(self, k:int):
        if k < 1 or k > self.count:
            return None

        x = self

        while True:
            l_cnt = x.left.count if x.left is not None else 0

            if k <= l_cnt:
                x = x.left
            elif k == l_cnt + 1:
                x.splay()
                return x
            else:
                k -= l_cnt + 1
                x = x.right

        return None