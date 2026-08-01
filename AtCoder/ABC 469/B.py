n = int(input())
s = 'x'+input().strip()+'x'
count = 0
for i in range(1, n+1):
    if s[i-1] == s[i] == s[i+1] == 'x':
        count += 1
print(count)