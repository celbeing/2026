import sys
input = sys.stdin.readline

total = [0] * 7
dice = [i for i in range(7)]
for _ in range(int(input())):
    a, b, c, d, e, f = map(int, input().split())
    total[dice[a]] += max(b, c, d, e)
    total[dice[b]] += max(a, c, e, f)
    total[dice[c]] += max(a, b, d, f)
    total[dice[d]] += max(a, c, e, f)
    total[dice[e]] += max(a, b, d, f)
    total[dice[f]] += max(b, c, d, e)

    dice[a], dice[f] = dice[f], dice[a]
    dice[b], dice[d] = dice[d], dice[b]
    dice[c], dice[e] = dice[e], dice[c]

print(max(total))