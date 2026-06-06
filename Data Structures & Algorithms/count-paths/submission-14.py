class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Edge Cases
        if m <= 0 or n <= 0: return 0
        if m == 1 or n == 1: return 1

        # Intialization Variables
        # - Intialize the whole Grid of Values
        # - Initialize all last row and last column values to 1
        # - Store all Previous Row Values
        # grid = [[0]*n for _ in range(m)]
        # for c in range(n-1, -1, -1):
        #     grid[m-1][c] = 1
        # for r in range(m-1, -1, -1):
        #     grid[r][n-1] = 1
        # prev_row = grid[m-1]

        # Core Algorithm
        # - Bottom right [m-1][n-1] to Top left [0][0]
        # - Computing right side element + prev_row element
        # - Updating prev_row (M)
        prev_row = [1]*n
        for r in range(m-2, -1, -1):
            right_element = 1
            for c in range(n-2, -1, -1):
                cur_element = right_element + prev_row[c]
                right_element, prev_row[c] = cur_element, cur_element
        
        return prev_row[0]






#         # Two Ints: M and N.  M represents rows. N represents columns
#         Constraints: 1) Move down or to the right
#         # Integer representing unique paths from top left to bottom right
#         Top Left: [0][0], Bottom right = [M-1][N-1]

#         Edge Cases:
#         - M = 0. N = 0. 0
#         - M = 1, N = 0, 0
#         If any M or N is zero: return 0

#         - M =1 N =1 1
#         - M = 1, N = 2. 1
#         - M = 2, N = 2. DR, RD --> 2
#         - M = 3, N = 2. DDR, DRD, RDD --> 3
        
#         Brute Force: Current position: (i,j)
#         - You always have the optionality of going down or right. 
#             - Down: (i+1, j)
#             - Right: (i, j+1)
#         - Constraint: Cannot go left or up. 
#         - The amount of ways to get to [M-1,N-1] from your current position is simply the sum of
#         the amount of ways to get right from the next down position and the next right position. 
#         - you are next step down or your next step right is the bottom right position. You return 1. 
#         - O(2^N) Time O(N) space
#         Constraint: Time

#         1) Memoization. O(N*M) Time O(N*M) space

#         2) DP. O(N*M) Time, O(min(N, M)) space
#         Constraint: What is the minimum amount of information I need to store to get what I nee?
# M=2,N=2. Minimum is element below you and element to your right. Two variables?
#         x 1
#         1 x

# M = 3, n = 3
# down,rigth = 1,2. 
#         x x 1
#         x 2 1
#         1 1 x
# space complexity: O(M)
# min(O(N), O(M))
