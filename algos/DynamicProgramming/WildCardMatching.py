def wild_card_matching(str, pat):
    dp = [[False for _ in range(len(str)+1)] for _ in range(len(pat)+1)]

    for i in range(1, len(str)+1):
        for j in range(1, len(pat)+1):
            if str[i-1] == pat[j-1] or pat[j-1] == '?':
                dp[i][j] = dp[i-1][j-1]
            elif pat[j-1] == '*':
                dp[i][j] = dp[i-1][j] or dp[i][j-1]

    return dp[len(str)][len(pat)]



