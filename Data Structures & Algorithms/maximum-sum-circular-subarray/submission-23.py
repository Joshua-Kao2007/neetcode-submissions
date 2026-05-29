class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # [-2,4,-5,4,-5,9,4]
        LENGTH = len(nums)
        bestSum,curSum = float('-inf'), 0
        for i in range(len(nums)):
            curSum = 0
            for j in range(i, i+LENGTH):
                if curSum < 0:
                    curSum = 0
                curSum += nums[j%LENGTH]
                bestSum = max(bestSum, curSum)
        return bestSum