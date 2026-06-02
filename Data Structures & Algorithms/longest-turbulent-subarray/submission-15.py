class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # Edge case: if length of arr is less than 2 just return ...not if identical elements
        if len(arr)==1:return 1
        max_len, cur_sign, cur_len = 0, None, 1
        dp = [0]*len(arr)
        dp[len(arr)-1] = 1
        for R in range(len(arr)-2, -1, -1):
            if not cur_sign:
                if arr[R] > arr[R+1]:
                    cur_sign = '<'
                    cur_len += 1
                elif arr[R] < arr[R+1]:
                    cur_sign = '>'
                    cur_len += 1
                else:
                    cur_len = 1
                    cur_sign = None
            else:
                if cur_sign == '<':
                    if arr[R] < arr[R+1]:
                        cur_len += 1
                        cur_sign = '>'
                    elif arr[R] > arr[R+1]:
                        cur_len = 2
                        cur_sign = '<'
                    else:
                        cur_len = 1
                        cur_sign = None
                elif cur_sign == '>':
                    if arr[R] > arr[R+1]:
                        cur_len += 1
                        cur_sign = '<'
                    elif arr[R] < arr[R+1]:
                        cur_len = 2
                        cur_sign = '>'
                    else:
                        cur_len = 1
                        cur_sign = None
                        
            max_len = max(max_len, cur_len)
            dp[R] = max_len

        return dp[0]


        # # Given a list of integers, return the length of the maximum turblent subarray of arr such that they alterante by which numbers are greater

        # # Case 1:
        # [5,9,7,11,9,13] Working Subarray

        # # Case 2:
        # [9,5,8,7] Not working Subarray

        # # Constraints: The actual checking if subarray is good or not
        # - Simulation

        # # Getting of the subarray
        # - Sliding Window
        # - Brute Force
    
        # Some sort of two pass solution is needed here to avoid recomputation
        # Maximum Size Turbulent subarray. So sliding window is of variable size. 

        # we can start at each index, go the maximum turbulent subarray and do that at the start of every index. Lots of recomputation. O(N^2)
        # Can we save if something works as a subarray or not? 
        # We can use dynamic programming to do the saving of if something is a subarray or not to avoid recomputation. 
        # Find the maximum subarray starting at each index. 

        # [9,5,8,7]
        # start at the last element
        # so at 7 --> max subarray is length 1 it works

        # add in 8
        # 8 > 7 --> Max subarray is length 2...because 8 > 7..next element needs to be less than 8...is it less than 8? Keep track of sign...
        # If it is less than 8...max subarray is three. switch signs. if not then just switch ma subarray back to 1 or set the current subarray
        # to 1. Which means that the sign can be whatever. You'll miss the intersection. 

        # When it breaks --> just set max subarray to 2..




