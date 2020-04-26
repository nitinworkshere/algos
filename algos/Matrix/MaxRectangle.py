class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        t = [int(n) for n in matrix[0]]
        mx = 0
        mx = max(mx, self.maxHisto(t + [0]))
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    t[j] = 0
                else:
                    t[j] += int(matrix[i][j])

            mx = max(mx, self.maxHisto(t + [0]))

        return mx

    def maxHisto(self, arr):
        mx = 0
        stack = []
        i = 0
        while i < len(arr):
            if len(stack) == 0 or arr[stack[-1]] <= arr[i]:
                stack.append(i)
                i += 1
            else:
                index = stack.pop()
                h = arr[index]
                w = i
                if stack:
                    w = i - stack[-1] - 1

                mx = max(mx, w * h)

        return mx
