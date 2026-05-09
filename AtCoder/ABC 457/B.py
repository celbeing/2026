n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
x, y = map(int, input().split())
print(a[x-1][y])