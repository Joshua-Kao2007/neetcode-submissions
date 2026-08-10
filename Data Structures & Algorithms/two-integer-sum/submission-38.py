class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        used = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in used:
                return [used[needed], i]
            used[nums[i]] = i
        return -1