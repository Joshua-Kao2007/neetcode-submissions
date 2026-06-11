class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        used = set()
        for num in nums:
            used.add(num)
        return len(nums) != len(used)