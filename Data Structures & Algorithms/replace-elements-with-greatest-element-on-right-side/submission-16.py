class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        best_val = -1
        for i in range(len(arr)-1, -1, -1):
            tmp = arr[i]
            arr[i] = best_val
            best_val = max(best_val, tmp)
        return arr