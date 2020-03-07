def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        merge_sort(arr[:mid])
        merge_sort(arr[mid:])

arr = [5, 2, 4, 7]
print(arr)
merge_sort(arr)
print(arr)

