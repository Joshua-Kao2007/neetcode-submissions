class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        # Initialize
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        res = [[[] for _ in range(n)] for _ in range(m)]

        # Core Algorithm
        for i in range(m):
            cur_row = mat1[i]
            for j in range(n):
                cur_val = 0
                for row in range(k):
                    cur_val += (mat2[row][j] * mat1[i][row])
                res[i][j] = cur_val
        return res

            
        
        
        # - Take Each Row of Mat1
        # - Go Thru Each Col of Mat2. Go thru eaceh row of that column. Fill in that position of the column/row with addition of all of its products. 

        # [1,0,0]



        # Output: M X N. 