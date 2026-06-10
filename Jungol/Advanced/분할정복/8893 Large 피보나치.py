def mat_comp(mat1, mat2):
    ret = [mat1[0]*mat2[0]+mat1[1]*mat2[2],
           mat1[0]*mat2[1]+mat1[1]*mat2[3],
           mat1[2]*mat2[0]+mat1[3]*mat2[2],
           mat1[2]*mat2[1]+mat1[3]*mat2[3]]
    for i in range(4):
        ret[i] %= 1_000_000_007
    return ret

def mat_power(k):
    bit = 1
    while bit <= k: bit <<= 1
    bit >>= 1

    mat = [1,0,0,1]
    while bit:
        mat = mat_comp(mat, mat)
        if k & bit:
            mat = mat_comp(mat, [1,1,1,0])
        bit >>= 1
    return mat[1]

def solution():
    while True:
        n = int(input())
        if n == -1: break
        elif n == 0: print(0)
        else: print(mat_power(n))

solution()