def solution():
    n = int(input())
    paper = [[''] * n for _ in range(n)]
    s = input().strip()
    l = len(s)
    stack = []
    idx = 0
    def dfs(d, x, y):
        nonlocal idx
        if s[idx] == 'X':
            idx += 1
            dfs(d//2, x, y)
            idx += 1
            dfs(d//2, x, y+d//2)
            idx += 1
            dfs(d//2, x+d//2, y)
            idx += 1
            dfs(d//2, x+d//2, y+d//2)
        else:
            stack.append((x, y, d, s[idx]))
    dfs(n, 0, 0)
    for x, y, d, k in stack:
        for i in range(x, x+d):
            for j in range(y, y+d):
                paper[i][j] = k
    print(n)
    res = ''
    for a in paper:
        res += ' '.join(a) + '\n'
    print(res.strip())
solution()