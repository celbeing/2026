from collections import deque
from heapq import heappush, heappop
from random import random, randint, shuffle
check = set()
path = r"C:\Users\kimsd\Documents\2026\COALLA\create_problems\Local Judge\문제번호\\"

for tc in range(1, 21):
    with open(path + f"{tc}.in", "w", encoding="utf-8") as file:
        file.write(f"\n")

    with open(path + f"{tc}.out", "w", encoding="utf-8") as file:
        file.write(f"\n")