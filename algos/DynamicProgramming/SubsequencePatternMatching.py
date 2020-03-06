#This algo is a variation of LCS the only difference is that we need to keep count
#If pattern len reached return 1, if string length reached return 0

def subseq_pattern_matching(str, pat, index=0, pat_index=0):
    if pat_index == len(pat): # full match
        return 1
    if str == len(str): #nothing matched
        return 0

    count = 0
    if str[index] == pat[index]:
        count = 1 + subseq_pattern_matching(str, pat, index+1, pat+1)
    c1 = subseq_pattern_matching(str, pat, index+1, pat)
    return count + c1

def subseq_pattern_matching_tab(str, pat):
    strLen, patLen = len(str), len(pat)
    # every empty pattern has one match
    if patLen == 0:
        return 1

    if strLen == 0 or patLen > strLen:
        return 0

    # dp[strIndex][patIndex] will be storing the count of SPM up to str[0..strIndex-1][0..patIndex-1]
    dp = [[0 for _ in range(patLen + 1)] for _ in range(strLen + 1)]

    # for the empty pattern, we have one matching
    for i in range(strLen + 1):
        dp[i][0] = 1

    for strIndex in range(1, strLen + 1):
        for patIndex in range(1, patLen + 1):
            if str[strIndex - 1] == pat[patIndex - 1]:
                dp[strIndex][patIndex] = dp[strIndex - 1][patIndex - 1]
            dp[strIndex][patIndex] += dp[strIndex - 1][patIndex] #notice += here as we want to add

    return dp[strLen][patLen]


