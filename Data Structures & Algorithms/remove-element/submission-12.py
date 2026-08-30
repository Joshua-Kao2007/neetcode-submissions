class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # delete val in place and shift all elements to left
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1

        return index