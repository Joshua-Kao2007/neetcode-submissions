import math
class Solution(object):

    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        L = 1
        R = min_val = max(piles)
        while L < R:
            mid = L+(R-L)//2
            tmp = h
            for pile in piles:
                tmp -= math.ceil(pile/mid)
            if tmp >= 0:
                R = mid
            else:
                L = mid+1

        return L
