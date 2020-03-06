#[2, 2, 0, 1, 2, 0]

def dutch_flag_sort(arr):
    low, high = 0, len(arr) - 1
    i = 0
    while i <= high:
        if arr[i] == 0:
            arr[i], arr[low] = arr[low], arr[i]
            low += 1
            i += 1
        elif arr[i] == 1:
            i += 1 # we are in right place move on
        else:
            arr[i], arr[high] = arr[high], arr[low]
            high -= 1 # notice i also doesn't have to increase as