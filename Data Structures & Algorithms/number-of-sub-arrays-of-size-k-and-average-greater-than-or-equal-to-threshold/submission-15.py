class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # Prefix Sum solution
        if k == 0 or not arr: return 0
        
        threshold *= k
        # create prefix sum first initialize
        prefix_sum = [0]*(len(arr)+1)
        cur_sum = 0
        for i in range(len(arr)):
            cur_sum += arr[i]
            prefix_sum[i+1] = cur_sum
        
        res = 0
        # calculate thresholds
        for R in range(k-1, len(arr)):
            if prefix_sum[R+1]-prefix_sum[R+1-k] >= threshold:
                res += 1
        return res

