# 1 approach can be reverse str1 into str2 and find using longest common substring algorithm
# Manacher's algo (a bit complicated for O(n)
# O(n2) using iterative or recursive


def longest_palindromic_substring_length(str, index1=0, index2=0):
    if index1 > index2:
        return 0
    if index1 == index2:
        return 1
    if str[index1] == str[index2]:
        remain_length = index2 - index1 - 1
        if remain_length == longest_palindromic_substring_length(str, index1+1, index2-1):
            return 2 + remain_length

    c1 = longest_palindromic_substring_length(str, index1+1, index2)
    c2 = longest_palindromic_substring_length(str, index1, index2-1)

    return max(c1, c2)

# first fill for 1 and 2 substring and then fill for rest length by looking at i == j and [i+1][j-1] is True
def longest_palindromic_substring_tab(str):
    n = len(str)
    dp = [[False for _ in range(n)] for _ in range(n)]
    start = 0
    max_length = 0

    #fill for 1
    for i in range(n+1):
        dp[i][i] = True

    #fill for 2
    for i in range(n):
        j = i+1
        if str[i] == str[j]:
            start = i
            dp[i][j] = True

    #now fill for 3 and onwards
    diff = 3
    for diff in range(3, n+1):
        global  diff
        for i in range(n-diff+1):
            j = i + diff - 1
            if str[i] == str[j] and dp[i+1][j-1] is True:
                dp[i][j] = True

            if diff > max_length:
                max_length = diff
                start = i

    return str(i, (i+max_length) - 1)

#which is already palindrom you dont need to cut it. cut the rest length into smaller pieces for all false
def palindrome_partitioning(str, start=0, end=0):
    if start >= end or is_palindrome(str, start, end):
        return 0 #No cut
    min_cuts = end - start

    for i in range(start, end+1):
        if is_palindrome(str, start, i):
            min_cuts = min(min_cuts, 1 + palindrome_partitioning(str, i+1, end))

    return min_cuts

def is_palindrome(str, i, j):
    while i < j:
        if str[i] is not str[j]:
            return False
        i += 1
        j -= 1
    return True


def longestPalindrome(self, s: str) -> str:
    def expandM(s, l, r, length):
        while (l >= 0) and (r < length) and (s[l] == s[r]):
            l -= 1
            r += 1

        return r - l - 1, l + 1

    length = len(s)
    maxLen = 0
    maxPalindromes = {0: ""}

    for i in range(length):
        len1, index1 = expandM(s, i, i, length)
        len2, index2 = expandM(s, i, i + 1, length)
        maxLen = max(maxLen, len1, len2)
        if maxPalindromes.get(maxLen) is None:
            maxPalindromes[maxLen] = s[index1:index1 + maxLen] if maxLen == len1 else s[index2:index2 + maxLen]

    return maxPalindromes[maxLen]
