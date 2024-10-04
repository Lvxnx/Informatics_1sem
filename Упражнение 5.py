n, m = map(int, input().split())
data = [[0] * m for _ in range(n)]

i, j, d = 0, 0, 0
moves = ((0, 1,), (1, 0,), (0, -1,), (-1, 0,),)
for k in range(1, n * m + 1):
    data[i][j] = k
    for l in range(4):
        D = (d + l) % 4
        di, dj = moves[D]
        I, J = i + di, j + dj
        if 0 <= I < n and 0 <= J < m and data[I][J] == 0:
            i, j, d = I, J, D
            break
for n in range(len(data)):
    print(*list(map(lambda x: x * n, data[n])))