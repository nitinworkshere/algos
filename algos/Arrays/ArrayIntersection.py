#Given two array intersection

def array_intersection(arr1, arr2, arr =[]):
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            arr.append(arr1[i])
            i += 1
            j += 1

