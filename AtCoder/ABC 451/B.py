import sys
input = sys.stdin.readline
n, m = map(int, input().split())

depart = [0] * (m+1)
for _ in range(n):
    a, b = map(int, input().split())
    depart[a] -= 1
    depart[b] += 1

for i in range(1, m+1):
    print(depart[i])