# Python3 program to find position of
# only set bit in a given number

# A utility function to check
# whether n is power of 2 or
# not.
def isPowerOfTwo(n):
    return (True if (n > 0 and
                     ((n & (n - 1)) > 0))
            else False);


# Returns position of the
# only set bit in 'n'
def findPosition(n):
    if (isPowerOfTwo(n) == True):
        return -1;

    i = 1;
    pos = 1;

    # Iterate through bits of n
    # till we find a set bit i&n
    # will be non-zero only when
    # 'i' and 'n' have a set bit
    # at same position
    while ((i & n) == 0):
        # Unset current bit and
        # set the next bit in 'i'
        i = i << 1;

        # increment position
        pos += 1;

    return pos;


# Driver Code
n = 16;
pos = findPosition(n);
if (pos == -1):
    print("n =", n, ", Invalid number");
else:
    print("n =", n, ", Position ", pos);

n = 12;
pos = findPosition(n);
if (pos == -1):
    print("n =", n, ", Invalid number");
else:
    print("n =", n, ", Position ", pos);

n = 128;
pos = findPosition(n);
if (pos == -1):
    print("n =", n, ", Invalid number");
else:
    print("n =", n, ", Position ", pos);

# This code is contributed by mits
