class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        LENGTH = len(nums)
        dp = [[0]*2 for _ in range(LENGTH)]
        dp[LENGTH-1][1] = dp[LENGTH-1][0] = nums[LENGTH-1]
        for i in range(LENGTH-2,-1,-1):
            dp[i][1] = max(nums[i], nums[i]+dp[i+1][1])
            dp[i][0] = max(dp[i+1][0], dp[i][1])
        return dp[0][0]
 