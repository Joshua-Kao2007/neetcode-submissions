class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not nums: return
        def helper(i:int, summ:int)-> int:
            if i == len(nums):
                return 1 if summ == target else 0
            return helper(i+1, summ+nums[i]) + helper(i+1, summ-nums[i])

        return helper(0,0)

        # Input: Array nums, integer target. 
        # Constraint: Add or subtract it to tal sum 
        # Output: 
        # How many diff ways to build expression to equal target
        # Will you be given negative numebrs? Can target be negative? 

        # Unsorted nums array with negative, zero, and positive numbers. 
        # Integer target that you need to get to. 
        # REturn number of different expressive combinations to get there. 

    #     # 
    #     [1,1,2], target = 2
    #     1-1+2
    #     1+1-2
    #     2

    #     [2,2,2], target = 2
    #     2+2-2
    #     2-2+2
    #     -2+2+2
    #     3

    #     Brute Force: Try all combinations
    #     +1 or -1
    #     +1 or -1
    #     +2 or -2
    #     O(2^N), O(N) where N is the number of elements in nums
    #     Memoization: O(N), O(N). Store with a Cache. 
    #     Store Two Dimensional (+,-) for each element

    #     True DP:
    #     [2,2,2] target = 2
    #     + -
    # 2.  2 -2
    # 2.  (4,0) (0,-4)
    # 2. (6,2,2,-2). (2,-2,-2,-6)



