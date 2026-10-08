class Solution:
    def countElements(self, arr: List[int]) -> int:
        cnt = 0
        x = set(arr)
        for num in arr:
            if num+1 in x:
                cnt += 1
        return cnt
