class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 1 Always brute force linear search, min_value variable
        # x = float('inf')
        # for num in nums:
        #     x = min(num,x)
        # return x

        #2 O(Logn) some type of binary search algorithm
        L,R,min_value = 0, len(nums)-1, float('inf')
        while L < R-1:
            mid = L + (R-L)//2 #why
            if nums[L] < nums[mid] < nums[R]: # middle must be on left side
                R = mid-1
            elif nums[mid] > nums[L] and nums[mid] > nums[R]: # must be on right side
                L = mid+1
            else:
                R = mid

        return min(nums[L],nums[R])


        # Scope out all the diff cases of bsearch and write an algo that satisfies them all
        # Middle elemnt can either be the tip
        # [3,4,5,6,1,2] --> find the tip of the original array
        # [4,5,2] --> 2
        # [6,1,2,3,4] --> 
        # [5,1,2,3,4] --> n = 1 --> middle is less than both ends, on left side
        # [4,5,1,2,3] --> n = 2 --> middle is less than both, is the middle
        # [3,4,5,1,2] --> n = 3 --> middle is greater than both, is on right side
        # [2,3,4,5,1] --> n = 4 --> middle is greater than both, is on right side
        # [1,2,3,4,5] --> n = 5 --> middle is in between, is on left side
        # [7,1,2,3,4,5,6] --> lessn than both --> middle is on left
        # [6,7,1,2,3,4,5] --> less than both --> middle is on left
        # [5,6,7,1,2,3,4] --> less than both middle is it
        # [4,5,6,7,1,2,3] --> greater than both --> middle is on right
        # [3,4,5,6,7,1,2] --> greater than both --> middle is on right
        # [2,3,4,5,6,7,1] --> greater tha both --> middle is on right
        # [1,2,3,4,5,6,7] --> in between both --> middle is on left

        # [1,2,3,4,5,6] --> n=1 -->middle is in between on left side
        # [6,1,2,3,4,5] --> middle is less than both, middle is on the left side
        # [5,6,1,2,3,4] --> middle is less than both, on left side
        # [4,5,6,1,2,3] --> middle is less than both, is it
        # [3,4,5,6,1,2] --> middle is greater than both, on right side
        # [2,3,4,5,6,1] --> middle is greater than both on right