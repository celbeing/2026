from random import randint

ls = [[randint(1, 9) for _ in range(8)] for _ in range(6)]
for l in ls: print(*l)