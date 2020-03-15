def find_LRS_length(str):
    return find_LRS_length_recursive(str, 0, 0)


def find_LRS_length_recursive(str, i1, i2):
    if i1 == len(str) or i2 == len(str):
        return 0

    if i1 != i2 and str[i1] == str[i2]:
        return 1 + find_LRS_length_recursive(str, i1 + 1, i2 + 1)

    c1 = find_LRS_length_recursive(str, i1, i2 + 1)
    c2 = find_LRS_length_recursive(str, i1 + 1, i2)

    return max(c1, c2)


def find_LRS_length(str):
    n = len(str)
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    maxLength = 0
    # dp[i1][i2] will be storing the LRS up to str[0..i1-1][0..i2-1]
    # this also means that subsequences of length zero(first row and column of
    # dp[][]), will always have LRS of size zero.
    for i1 in range(1, n + 1):
        for i2 in range(1, n + 1):
            if i1 != i2 and str[i1 - 1] == str[i2 - 1]:
                dp[i1][i2] = 1 + dp[i1 - 1][i2 - 1]
            else:
                dp[i1][i2] = max(dp[i1 - 1][i2], dp[i1][i2 - 1])

            maxLength = max(maxLength, dp[i1][i2])

    return maxLength


def main():
    print(find_LRS_length("tomorrow"))
    print(find_LRS_length("aabdbcec"))
    print(find_LRS_length("fmff"))


main()


def main():
    print(find_LRS_length("tomorrow"))
    print(find_LRS_length("aabdbcec"))
    print(find_LRS_length("fmff"))


main()
