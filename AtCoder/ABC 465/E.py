n = input().strip()
L = len(n)
mod = 998244353

dp = [[[[0] * 2 for _ in range(3)] for _ in range(1024)] for _ in range(L+1)]
dp[0][0][0][0] = 1
# 자릿수
for i in range(L):
    x = int(n[i])

    # 사용한 숫자
    for j in range(1024):

        # 나머지
        for k in range(3):

            # 지금 채울 자리
            for d in range(10):
                bit = 0 if j == 0 and d == 0 else j|(1<<d)
                rem = (k*10+d)%3
                if d <= x:
                    dp[i+1][bit][rem][0 if d == x else 1] += dp[i][j][k][0]
                dp[i+1][bit][rem][1] += dp[i][j][k][1]

    for j in range(1024):
        for k in range(3):
            for l in range(2):
                dp[i+1][j][k][l] %= mod

result = 0
for j in range(1, 1024):
    for k in range(3):
        for l in range(2):
            cond = 0
            if j.bit_count() == 3: cond += 1
            if j & 8: cond += 1
            if k == 0: cond += 1

            if cond == 1:
                result += dp[L][j][k][l]
            result %= mod
print(result)