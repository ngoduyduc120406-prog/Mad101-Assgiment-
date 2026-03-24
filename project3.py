def get_knight_positions(m, n, i, j):
    deltas = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
    res = []
    for di,dj in deltas:
        ni = i + di
        nj = j + dj
        if 0 <= ni < m and 0 <= nj < n:
            res.append((ni,nj))
    return res

def find_min_knight_sum(A):
    m = len(A)
    if m == 0:
        return None, None, None
    nn = len(A[0])
    min_sum = 999999999
    best1 = None
    best2 = None
    for i in range(m):
        for j in range(nn):
            neigh = get_knight_positions(m, nn, i, j)
            for ni,nj in neigh:
                if (i < ni) or (i == ni and j < nj):
                    sm = A[i][j] + A[ni][nj]
                    if sm < min_sum:
                        min_sum = sm
                        best1 = (i,j)
                        best2 = (ni,nj)
    return best1, best2, min_sum

def compute_f(n):
    max_sum = -999999999
    deltas = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            for di,dj in deltas:
                ni = i + di
                nj = j + dj
                if 1 <= ni <= n and 1 <= nj <= n:
                    aij = ((-1)**i * (i*i - i)) + ((-1)**j * (j*j - j + 1))
                    anj = ((-1)**ni * (ni*ni - ni)) + ((-1)**nj * (nj*nj - nj + 1))
                    sm = aij + anj
                    if sm > max_sum:
                        max_sum = sm
    return max_sum

if __name__ == "__main__":
    print("PROBLEM 3 - MAD101")
    print("Cau 3.3: f(1000) mod 7001")
    print(compute_f(1000) % 7001)
