from math import inf
#Find minimum number of attempts to find which floor is safe to drop out of k
def number_of_attempts_egg_drop(k, n):
    if n == 0:
        return 0
    if k == 1 or k == 0: #if there are 0 or 1 floor then no or only one trial needed
        return k

    trials = inf
    for x in range(1, k+1):
        res = max(number_of_attempts_egg_drop(n-1, x-1), number_of_attempts_egg_drop(n, k-x))
        if res < trials:
            trials = res
    return trials+1
