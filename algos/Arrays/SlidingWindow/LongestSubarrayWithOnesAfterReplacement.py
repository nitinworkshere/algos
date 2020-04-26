# Python3 program to find length
# of longest subsegment of all 1's
# by changing at most k 0's

def longestSubSeg(a, n, k):
    cnt0 = 0
    l = 0
    max_len = 0;

    # i decides current ending point
    for i in range(0, n):
        if a[i] == 0:
            cnt0 += 1

        # If there are more 0's move
        # left point for current
        # ending point.
        while (cnt0 > k):
            if a[l] == 0:
                cnt0 -= 1
            l += 1

        max_len = max(max_len, i - l + 1);

    return max_len


# Driver code
a = [1, 0, 0, 1, 0, 1, 0, 1]
k = 2
n = len(a)
print(longestSubSeg(a, n, k))

# This code is contributed by Smitha Dinesh Semwal
