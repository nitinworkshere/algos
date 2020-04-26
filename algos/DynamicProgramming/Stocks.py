from math import  inf
#case1 when only one transaction allowed
def max_buy_sell(prices):
    profit = 0
    lowest = inf

    for i in range(prices):
        if prices[i] < lowest:
            lowest = prices[i] #lowest price I have seen so far
        else:
            profit = max(profit, prices[i] - lowest) #find max profit by looking at max of current max profit or if i sell today with minimum buy price

    return profit


#case2 where non overlapping transactions can be done
def max_buy_sell_multiple(prices):
    profit = 0
    if prices:
        for i in range(len(prices)):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i] #only sell when price is getting bigger

    return profit


# Python3 Program to find
# best buying and selling days

# This function finds the buy sell
# schedule for maximum profit
def stockBuySell(price, n):
    # Prices must be given for at least two days
    if n == 1:
        return

    # Traverse through given price array
    i = 0
    while i < (n - 1):

        # Find Local Minima
        # Note that the limit is (n-2) as we are
        # comparing present element to the next element
        while ((i < (n - 1)) and
               (price[i + 1] <= price[i])):
            i += 1

        # If we reached the end, break
        # as no further solution possible
        if i == n - 1:
            break

        # Store the index of minima
        buy = i
        i += 1

        # Find Local Maxima
        # Note that the limit is (n-1) as we are
        # comparing to previous element
        while ((i < n) and (price[i] >= price[i - 1])):
            i += 1

        # Store the index of maxima
        sell = i - 1

        print("Buy on day: ", buy, "\t",
              "Sell on day: ", sell)

    # Driver code


# Stock prices on consecutive days
price = [100, 180, 260, 310, 40, 535, 695]
n = len(price)

# Fucntion call
stockBuySell(price, n)


# This is code contributed by SHUBHAMSINGH10

#i is no of transactions and j is day
def maxProfit_k_times(prices, n, k):
    # Bottom-up DP approach
    profit = [[0 for i in range(k + 1)]
              for j in range(n)]

    # Profit is zero for the first
    # day and for zero transactions
    for i in range(1, n):

        for j in range(1, k + 1):
            max_so_far = 0

            for l in range(i):
                max_so_far = max(max_so_far, prices[i] -
                                 prices[l] + profit[l][j - 1])

            profit[i][j] = max(profit[i - 1][j], max_so_far)

    return profit[n - 1][k]


# Driver code
k = 2
prices = [10, 22, 5, 75, 65, 80]
n = len(prices)

