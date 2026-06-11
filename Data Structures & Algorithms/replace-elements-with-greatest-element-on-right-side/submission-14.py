class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # 1 One Pass from the right
        best = -1
        for i in range(len(arr)-1, -1, -1):
            tmp = arr[i]
            arr[i] = best
            best = max(tmp, best)
        return arr