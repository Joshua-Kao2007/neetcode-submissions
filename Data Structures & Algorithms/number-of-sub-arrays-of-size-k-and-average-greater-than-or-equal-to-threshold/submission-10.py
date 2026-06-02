class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # 1. Edge Case
        if k == 0 or not arr: return 0

        # 2. Initialize Variables
        L, res, curSum = 0,0,0

        # 3. Algorithm
        for R in range(len(arr)):
            curSum += arr[R]
            if R-L+1 == k:
                if (curSum / k) >= threshold:
                    res += 1
                curSum -= arr[L]
                L += 1      

        return res



        # Given List of integers and size K and threshold integer. Find all subarrays of size K that average is greater tha nor equal to threshold. 
        # negative numbers --> not important. 0's don't affect anything. 
        # k assuming is greater than or equal to 0. If zero, return 0?
        # Edge Case: If k is zero, just return 0

        # Core Algorithm: Dynamic Sliding window for the subarray of size k (must be contiguous)...assuming they must be contiguous elements?
        # Slide the window of size k..if it is greater threshold increase count, other wise don't. O(N) solution

        # [2,2,2,2,5,5,5,8] k = 3, threshold = 4

        # Expand Right until R-L+1 == k adding to sum
        # L = 0, R = 0+3-1 = 2, sum = 6 6>4 so add by 1
        # minus Left move Left up by 1...
        # All the way till the end..
        # No edge cases but we'll test later






