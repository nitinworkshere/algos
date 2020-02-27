def fibonacci(num, memoize=[]):
    memoize = [-1 for x in range(num+1)]
    if num < 2:
        return num
    if memoize[num] >= 0:
        return memoize[num]

    memoize[num] = fibonacci(num-1, memoize) + fibonacci(num-2, memoize)
    return memoize[num]

def fibonacci_bottom_up_tabulation(num):
    fib = [0, 1]
    for i in range(2, num+1):
        fib.append(fib[i-1] + fib[i-2])

    return fib(num)
