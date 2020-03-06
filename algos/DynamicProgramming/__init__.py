from algos.DynamicProgramming.Fibbonaci import *
from algos.DynamicProgramming.Knapsack import *
from algos.DynamicProgramming.SubsetSum import *
from algos.DynamicProgramming.UnboundedKnapsack import *

print(fibonacci(10))
print(knapsack([1,2,3,5],[1,6,10,16],10,0))

print()
print(find_equal_subset_sum([1,2,3,4]))

print()
print(unbounded_knapsack([1,2,3,5],[1,6,10,16],11,0))

print()


print(coin_change([1,2,3],5))

print()
print(min_coin_change([1,2,3], 5))
