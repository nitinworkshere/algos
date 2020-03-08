def longest_palindromic_subsequence(str1, start_index=0, end_index=0):
    if start_index > end_index:
        return 0
    if start_index == end_index:
        return 1
    if str1[start_index] == str1[end_index]:
        return 2 + longest_palindromic_subsequence(str1, start_index+1, end_index-1)

    c1 = longest_palindromic_subsequence(str1, start_index+1, end_index)
    c2 = longest_palindromic_subsequence(str1, start_index, end_index-1)

    return max(c1, c2)


def longest_palindromic_subsequence_bottom_up(st):
    n = len(st)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n): # 1 character is palindrome
        dp[i][i] = 1

    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if st[i] == st[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    return dp[0][n-1]
