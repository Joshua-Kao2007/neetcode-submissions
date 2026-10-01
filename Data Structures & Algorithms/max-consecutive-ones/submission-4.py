class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best, cur_count = 0,0
        for num in nums:
            best = max(best, cur_count)
            if num == 1:
                cur_count += 1
            else:
                cur_count = 0
        return max(best, cur_count)
