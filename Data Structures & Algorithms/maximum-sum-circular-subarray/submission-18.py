class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        ext = nums[:]
        for _ in range(0,len(nums)-1):
            ext.append(nums[_])
        global_best = float('-inf')
        for i in range(0, len(nums)): # start element
            cur_sum = 0
            for j in range(i, i+len(nums)):
                cur_sum += ext[j]
                global_best = max(global_best,cur_sum)
        return global_best

