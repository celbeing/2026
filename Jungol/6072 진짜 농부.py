def solution():
    n = int(input())
    h = list(map(int, input().split()))
    a = list(map(int, input().split()))
    t = list(map(int, input().split()))

    order = sorted(range(n), key=lambda i: t[i])
    print(order)

for _ in range(int(input())):
    solution()