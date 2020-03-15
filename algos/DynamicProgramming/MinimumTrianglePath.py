# Python 3 program for Dynamic
# Programming implementation of
# Min Sum Path in a Triangle

# Util function to find
# minimum sum for a path
def minSumPath(A):
    # For storing the result in
    # a 1-D array, and simultaneously
    # updating the result.
    memo = [None] * len(A)
    n = len(A) - 1

    # For the bottom row
    for i in range(len(A[n])):
        memo[i] = A[n][i]

    # Calculation of the
    # remaining rows,
    # in bottom up manner.
    for i in range(len(A) - 2, -1, -1):
        for j in range(len(A[i])):
            memo[j] = A[i][j] + min(memo[j],
                                    memo[j + 1]);

        # return the top element
    return memo[0]


# Driver Code
A = [[2],
     [3, 9],
     [1, 6, 7]]
print(minSumPath(A))

# This code is contributed
# by ChitraNayal
