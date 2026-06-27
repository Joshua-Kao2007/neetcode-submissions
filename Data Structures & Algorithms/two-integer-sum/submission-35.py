class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        used = {}
        for idx,num in enumerate(nums):
            used[num] = idx

        for idx,num in enumerate(nums):
            complement = target-num
            if complement in used and idx != used[complement]:
                return [idx,used[complement]]
        return []