class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = [[None]*2 for _ in range(len(nums))]
        def helper(i:int, flag:bool)->int:
            if i == len(nums)-1:
                return max(0,nums[i])if flag else nums[i]
            if memo[i][flag]:
                return memo[i][flag]
            if flag:
                memo[i][flag] = max(0, nums[i]+helper(i+1,flag))
            else:
                memo[i][flag] = max(nums[i]+helper(i+1,True), helper(i+1,False))
            return memo[i][flag]
        return helper(0, False)