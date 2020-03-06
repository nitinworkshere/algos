#Problem boils down to fixing one digit a[i] and finding sum-a[i] from remaining array (using binary search)
#We can use hash map too to see if any sum-a[i] is already processed

def find_two_sum(arr, sum, dict={}):
    for i in range(len(arr)):
        if dict.__contains__(sum - arr[i]):
            return arr[i], dict[sum-arr[i]]
        else:
            dict[arr[i]] = arr[i]
    return -1, -1

print(find_two_sum([2,7,11,15], 10))

