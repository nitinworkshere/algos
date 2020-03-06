#Factorial complexity and space O(n*n)

def place_n_queen(board, col=0): #we will go column wise all column done should mean we have reached the final
    board = [[0 for _ in range(len(board))] for _ in range(len(board[0]))]

    if col >= len(board):
        return True

    for i in range(len(board)):
        if is_safe(board, col):
            board[i][col] = 1
            if place_n_queen(board, col+1): #move to next column
                return True
            board[i][col] = 0 #Kinda undo what we just did and trackback on same column with different row
    return False


#you only need to check on left side in row or even diagonally and reason is we are filling it columnwise left to right
def is_safe(board, row, col):
    #left row
    for i in range(col):
        if board[row][i]:
            return False
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


