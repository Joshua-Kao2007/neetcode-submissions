class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def helper(i:int,s1:int,s2:int, cache:dict[tuple(int),int]) -> bool:
            if i == len(nums):
                return s1 == s2
            if (i,s1) in cache:
                return cache[(i,s1)]

            cache[(i,s1)] = helper(i+1, s1+nums[i],s2, cache) or helper(i+1,s1,s2+nums[i],cache)
            return cache[(i,s1)]

        if not nums: return True
        if len(nums)==1: return False
        if len(nums)==2: return nums[0] == nums[1]
        cache = {}
        return helper(0, 0, 0, cache)

        

        # Brute Force. Get to the end and see if subsets are equal..



    #     # Input: List of Positive Integer Nums
    #     [1,5,4,3] 
    #     # Unsorted. Are all > 0.

    #     # Output: Boolean if you can paritition them into two subsets
    #     Constraints:
    #     - Don't have to be contiuguous. No restriction. As long as theya re numbers in the subarray. 
    #     - All bnumbers must be used up. No neglecting numbers? Can you neglect numbers? No. 

    #     [1,2,3,4]
    #     - [1,2] [3,4] --> False
    #     - [1,3] [2,4] --> false
    #     - [1,4] [2,3] --> True
    
    #     Brute Force:
    #     - Just Try all subsets and see if the sums are equal
    #     O(2^N), O(N) Space

    #     - Constarint :Time
    #     - Two D Cache. One Column is if you include in subset1. 1 in subset2. 
    #     - Sum

    #     [1,2,3,4]

    #     S1.    S2
    # 0.  1.     
    # 1         
    # 2
    # 3 


        