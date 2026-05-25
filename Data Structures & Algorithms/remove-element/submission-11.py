class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        R = len(nums)-1
        for L in range(len(nums)-1, -1, -1):
            if nums[L] == val: #then swap
                nums[L], nums[R] = nums[R], nums[L]
                R -= 1
        return R + 1