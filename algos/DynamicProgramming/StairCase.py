def count_ways_to_reach_stairs(steps_count=0):
    if steps_count == 0:
        return 1
    if steps_count == 1:
        return 1
    if steps_count == 2:
        return 2

    take_1_step = count_ways_to_reach_stairs(steps_count-1)
    take_2_step = count_ways_to_reach_stairs(steps_count-2)
    take_3_step = count_ways_to_reach_stairs(steps_count-3)

    return take_1_step + take_2_step + take_3_step

#essantially this is a fibonacci because for any step n we will need to take step [n-1]+[n-2] and so on
#This program would have been fibonacci if only 1 and 2 steps were allowed
def count_ways_to_reach_stairs_tab(steps_count=0):
    dp = [0 for _ in range(steps_count+1)]
    dp[0], dp[1], dp[2] = 1, 1, 2
    for i in range(3, steps_count+1):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

    return dp[steps_count]

