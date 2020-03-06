def string_interleaving(str1, str2, pat, index1, index2, index):
    if index1 == len(str1) and index2 == len(str2) and index == len(pat): #everthing matched in subsequence
        return True

    if index == len(pat): # some chars left to match in input strings
        return False

    b1, b2 = False
    if index1 < len(str1) and str1[index1] == index[pat]:
        b1 = 1 + string_interleaving(str1+1, str2, pat+1)

    if index2 < len(str2) and str2[index2] == index[pat]:
        b2 = 1 + string_interleaving(str1+1, str2, pat+1)

    return b1 or b2


def string_interleaving_tab(m, n, p):
    mLen, nLen, pLen = len(m), len(n), len(p)
    # dp[mIndex][nIndex] will be storing the result of string interleaving
    # up to p[0..mIndex+nIndex-1]
    dp = [[False for _ in range(nLen + 1)] for _ in range(mLen + 1)]

    # for the empty pattern, we have one matching
    if mLen + nLen != pLen:
        return False

    for mIndex in range(mLen + 1):
        for nIndex in range(nLen + 1):
            # if 'm' and 'n' are empty, then 'p' must have been empty too.
            if mIndex == 0 and nIndex == 0:
                dp[mIndex][nIndex] = True
            # if 'm' is empty, we need to check the interleaving with 'n' only
            elif mIndex == 0 and n[nIndex - 1] == p[mIndex + nIndex - 1]:
                dp[mIndex][nIndex] = dp[mIndex][nIndex - 1]
            # if 'n' is empty, we need to check the interleaving with 'm' only
            elif nIndex == 0 and m[mIndex - 1] == p[mIndex + nIndex - 1]:
                dp[mIndex][nIndex] = dp[mIndex - 1][nIndex]
            else:
                # if the letter of 'm' and 'p' match, we take whatever is matched till mIndex-1
                if mIndex > 0 and m[mIndex - 1] == p[mIndex + nIndex - 1]:
                    dp[mIndex][nIndex] = dp[mIndex - 1][nIndex]
                # if the letter of 'n' and 'p' match, we take whatever is matched till nIndex-1 too
                # note the '|=', this is required when we have common letters
                if nIndex > 0 and n[nIndex - 1] == p[mIndex + nIndex - 1]:
                    dp[mIndex][nIndex] |= dp[mIndex][nIndex - 1]

    return dp[mLen][nLen]
