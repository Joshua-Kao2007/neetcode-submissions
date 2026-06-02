class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # if len(arr) < 2: return len(arr)
        n = len(arr)
        up = [1]*n
        down = [1]*n
        ans = 1
        for x in range(1, n):
            if arr[x-1] < arr[x]:
                down[x] = up[x-1]+1
                up[x] = 1
            elif arr[x-1] > arr[x]:
                up[x] = down[x-1]+1
                down[x] = 1
            else:
                up[x] = 1
                down[x] = 1
            
            ans = max(ans, up[x], down[x])
        
        return ans