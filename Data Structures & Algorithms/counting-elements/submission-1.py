class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr_set = set(arr)
        cnt = 0
        for num in arr:
            if num+1 in arr_set:
                cnt += 1
        return cnt