class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n # climbStairs(0) = 0, climbStairs(1) = 1, climbStairs(2) = 2
        x,y = 1,2
        for i in range(3, n+1):
            tmp = y
            y = x+y
            x = tmp
        return y
       
       
       
        # Integer N. Number of steps in staircase
        # Output: Integer. Disctint ways to get to top. 

#         n = 2. 2 steps in the staircase. Constraints: >0. n = 0. 0. n=1. 1. n = 2. 2 ways to climb it
#         Distinct ways to climb 2 steps
#            2
#         1 
#       0
#         Brute Force: 1-1, 2-0. 2

#      n = 5. 5 steps in this stairacase. 
#     Output: distinct ways to climb 5 steps
#                         5
#                     4
#                 3
#             2
#         1
#     0

#     1-2-3-4-5
#     1-2-3-5
#     1-2-4-5
#     1-3-4-5
#     1-3-5
#     2-3-4-5
#     2-3-5
#     2-4-5
# 8

# Brute Force: Recursive approach. amount of ways to get to the top if i go 2 steps + amount of ways to get to the top if i go 1 step, with the base cases aove. 
# Time Complexity: O(2^N), Space: O(N)

# Limitations: Time is exponential. 
# Optimize:
# - 1) Memoization/caching
# - Time would e lienar, No recomputation. 

# - 2) Dynamic Programming. 
# - n = 0...just computing all the way up to n so breaking it down into the littlest subproblems and adding onto n until we are at n
# - Time would also be linear. 
# - O(1) space complexity

