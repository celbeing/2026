n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [(b[i]-(a[i]+a[i+1]))%m for i in range(n-1)]
print(c)