class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [None]*(n*2)
        for i in range(len(nums)):
            ans[i], ans[i+n] = nums[i], nums[i]
        return ans
