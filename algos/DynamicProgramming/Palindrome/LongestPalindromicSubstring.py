def longest_palindromic_subsequence(st, start_index=0, end_index=0):
    if start_index > end_index:
        return 0
    if start_index == end_index:
        return 1

    if st[start_index] == st[end_index]:
        # check palindrome for inside too
        remaining_length = end_index - start_index - 1
        if remaining_length == longest_palindromic_subsequence(st, start_index+1, end_index-1):
            return 2 + remaining_length

    c1 = longest_palindromic_subsequence(st, start_index+1, end_index)
    c2 = longest_palindromic_subsequence(st, start_index, end_index-1)

    return max(c1, c2)


def find_LPS_length(st):
    n = len(st)
    dp = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = True

    maxLength = 1
    for startIndex in range(n - 1, -1, -1):
        for endIndex in range(startIndex + 1, n):
            if st[startIndex] == st[endIndex]:
                if endIndex - startIndex == 1 or dp[startIndex + 1][endIndex - 1]:
                    dp[startIndex][endIndex] = True
                    maxLength = max(maxLength, endIndex - startIndex + 1)

    return maxLength
