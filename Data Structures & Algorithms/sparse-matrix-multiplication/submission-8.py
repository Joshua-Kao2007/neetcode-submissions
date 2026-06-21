class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        mat3 = [[0] * n for _ in range(m)]
        # 1: Brute Force:
        for i in range(m):
            for col in range(n):
                for j in range(k):
                    mat3[i][col] += mat1[i][j]*mat2[j][col] 
        return mat3

        # 2: Abstraction Summarization