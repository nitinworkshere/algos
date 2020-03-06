def find_generated_subset(arr):
    subsets = []
    subsets.append([])

    for num in arr:
        for i in range(len(subsets)):
            new_set = list(subsets[i]) #most important line
            new_set.append(num)
            subsets.append(new_set)
    return subsets


print(find_generated_subset([1, 5, 3]))