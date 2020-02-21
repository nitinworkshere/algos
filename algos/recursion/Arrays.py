class Arrays:

    @staticmethod
    def countoccuranceofnumber(arr, n):
        if not arr:
            return 0
        return (1 if arr[0] == n else 0) + Arrays.countoccuranceofnumber(arr[1:], n)

    @staticmethod
    def invertarray(arr):
        if not arr:
            return []
        return arr[len(arr)-1] + Arrays.invertarray(arr[:len(arr)-1])

    @staticmethod
    def replaceallnegativewithzero(arr, index=0):
        if not arr:
            return []
        if index == len(arr):
            return arr
        if arr[index] < 0:
            arr[index] = 0
        return Arrays.replaceallnegativewithzero(arr, index+1)

    @staticmethod
    def calculateaverage(arr, index=0):
        if index == 0:
            return (arr[index] + Arrays.calculateaverage(arr, index + 1)) / len(arr)
        if index == len(arr) -1:
            return arr[index]
        return arr[index] + Arrays.calculateaverage(arr, index +1)

    @staticmethod
    def parenthesismatching(arr, index, open):
        if index == len(arr) -1:
            return open == 0
        if open < 0:
            return False
        if arr[index] == '(':
            return Arrays.parenthesismatching(arr, index+1, open+1)
        if arr[index] == ')':
            return Arrays.parenthesismatching(arr, index+1, open-1)
