def edit_distance(str1, str2, index1, index2):
    if index1 == len(str1):
        return len(str2)-index2

    if index2 == len(str2):
        return len(str1)-index1

    if str1[index1] == str2[index2]:
        return edit_distance(str1, str2, index1+1, index2+1)

    #perform deletion
    c1 = 1 + edit_distance(str1, str2, index1+1, index2)
    #perform insertion
    c2 = 1 + edit_distance(str1, str2, index1, index2+1)
    #update
    c3 = 1 + edit_distance(str1, str2, index1+1, index2+1)

    return min(c1, min(c2,c3))


def edit_distance_tab(str1, str2):
    dp = [[-1 for _ in range(len(str1)+1)] for _ in range(len(str2))]

    for i in range(len(str1)+1):
        dp[i][0] = i

    for j in range(len(str2)+1):
        dp[0][j] = j

    for i in range(i, len(str1)+1):
        for j in range(1, range(len(str2)+1)):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], min(dp[i][j-1], dp[i-1][j-1]))
    return dp[len(str1), len(str2)]


