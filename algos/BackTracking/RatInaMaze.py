def rat_in_a_maze(maze):
    sol = [[0 for _ in range(len(maze))] for _ in range(len(maze))]


def rat_in_a_maze_helper(maze, x, y, sol):
    N = len(maze)
    if x == N-1 and y == N-1:
        sol[x][y] = 1
        return True

    if can_move(maze, x, y):
        sol[x][y] = 1 #first mark this visited than make possible next moves
        if rat_in_a_maze_helper(maze, x+1, y, sol):
            return True
        if rat_in_a_maze_helper(maze, x, y+1, sol):
            return True
        sol[x][y] = 0
        False



def can_move(maze, x, y):
    if len(maze) > x >= 0 and len(maze) > y >= 0 and maze[x][y] == 1:
        return True
    return False

