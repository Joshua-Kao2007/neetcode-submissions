class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        up = [1] * n
        down = [1] * n
        ans = 1

        for i in range(1, n):
            if arr[i-1] < arr[i]:
                up[i] = down[i-1] + 1
                down[i] = 1
            elif arr[i-1] > arr[i]:
                down[i] = up[i-1] + 1
                up[i] = 1
            else:
                up[i] = down[i] = 1

            ans = max(ans, up[i], down[i])

        return ans