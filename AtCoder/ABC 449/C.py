ab = 'qwertyuiopasdfghjklzxcvbnm'
count = dict()
for a in ab:
    count[a] = 0
n, l, r = map(int, input().split())
s = input().strip()
small, large = 0, 0

start, end = 0, l - 1
for i in range(l):
    small += count[s[i]]
    count[s[i]] += 1

while end < n - 1:
    count[s[start]] -= 1
    start += 1
    end += 1
    small += count[s[end]]
    count[s[end]] += 1

for a in ab:
    count[a] = 0
start, end = 0, r
for i in range(r + 1):
    large += count[s[i]]
    count[s[i]] += 1

while end < n - 1:
    count[s[start]] -= 1
    start += 1
    end += 1
    large += count[s[end]]
    count[s[end]] += 1

print(large - small)