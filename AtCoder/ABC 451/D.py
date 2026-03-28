import sys
input = sys.stdin.readline

pow2 = [1] * 30
for i in range(1, 30):
    pow2[i] = pow2[i-1] * 2
pow2 = list(map(str, pow2))
numbers = []
check = set()

def dfs(now):
    for i in range(30):
        new = now + pow2[i]
        if len(new) < 10:
            if not(new in check):
                numbers.append(int(new))
                check.add(new)
                dfs(new)
        else:
            return

dfs('')
numbers.sort()
n = int(input())
print(numbers[n-1])