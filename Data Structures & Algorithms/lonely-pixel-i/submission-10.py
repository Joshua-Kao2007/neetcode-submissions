# W B W W
# W B B W
# W W W W


class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        # Initalize
        total_b = 0
        m = len(picture)
        n = len(picture[0])


# W W B
# W B W
# B W W

        # Step 1: Go By Row. If good: move to good set. 
        used = set()
        for i in range(len(picture)):
            occur = 0
            save_index = -1
            for j in range(len(picture[i])):
                if picture[i][j] == "B":
                    occur += 1
                    save_index = j
            if occur == 1:
                used.add(save_index)
        
        # Go By Column for each in the used
        used_copy = used.copy()
        for j in used_copy:
            occur = 0
            for k in range(m):
                if picture[k][j] == "B":
                    occur += 1
            if occur > 1:
                used.remove(j)
        return len(used)



        # # Input
        # - M*N (Rectangle). List of Length M, each list of length N
        # - B or W in each list

        # # Output
        # - Integer for B's that are on its own row and its own column 

        # # Brute Force
        # - Two Pass Approach: Store All B's in First Pass. Second Pass Check their row and column. O(M*N) floodfill
        # - O(M*N) start fro each B in a set:
        #     then put all of those in its row and col to zeroO(M*N*(M+N))
        
        # - getting all B's (O(M*N))
        # - checking all of the rows and cols to see if they exist can we do that in O(1) Time?

        # Rows_Valid: 3 rows
        # - store B positions...more than 1B ressest it to W...
        # -  reset to W...
        # - reset to W

        # Cols_Valid
        # - reset to W accordingly

        # All B_Postions:
        # - return final counter

        # O(M*N)...