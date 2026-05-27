import sys
from collections import deque

def solution():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    dq = deque()
    res = []
    for i in range(n):
        while dq and dq[0] <= i - w:
            dq.popleft()
        while dq and a[dq[-1]] <= a[i]:
            dq.pop()
        dq.append(i)
        if i >= w - 1:
            res.append(str(a[dq[0]]))
    print("\n".join(res))

solution()