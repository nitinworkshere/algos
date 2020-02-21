class Numbers:
    @staticmethod
    def calculatesquarerecursive(n):
        #Hint use mathematical progression to solve this problem (n - 1)^2 = n^2 -2n + 1 so n^2 = (n -1 )^2 +2*n -1
        if n == 0:
            return 0
        return Numbers.calculatesquarerecursive(n-1) + 2 * n - 1

    @staticmethod
    def firstoccuranceofnumberrecursive(arr, n, index):
        if len(arr) == index: #index has reached last
            return - 1
        if arr[index] == n:
            return index
        index = index + 1
        return Numbers.firstoccuranceofnumberrecursive(arr, n, index)

    @staticmethod
    def powerofnumberrecursive(n, exp):
        if exp == 1:
            return n
        return n * Numbers.powerofnumberrecursive(n, exp - 1)

    @staticmethod
    def sumofintegers(n):
        if n == 1:
            return 1
        return n + Numbers.sumofintegers(n-1)

    @staticmethod
    def modofnumber(dividend, divisor):
        if divisor <= 0:
            return 0
        if divisor > dividend:
            return dividend
        return Numbers.modofnumber(dividend - divisor, divisor)

    @staticmethod
    def greatestcommondivisor(num1, num2):
        if num1 == num2:
            return num1
        if num1 > num2:
            return Numbers.greatestcommondivisor(num1 - num2, num2)
        if num1 < num2:
            return Numbers.greatestcommondivisor(num1, num2 - num1)

    @staticmethod
    def decimaltobinary(num):
        if num <= 1:
            return str(num)
        else:
            return Numbers.decimaltobinary(num//2)+Numbers.decimaltobinary(num%2)


