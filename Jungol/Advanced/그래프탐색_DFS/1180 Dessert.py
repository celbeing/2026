n = int(input())
results = []
# dep: 현재 숫자
# kep: 아직 연산되지 않은 숫자
# last: 아직 연산되지 않은 연산자
# res: 현재까지 연산결과
# fm: 현재까지 만들어진 수식
def dfs(dep:int, kep:int, last:int, res:int, fm:str):
    if dep == n:
        if res + kep*last: return
        else:
            results.append(fm)
            return

    dfs(dep+1, dep+1, 1, res + kep*last, fm+f'+ {dep+1} ')    # 더하기
    dfs(dep+1, dep+1, -1, res + kep*last, fm+f'- {dep+1} ')       # 빼기
    dfs(dep+1, (kep*10 if dep < 9 else kep*100) + dep+1, last, res, fm+f'. {dep+1} ')       # 이어붙이기

dfs(1, 1, 1, 0, '1 ')

results.sort()
if len(results) > 20:
    for i in range(20):
        print(results[i])
else:
    for l in results:
        print(l)
print(len(results))