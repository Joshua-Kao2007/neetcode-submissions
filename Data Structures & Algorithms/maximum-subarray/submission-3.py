class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.helper(nums, float('-inf'), float('-inf'))
    
    def helper(self, nums:List[int], previous_max:int, global_max:int)->int:
        if not nums:
            return global_max
        cur_num = max(0, previous_max) + nums[0]
        global_max=max(cur_num, global_max)
        return self.helper(nums[1:], cur_num, global_max)