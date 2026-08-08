n = int(input())
color = [0] * (n+1)
for c in list(map(int, input().split())):
    color[c] += 1
print(n-max(color))