# Python program to print pattern
# that first reduces 5 one by one,
# then adds 5. Without any loop.

# Recursive function to print
# the pattern.n indicates
# input value m indicates
# current value to be printed
# flag indicates whether we
# need to add 5 or subtract 5.
# Initially flag is True.
def printPattern(n, m, flag):
    # Print m.
    print(m)

    # If we are moving back
    # toward the n and we
    # have reached there,
    # then we are done
    if flag == False and n == m:
        return
    # If we are moving
    # toward 0 or negative.
    if flag:
        # If m is greater, then 5,
        # recur with true flag
        if m - 5 > 0:
            printPattern(n, m - 5, True)
        else:  # recur with false flag
            printPattern(n, m - 5, False)
    else:  # If flag is false.
        printPattern(n, m + 5, False)

    # Driver Code


n = 16
printPattern(n, n, True)

# This code is contributed
# by HrushikeshChoudhary
