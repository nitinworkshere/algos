def uniquePaths(m: int, n: int):
    if n == 0 or m == 0:
        return 1
    mat = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                mat[i][j] = 1
            else:
                mat[i][j] = mat[i - 1][j] + mat[i][j - 1]
    return mat[n - 1][m - 1]


def uniquePathsWithObstacles(obstacleGrid):
    n, m = len(obstacleGrid), len(obstacleGrid[0])
    A = [[0] * m for _ in range(n)]
    A[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

    for i in range(n):
        for j in range(m):
            if i == j == 0:
                continue
            if obstacleGrid[i][j] == 0:
                if j == 0:
                    A[i][j] = A[i - 1][j]
                elif i == 0:
                    A[i][j] = A[i][j - 1]
                else:
                    A[i][j] = A[i - 1][j] + A[i][j - 1]
            elif obstacleGrid[i][j] == 1:
                A[i][j] = 0

    return A[n - 1][m - 1]


print(uniquePaths(5, 5))