class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        # Brute Force...find smallest of tha telement...O(N^2)
        # O(M*N) Time, O(M*N) Space worst case...

        counter = {}
        for li in mat:
            for num in li:
                if num not in counter:
                    counter[num] = 0
                counter[num] += 1
        
        best = float('inf')
        for k,v in counter.items():
            if v == len(mat):
                best = min(k,best)
        
        return best if best != float('inf') else -1
        # - just check one row cuz must be in every row right? If none return -1. O(N*M*K)
        # - since htere's no duplicates...Iterate thru mat once...
        # - Itreate thru again thru dictionary to get smallest element...
        # else -1