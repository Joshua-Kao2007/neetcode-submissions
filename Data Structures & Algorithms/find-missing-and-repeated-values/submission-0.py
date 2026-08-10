class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        rows = len(grid)
        nums = set()
        for i in range(rows*rows):
            nums.add(i+1)
        
        a,b = -1,-1
        used = set()
        for i in range(rows):
            for j in range(rows):
                if grid[i][j] in used:
                    a = grid[i][j]
                else:
                    used.add(grid[i][j])
                    nums.remove(grid[i][j])
        
        return [a, next(iter(nums))]

        # set --> used twice than that gets you a
        
        # set containing all the numbers of 1 to n^2. last number remaining is b.

        # set containug all numbers that are added. when exists in set you've found a

        # # O(N) O(N) Solution

        # 1 4
        # 4 2
        # [4,3]