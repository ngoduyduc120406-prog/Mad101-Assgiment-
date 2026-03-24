def product(M, N):
    p11 = M[0][0] * N[0][0] + M[0][1] * N[1][0]
    p12 = M[0][0] * N[0][1] + M[0][1] * N[1][1]
    p21 = M[1][0] * N[0][0] + M[1][1] * N[1][0]
    p22 = M[1][0] * N[0][1] + M[1][1] * N[1][1]
    return [[p11, p12], [p21, p22]]

A = [[3, -4], [2, -1]]
B = [[2, -3], [1, 4]]

def tinh_An_Bn(n):
    if n == 0:
        return [[1, 0], [0, 1]], [[0, 0], [0, 0]]
    if n == 1:
        return [[3, -4], [2, -1]], [[-2, 3], [-1, -4]]
    An = [[3, -4], [2, -1]]
    Bn = [[-2, 3], [-1, -4]]
    for i in range(2, n + 1):
        AA = product(A, An)
        BB = product(B, Bn)
        BB13 = [[0, 0], [0, 0]]
        BB13[0][0] = BB[0][0] // 13
        BB13[0][1] = BB[0][1] // 13
        BB13[1][0] = BB[1][0] // 13
        BB13[1][1] = BB[1][1] // 13
        new_An = [[0, 0], [0, 0]]
        new_An[0][0] = AA[0][0] - BB13[0][0]
        new_An[0][1] = AA[0][1] - BB13[0][1]
        new_An[1][0] = AA[1][0] - BB13[1][0]
        new_An[1][1] = AA[1][1] - BB13[1][1]
        ABn = product(A, Bn)
        BAn = product(B, An)
        new_Bn = [[0, 0], [0, 0]]
        new_Bn[0][0] = ABn[0][0] - BAn[0][0]
        new_Bn[0][1] = ABn[0][1] - BAn[0][1]
        new_Bn[1][0] = ABn[1][0] - BAn[1][0]
        new_Bn[1][1] = ABn[1][1] - BAn[1][1]
        An = new_An
        Bn = new_Bn
    return An, Bn

if __name__ == "__main__":
    print("PROBLEM 2 - MAD101")
    print("Cau 1: product(M, N)")
    A_test = [[3, -4], [2, -1]]
    B_test = [[2, -3], [1, 4]]
    C = product(A_test, B_test)
    print(A_test[0])
    print(A_test[1])
    print(B_test[0])
    print(B_test[1])
    print("A * B =")
    print(C[0])
    print(C[1])
    print("\nCau 2: tinh An va Bn")
    n = int(input("Nhap n: "))
    An, Bn = tinh_An_Bn(n)
    print("An =")
    print(An[0])
    print(An[1])
    print("Bn =")
    print(Bn[0])
    print(Bn[1])
