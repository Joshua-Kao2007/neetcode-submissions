class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        mat3 = [[0] * n for _ in range(m)]
        # 1: Brute Force:
        # for i in range(m):
        #     for col in range(n):
        #         for j in range(k):
        #             mat3[i][col] += mat1[i][j]*mat2[j][col] 
        # return mat3

        # 2: Abstraction Summarization
        # (1,0) --> represnts value 1 at index 0
        tmp_mat1 = [[] for _ in range(m)]
        for i in range(m):
            for j in range(k):
                if mat1[i][j] != 0:
                    tmp_mat1[i].append((mat1[i][j], j))

        tmp_mat = [[] for _ in range(n)]
        for col in range(n):
            for row in range(k):
                if mat2[row][col] != 0:
                    tmp_mat[col].append((mat2[row][col], row))
        

        for i in range(m):
            for j in range(n):
                for num,col in tmp_mat1[i]:
                    for num2,row in tmp_mat[j]:
                        if col == row:
                            mat3[i][j] += num*num2
        
        return mat3
