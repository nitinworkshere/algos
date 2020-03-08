def count_ways(n):
    if n == 0:
        return 1
    if n <= 2:
        return n

    take1Step = count_ways(n-1)
    take2Step = count_ways(n-2)
    take3Step = count_ways(n-3)

    return take1Step + take2Step + take3Step


def count_ways_bottom_up(n):
    dp = [0 for _ in range(n+1)]

    dp[0], dp[1], dp[2] = 1, 1, 2

    for i in range(3, n+1):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

    return dp[n]

