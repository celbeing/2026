def solution():
    n = int(input())
    if n & 1:
        print(0)
        return

    n >>= 1
    prefix = 1
    result = 1
    for _ in range(n):
        result = prefix * 2 + result
        prefix += result
    print(result)
solution()