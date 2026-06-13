class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i in range(len(heights)):
            idx = i
            while stack and stack[-1][0] > heights[i]:
                val,idx = stack.pop()
                max_area = max((i-idx)*val, max_area)
            stack.append((heights[i],idx))
        
        while stack:
            tmp = stack.pop()
            max_area = max(max_area, (len(heights)-tmp[1]) * tmp[0])
        return max_area
            