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
        # if len(arr) < 2: return len(arr)

        # up = [1]*len(arr)
        # down = [1]*len(arr)
        # ans = 1
        # for x in range(1, len(arr)):
        #     if arr[x-1] < arr[x]:
        #         down[x] = down[x-1]+1
        #         up[x] = 1
        #     elif arr[x-1] > arr[x]:
        #         up[x] = up[x-1]+1
        #         down[x] = 1
        #     else:
        #         up[x] = 1
        #         down[x] = 1
            
        #     ans = max(ans, up[x], down[x])
        
        # return ans