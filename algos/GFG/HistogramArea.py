# 3, 1, 2, 4
def largestRectangleArea(heights):
    if not heights or len(heights) == 0:
        return 0
    n = len(heights)
    maxArea = 0
    stack = []
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            idx = stack.pop()
            leftIdx = stack[-1] if stack else -1
            rightIdx = i
            maxArea = max(maxArea, heights[idx] * ((idx - leftIdx) + (rightIdx - idx) - 1))
        stack.append(i)
    while stack:
        idx = stack.pop()
        leftIdx = stack[-1] if stack else -1
        rightIdx = n
        maxArea = max(maxArea, heights[idx] * ((idx - leftIdx) + (rightIdx - idx) - 1))
    return maxArea
