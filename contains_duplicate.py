from typing import List, Optional
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # check if duplicates. If yes --> true. Else --> No
        # simple: Set. If in set. Return True. Else No. O(N), O(N)
        used = set()
        for num in nums:
            if num in used:
                return True
            used.add(num)
        return False

sol = Solution()
assert sol.hasDuplicate([1,2,3,3]) == False
assert sol.hasDuplicate([1,2,3,4]) == False


