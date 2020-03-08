def longest_palindromic_subseq(str):
    return longest_palindromic_subseq_rec(str, 0, len(str)-1)


def longest_palindromic_subseq_rec(str, start, end):
    if start > end:
        return 0
    if start == end:
        return 1

    if str[start] == str[end]:
        return 2 + longest_palindromic_subseq_rec(str, start+1, end-1)

    c1 = longest_palindromic_subseq_rec(str, start+1, end)
    c2 = longest_palindromic_subseq_rec(str, start, end-1)
    return max(c1, c2)

# step 1 start with start_index and end_index difference 1 then 2 then 3 and go till difference is entire length of string
#trick is only upper diagonal needs to be filled lower no required as we are looking for palindrome
def longest_palindromic_subseq_tab(str):
    n = len(str)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for diff in range(2, n+1): # difference will go from 2 to all chars in string
        for i in range(n-diff+1): # i could only reach to length - diff window +1 and j will automatically be placed at i+diff-1 location
            j = i + diff - 1
            if str[i] == str[j] and diff == 2:
                dp[i][j] = 2
            elif str[i] == str[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])
    return dp[0][n-1]

#return str total length - palindrome subsequence max length to find minimum number of deletion
def find_minimum_number_of_deletion_to_make_palindrome(str):
    return len(str) - longest_palindromic_subseq_tab(str)





