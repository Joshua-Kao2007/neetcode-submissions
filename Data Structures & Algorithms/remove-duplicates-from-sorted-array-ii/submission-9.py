class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Given an integer array sorted in non-decreasing order..so increasing with chance of equal signs
        # Remove duplicates in place such that each unique element can only appear at most twice
        # nums = [1,1,1,2,2,3] --> nums = [1,1,2,2,3,_] --> this would return 5
        # One pointer k simply points to the place in memory of the bad index
        # have index L traversing the list
        L = 0
        LENGTH = len(nums)
        for num in nums:
            if L < 2 or num != nums[L-2]:
                nums[L] = num
                L += 1
        return L


        # LENGTH = len(nums)
        # counter = {}
        # L = 0
        # for R in range(LENGTH):
        #     num = nums[R]
        #     if num not in counter:
        #         counter[num] = 0
        #     counter[num]+= 1
        #     if counter[num] > 2:
        #         continue
        #     nums[L] = num
        #     L += 1
        # return L
