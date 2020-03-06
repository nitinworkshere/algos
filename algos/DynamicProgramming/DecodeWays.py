#think of it as fibonacci till we reach that the length
def decode_ways(digits, n): # digits is array and n is length
    dp = [0 for _ in range(n+1)]
    dp[0], dp[1] = 0, 1

    for i in range(2, n+1):
        if digits[i-1] > 0:
            dp[i] = dp[i-1]

        if digits[i-2] == 1 or (digits[i-2] == 2 and digits[i-1] < 7):
            dp[i] += dp[i-2]

    return dp[n]


