from collections import Counter
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        cur_max = -1
        for k,v in count.items():
            if k > cur_max and v == 1:
                cur_max = k
        return cur_max