def quick_sort(arr, low, high):
    if low < high:
        p = find_pivot(arr, low, high)
        quick_sort(arr, low, p-1)
        quick_sort(arr, p+1, high)


def find_pivot(arr, low, high):
    i = high+1  #imaginary higher number
    pivot = arr[low]
    for j in range(high, low, -1):

