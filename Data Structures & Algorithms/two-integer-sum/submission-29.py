class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = sorted(nums)
        used = set()
        li = {}
        for idx,num in enumerate(nums):
            needed = target-num
            if needed in used:
                return [li[needed],idx]
            used.add(num)
            li[num] = idx

        return 