from collections import deque

dq = deque()
n = int(input())
s = input().strip()

back = 1
for i in range(n):
    if back:
        dq.append(i+1)
    else:
        dq.appendleft(i+1)

    if s[i] == 'o':
        back ^= 1
if back == 0:
    dq.reverse()

print(*dq)