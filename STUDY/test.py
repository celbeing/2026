n = int(input())
def star(k):
    if k > n: return
    print('*'*k)
    star(k+1)
star(1)