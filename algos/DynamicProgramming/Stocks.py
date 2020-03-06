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



