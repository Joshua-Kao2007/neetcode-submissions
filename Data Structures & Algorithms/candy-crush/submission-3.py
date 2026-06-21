# Strategy 1: Use a set for all that need to be crushed
# Strategy 2: Delete them all
# Streatgy 3: Then replacing them all...

# Option 2: Instead of using a set, just change them to negative numbers

class Solution:
    def find(self,board,m,n):
        used = set()
        for row in range(m):
            for col in range(n-2):
                if board[row][col] == board[row][col+1] == board[row][col+2] and board[row][col]!=0:
                    used.add((row,col))
                    used.add((row,col+1))
                    used.add((row,col+2))
        
        # Col-First Iteration
        for col in range(n):
            for row in range(m-2):
                if board[row][col] == board[row+1][col] == board[row+2][col] and board[row][col] != 0:
                    used.add((row,col))
                    used.add((row+1,col))
                    used.add((row+2,col))

        for (row,col) in used:
            board[row][col] = 0
        return True if len(used)>0 else False
        
    def drop(self, board, m, n):
        for col in range(n):
            write = m-1
            for row in range(m-1, -1, -1):
                if board[row][col] != 0:
                    board[write][col] = board[row][col]
                    write -= 1
            for row in range(write, -1, -1):
                board[row][col] = 0

    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        # Three or more candies are adjcaent vertical or hozintally must be crushed
        used = set()
        m = len(board)
        n = len(board[0])
        while self.find(board,m,n):
            self.drop(board, m, n)
        return board
