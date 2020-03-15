def longest_common_substring(st1, st2, index1=0, index2=0, count=0):

    if index1 >= len(st1) or index2 >= len(st2):
        return count

    if st1[index1] == st2[index2]:
        count = longest_common_substring(st1, st2, index1+1, index2+1, count+1)

    c1 = longest_common_substring(st1, st2, index1+1, index2, 0)
    c2 = longest_common_substring(st1, st2, index1, index2+1, 0)

    return max(count, max(c1, c2))


def find_LCS_length(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
    maxLength = 0
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                maxLength = max(maxLength, dp[i][j])
    return maxLength


def main():
    print(find_LCS_length("abdca", "cbda"))
    print(find_LCS_length("passport", "ppsspt"))


main()
