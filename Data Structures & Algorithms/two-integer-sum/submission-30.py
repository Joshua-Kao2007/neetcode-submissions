class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        used = {}
        for idx,num in enumerate(nums):
            needed = target - num
            if needed in used:
                return [used[needed],idx]
            used[num] = idx
        return []