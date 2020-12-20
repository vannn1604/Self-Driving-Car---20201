def ptdt(P, Q):
    # [1,2], [3,4] => ax + by = c
    a = Q[1] - P[1]
    b = P[0] - Q[0]
    c = a * (P[0]) + b * (P[1])
    return a, b, c


def giao_diem(arr1, arr2):
    # [4,3,32], [4,-2,12] => [x, y]
    import numpy as np

    a = np.array([[arr1[0], arr1[1]], [arr2[0], arr2[1]]])
    b = np.array([arr1[2], arr2[2]])
    try:
        return np.linalg.solve(a, b)
    except:
        return None


def distance(a, b):
    import math

    return math.dist(a, b)


def nam_giua(a, b, c):
    # c nam giua a va b
    crossproduct = (c[1] - a[1]) * (b[0] - a[0]) - (c[0] - a[0]) * (b[1] - a[1])
    
    dotproduct = (c[0] - a[0]) * (b[0] - a[0]) + (c[1] - a[1]) * (b[1] - a[1])
    if dotproduct < 0:
        return False

    squaredlengthba = (b[0] - a[0]) * (b[0] - a[0]) + (b[1] - a[1]) * (b[1] - a[1])
    if dotproduct > squaredlengthba:
        return False

    return True


if __name__ == "__main__":
    # ko dc co 2 nga tu lien nhau
    a = [1, 5, 9]  # list diem duong di, returned by get_path
    d = {1:[32,43]} # toa do
    b = [
        {1: [2, 3]},
        {5: [11, 12, 13, 14]},
        {9: [6, 8]},
    ]  # list diem 2 ben cua cac diem trong a
    kq = []
    for i, c in enumerate(a, 1):
        if len(b[c]) == 4:  # nga tu, co 4 diem canh trong tap b
            duong_1, duong_2 = ptdt(c, a[i - 1]), ptdt(
                c, a[i + 1]
            )  # 2 doan tren duong di
            for e in b[c]:
                pt11 = ptdt(c)
            

        # else: # ko phai nga tu
