def square_sorted_array(arr):
    N = len(arr)
    square_array = [0 for _ in range(len(arr))]

    left, right = 0, N-1
    higher_sqr_index = N-1 #in new array we will fill from right as we are comparing greater

    while left < right:
        leftSquare = arr[left] * arr[left]
        rightSquare = arr[right] * arr[right]

        if leftSquare > rightSquare:
            square_array[higher_sqr_index] = leftSquare
            right -= 1
        else:
            square_array[higher_sqr_index] = leftSquare
            left += 1
        higher_sqr_index -= 1
    return  square_array
