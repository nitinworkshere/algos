def fibonacci(num, memo=[]):
    memo = [-1 for x in range(0, num+1)]
    return fibonacci_recursive(num, memo)


def fibonacci_recursive(num, memo):
    if num < 2:
        memo[num] = num
        return num
    if memo[num] is not -1:
        return memo[num]
    memo[num] = fibonacci_recursive(num-2, memo) + fibonacci_recursive(num-1, memo)
    return memo[num]


def fibonacci_iterative(num):
    memo = [-1 for x in range(0, num+1)]
    memo[0] = 0
    memo[1] = 1
    for i in range(2, num+1):
        memo[i] = memo[i-2] + memo[i-1]

    return memo[num]


print(fibonacci(10))
print(fibonacci_iterative(10))