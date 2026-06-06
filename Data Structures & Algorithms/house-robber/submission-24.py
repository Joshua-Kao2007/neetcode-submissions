class Solution:
    def rob(self, nums: List[int]) -> int:
        LENGTH = len(nums)
        if not nums:return 0
        if LENGTH==1: return nums[0] #we know nums[i] >= 0
        if LENGTH==2: return max(nums[0], nums[1])
        if LENGTH==3: return max(nums[0], nums[1], nums[2], nums[0]+nums[2])
        cache = [-1]* (LENGTH)
        self.helper(0, nums, cache)
        print(cache)
        return cache[0]
    
    def helper(self, i:int, nums: List[int], cache: List[int]):
        if i >= len(nums):
            return 0
        if cache[i] != -1:
            return cache[i]
        cache[i] = max(self.helper(i+1, nums, cache), nums[i]+self.helper(i+2, nums,cache))
        return cache[i]



        # cache[2] = MAX money you can rob from element 0 to element 2
        # Return cache[len(nums)-1] = MAX money you can rob from element 0 to elemtn n-1
        # Input: Integer array nums. Each element in nums represents the amount of money in the ith house. 
        # Output: Integer. Max amount of money you can rob without alerting the police. 
        # Constraints: 
        # - Houses are arranged in a straight line
        # - ith house is the neighbor of i-1th and i+1th house.
        # - Two adjaceent houses = alerting the police. 
        # - If you rob house #1 you can't rob house 0 or house 2. 
        # - 0th house and the n-1th house, only has 1 neighbor. 

        # Edge Case:
        # - 0. Return 0—no houses to rob
        # - 1. Money is always 0 or positive. Return nums[0]
        # - 2. Return max(nums[0], nums[1])
        # - 3
        #     [3,9,6]

        #     1) Steal house 0 + house 2 --> 9
        #     2) Steal house 1 --> 9
        #     3) Steal house 0 --> 3
        #     4) Steal house 2 --> 6

        # - 4
        #     [4,5,8,9]

        #     1) Steal house 0 --> 4
        #     2) Steal house 1 --> 5
        #     3) setal ohuse 2 --> 8
        #     4) steal house 3 --> 9
        #     5) steal ohuse 0 and house 2 --> 12
        #     6) steal house 1 and house 3 --> 14
        
        # Brute Force:
        # - Try all legitimate combinations
        # - If I steal, value = cur_value + recursive(i+2)...skip recursive(i+1)
        # - O(2^N) Time Complexity. O(N)

        # Constraints: Exponential Time. Lots of recomputation. 

        # - 1) Caching/memoization. O(N), O(N)

