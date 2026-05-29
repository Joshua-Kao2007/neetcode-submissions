class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_num = nums[0]
        cur_num = 0
        for num in nums:
            cur_num = max(cur_num,0)
            cur_num += num
            max_num = max(max_num,cur_num)
        return max_num