# For any dp[i][j] if str1[i] matches str2[j] then 1+ diagonally left up else max  (left or top)

#complexity time and space both is O(n*m)
def longest_common_subsequence(str1, str2):
    dp = [[0 for i in range(len(str1)+2)] for j in range(len(str2)+2)]

    for row in range(1, len(str2)+1):
        for col in range(2, len(str1)+1):
            if str2[row-1] == str1[col-1]:
                dp[row][col] = 1 + dp[row-1][col-1]
            else:
                dp[row][col] = max(dp[row][col-1], dp[row-1][col])
    return dp

#complexity time O(2^(n+m)) space is O(n+m)
def longest_common_subsequence_rec(str1, str2, index1=0, index2=0):
    if index1 == len(str1) or index2 == len(str2):
        return 0
    if str1[index1] == str2[index2]:
        return 1 + longest_common_subsequence_rec(str1, str2, index1+1, index2+1)
    c1 = longest_common_subsequence_rec(str1, str2, index1+1, index2)
    c2 = longest_common_subsequence_rec(str1, str2, index1, index2+1)

    return max(c1, c2)

def minimum_insert_delete_to_convert_str1_str2(str1, str2):
    lcs = longest_common_subsequence_rec(str1, str2)
    min_deletion = len(str1)-lcs
    min_insertion = len(str2)-lcs
    return min_deletion, min_insertion


def shortest_super_common_seq(str1, str2, index1, index2):
    n1, n2 = len(str1), len(str1)

    if str1 == n1:
        return str2 - n2
    if str2 == n2:
        return str1 - n1

    length1, length2 = 0, 0
    if str1[index1] == str2[index2]:
        return 1 + shortest_super_common_seq(str1, str2, index1 + 1, index2 + 1)
    else:
        length1 = 1 + shortest_super_common_seq(str1, str2, index1+1, index2)
        length2 = 1 + shortest_super_common_seq(str1, str2, index1, index2+1)

    return  min(length1, length2)

def shortest_super_common_seq_tab(str1, str2):
    dp = [[0 for _ in len(str1)+1] for _ in len(str2)+1]

    for i in range(len(str1)+1):
        dp[0][i] = i

    for j in range(len(str2)+1):
        dp[j][0] = j

    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if str[i-1] == str[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
    return dp[len[str1]][len(str2)]


#This algo is a variation of lcs where both str1 and str2 are same
def longest_repeating_subseq(str, index1=0, index2=0):
    if index1 == len(str) or index2 == len(str):
        return 0
    if str[index1] == str[index2]:
        return 1 + longest_common_subsequence_rec(str, index1+1, index2+1)
    c1 = longest_common_subsequence_rec(str, index1+1, index2)
    c2 = longest_common_subsequence_rec(str, index1, index2+1)

    return max(c1, c2)




