class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globalMax = float('-inf')
        localMax = float('-inf')
        for num in nums:
            localMax = max(localMax,0)+num
            globalMax = max(globalMax, localMax)
        return globalMax