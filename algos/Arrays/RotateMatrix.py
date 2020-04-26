#[[1,2],[3,4]] should become [[3,1], [4,2]]. You just need 1 temp to store first char rest can be done in chain and only last will be replaced
N=4
def rotate_matrix(mat):
    for x in range(len(mat)/2):
        for y in range(x, len(mat)-x-1):
            temp = mat[x][y]
            mat[x][y] = mat[y][N - 1 - x]
            mat[y][N - 1 - x] = mat[N - 1 - x][N - 1 - y]
            mat[N - 1 - x][N - 1 - y] = mat[N - 1 - y][x]
            mat[N - 1 - y][x] = temp

