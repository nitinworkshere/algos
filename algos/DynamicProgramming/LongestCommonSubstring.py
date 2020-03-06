#metrices in python [[1,2,3],[4,5,6],[7,8,9]] arr = [[num for i in range(col+1)] for j in range(row+1)]
#another way is [[0]*cols]*row and access like a[row][col]

def longest_common_substr(str1, str2):
    return longest_common_substr_rec(str1, str2, 0, 0, 0)


def longest_common_substr_rec(str1, str2, index1, index2, count):
    if index1 >= len(str1) or index2 >= len(str2):
        return count
    if str1[index1] == str2[index2]:
        count = longest_common_substr_rec(str1, str2, index1+1, index2+1, count+1)
    c1 = longest_common_substr_rec(str1, str2, index1+1, index2, 0)
    c2 = longest_common_substr_rec(str1, str2, index1, index2+1, 0)
    return max(count, max(c1, c2))


#look diagonally left-up to +1 if character matches else no need

def longest_common_substr(str1, str2):
    dp = [[0 for i in range(len(str1)+2)] for j in range(len(str2)+2)]

    for row in range(1, len(str2)+1):
        for col in range(2, len(str1)+1):
            if str2[row-1] == str1[col-1]:
                dp[row][col] = 1 + dp[row-1][col-1]

    return dp


print(longest_common_substr('Nitin', 'Shikha'))


