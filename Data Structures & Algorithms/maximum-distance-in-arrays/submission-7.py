class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # 1. Initalize Variables
        m = len(arrays)
        best = 0
        n = len(arrays[0])
        min_val, max_val = arrays[0][0], arrays[0][n-1]

        # 2. O(N) Algorithm
        for i in range(1, len(arrays)):
            n = len(arrays[i])
            best_max = abs(arrays[i][n-1]-min_val)
            best_min = abs(max_val-arrays[i][0])
            if best_max >= best or best_min >= best:
                if best_max >= best_min:
                    max_val = arrays[i][n-1]
                    best = best_max
                else:
                    min_val = arrays[i][0]
                    best = best_min
        return best

        #     # Case 2:




        # # Input: m arrays (sorted in ascending order = no duplicates)
        #     - m = 2
        #         - [5,6], [8,11,13]

        # # Reqs: Two Integers. Two Diff arrays. 
        #     - choose 1 from arr 3. choose 4 from arr 1. 
        # # Output: Integer: maximum distance absolute value (between integers a and b)
        #     - abs of -3 and 10 is 13. 

        # Brute Force:
        # - 1) DeCouple Each List. Given a List[List[int]]
        #     - can decouple to index 0: [1,2,3]
        #     - index 1: [3,4] etc...
        
        # - 2) Within each list. There are no dupliactes. So the min is index 0. Max is last_index-1. 
        #     - [1,2,3] --> index 0 is 1
        #     - index 3-1 --> index is 3
        
        # - 3) Try Every Combo of min-max for each array. So len(arrays)C2 assortments calculate max of max-mins (both combinations)
        #     - O(N^2)

        # - 4) Reqs:
        #     - you can get min with index 0. you get max with length-1 --> O(1) Time to get min and max
        #     - expensive operation to try all combinations
        #     - If there's one index. Each array can only choose 1 as the max or the minimum. 

        # - 5) Another mental model:
        #     - this array can contain the min or the maximum. So try out both and see what gives a better result. If better than everything before it we keep it. 
        #     - Simply keep track of the best absolute difference of everything inf ront of it (worst min), best max that's valid. Then try our combination. If better than replace. We can only replace once. Can't replace max, then replace min, so the check must be done at the same time. 

        # HIGH LEVEL:
        # - Array Index 0 --> We can intialize Min to index 0 and Max to the last index length. Be careful. Boolean marking isValid is False
        # - If 2nd doesn't improve we don't improve...something that starts at index 2. 
        # - so we still have a variable tracking best but cur_min and cur_max belong as they are --> removes edge case where we never am better than index 0, abs will always be greater than zero
        # - Do this check til lwe get to end of array return final best_profit
        # - O(N) check and O(1) space