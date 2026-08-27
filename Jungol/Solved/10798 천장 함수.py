class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def add(self, node):
        if node < self.key:
            if self.left == None:
                self.left = Node(node)
            else:
                self.left.add(node)
        else:
            if self.right == None:
                self.right = Node(node)
            else:
                self.right.add(node)

    def shape(self):
        res = [self.key]
        if self.left is not None:
            res += self.left.shape()
        if self.right is not None:
            res += self.right.shape()
        return res

def comp(arr):
    dc = dict()
    for i, a in enumerate(sorted(arr),start=1):
        dc[a] = i
    res = [dc[a] for a in arr]
    tree = Node(0)
    for r in res:
        tree.add(r)

    return tree.shape()

def solution():
    n, k = map(int, input().split())
    count = set()
    for _ in range(n):
        count.add(tuple(comp(tuple(map(int, input().split())))))
    print(len(count))

solution()