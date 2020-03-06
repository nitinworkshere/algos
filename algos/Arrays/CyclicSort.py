#given 1 to n numbers in an array sort them in linear time
def cyclic_sort(arr):
    for i in range(len(arr)):
        if arr[i] != i+1:
            j = arr[i] - 1
            arr[i], arr[j] = arr[j], arr[i]
    return arr


print(cyclic_sort([3, 1, 5, 4, 2]))

