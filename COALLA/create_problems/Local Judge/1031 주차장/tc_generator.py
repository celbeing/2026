from collections import deque
from heapq import heappush, heappop
from random import random, randint, shuffle
check = set()
path = r"C:\Users\kimsd\Documents\2026\COALLA\create_problems\Local Judge\1031 주차장\\"

# 7~20시 주차요금 = 시간당 1500원
# 시간 외 주차요금 = 시간당 2000원

for tc in range(1, 21):
    ent = randint(1, 20)
    out = randint(ent+1, 24)
    while (ent, out) in check:
        ent = randint(1, 20)
        out = randint(ent + 1, 24)

    fee = 0

    for t in range(ent, out):
        if 7 <= t < 20:
            fee += 1500
        else:
            fee += 2000

    with open(path + f"{tc}.in", "w", encoding="utf-8") as file:
        file.write(f"{ent} {out}\n")

    with open(path + f"{tc}.out", "w", encoding="utf-8") as file:
        file.write(f"{fee}\n")