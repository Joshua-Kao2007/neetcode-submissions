class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        # largest integer that only occurs once. no integer occurs once return -1
        counter = Counter(nums)
        best = -1
        for num,freq in counter.items():
            if freq > 1:
                continue
            else:
                best = max(best, num)
        return best
            