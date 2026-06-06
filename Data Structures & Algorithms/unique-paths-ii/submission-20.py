class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:return 0
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        if m <= 0 or n <= 0: return 0

        prev_row = [1]*(n)
        for c in range(n-1,-1,-1):
            if obstacleGrid[m-1][c] == 1:
                prev_row[:c+1] = [0]*(c+1)
                break

        for r in range(m-2, -1, -1):
            if obstacleGrid[r][n-1] == 1:
                prev_row[n-1] = 0
            for c in range(n-2, -1, -1):
                if obstacleGrid[r][c] == 1:
                    prev_row[c] = 0
                else:
                    prev_row[c] += prev_row[c+1]
        
        return prev_row[0]