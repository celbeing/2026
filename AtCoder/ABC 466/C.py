n = int(input())


res = 0
l = 1
for r in range(2, n+1):
    while l < r:
        print(f'? {l} {r}', flush=True)
        if input() == 'Yes':
            res += r-l
            break
        l += 1
print(f'! {res}', flush=True)